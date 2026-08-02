"""Inspect and normalize read-only Slurm job status."""

import argparse
import json
import re
import shlex
import subprocess
from subprocess import CompletedProcess
from typing import Callable, Dict, List, Optional


STATE_MAP = {
    "PENDING": "queued",
    "CONFIGURING": "queued",
    "EXPEDITING": "queued",
    "POWER_UP_NODE": "queued",
    "REQUEUED": "queued",
    "REQUEUE_FED": "queued",
    "REQUEUE_HOLD": "queued",
    "RESV_DEL_HOLD": "queued",
    "SPECIAL_EXIT": "queued",
    "RUNNING": "running",
    "COMPLETING": "running",
    "RESIZING": "running",
    "SIGNALING": "running",
    "STAGE_OUT": "running",
    "STOPPED": "running",
    "SUSPENDED": "running",
    "COMPLETED": "completed",
    "FAILED": "failed",
    "BOOT_FAIL": "failed",
    "DEADLINE": "failed",
    "LAUNCH_FAILED": "failed",
    "OUT_OF_MEMORY": "failed",
    "NODE_FAIL": "failed",
    "PREEMPTED": "failed",
    "RECONFIG_FAIL": "failed",
    "REVOKED": "cancelled",
    "CANCELLED": "cancelled",
    "TIMEOUT": "failed",
}
RESOURCE_FAILURE_STATES = {"NODE_FAIL", "OUT_OF_MEMORY", "TIMEOUT"}
SCHEDULER_FAILURE_STATES = {
    "BOOT_FAIL",
    "DEADLINE",
    "LAUNCH_FAILED",
    "PREEMPTED",
    "RECONFIG_FAIL",
    "REVOKED",
}
JOB_ID = re.compile(r"[1-9][0-9]*\Z")
SSH_HOST_ALIAS = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")

Runner = Callable[..., CompletedProcess[str]]


def _first_line(text: str) -> List[str]:
    line = next((item for item in text.splitlines() if item.strip()), "")
    return [field.strip() for field in line.split("|")] if line else []


def _nonzero_exit(exit_code: str) -> bool:
    parts = exit_code.split(":")
    return len(parts) == 2 and all(part.isdigit() for part in parts) and any(
        int(part) != 0 for part in parts
    )


def _remote_transport_failure(
    ssh_host: Optional[str],
    result: CompletedProcess[str],
) -> Optional[Dict[str, object]]:
    if not ssh_host or result.returncode != 255:
        return None
    return {
        "status": "unknown",
        "failure_class": "remote",
        "query_exit_code": result.returncode,
        "diagnostic": "SSH transport failed",
    }


def parse_squeue(text: str) -> Dict[str, object]:
    """Parse the first non-empty row from fixed pipe-delimited squeue output."""
    fields = _first_line(text)
    if not fields:
        return {}
    job_id, raw_state, node, elapsed, tres = (fields + [""] * 5)[:5]
    return {
        "job_id": job_id,
        "status": STATE_MAP.get(raw_state.upper(), "unknown"),
        "raw_state": raw_state,
        "node": node,
        "elapsed": elapsed,
        "resources": tres,
    }


def parse_sacct(text: str) -> Dict[str, object]:
    """Parse fixed pipe-delimited sacct rows without losing parent identity."""
    rows = [
        [field.strip() for field in line.split("|")]
        for line in text.splitlines()
        if line.strip()
    ]
    if not rows:
        return {}
    results = [_parse_sacct_row(fields) for fields in rows]
    parent_results = [
        result
        for result in results
        if result["job_id"] and "." not in str(result["job_id"])
    ]
    step_results = [
        result
        for result in results
        if result["job_id"] and "." in str(result["job_id"])
    ]
    if parent_results:
        parent = dict(parent_results[0])
        if step_results:
            parent["steps"] = step_results
        resource_step = next(
            (
                step
                for step in step_results
                if step.get("failure_class") == "resource"
            ),
            None,
        )
        if parent["status"] == "failed" and resource_step:
            parent["failure_class"] = "resource"
            parent["decisive_step"] = resource_step
        return parent

    candidates = [
        result for result in results if result["job_id"]
    ]
    if not candidates:
        return {}
    decisive = next(
        (
            result
            for result in candidates
            if result.get("failure_class") == "resource"
        ),
        None,
    )
    if decisive:
        return decisive
    status_rank = {
        "failed": 0,
        "cancelled": 1,
        "completed": 2,
        "running": 3,
        "queued": 4,
        "unknown": 5,
    }
    return min(
        candidates,
        key=lambda result: status_rank[str(result["status"])],
    )


def _parse_sacct_row(fields: List[str]) -> Dict[str, object]:
    job_id, raw_state, exit_code, elapsed, max_rss, stdout_path, stderr_path = (
        fields + [""] * 7
    )[:7]
    state = raw_state.upper().split()[0] if raw_state.strip() else ""
    result: Dict[str, object] = {
        "job_id": job_id,
        "status": STATE_MAP.get(state, "unknown"),
        "raw_state": raw_state,
        "exit_code": exit_code,
        "elapsed": elapsed,
        "max_rss": max_rss,
        "stdout_path": stdout_path,
        "stderr_path": stderr_path,
    }
    if state in RESOURCE_FAILURE_STATES:
        result["failure_class"] = "resource"
    elif state in SCHEDULER_FAILURE_STATES:
        result["failure_class"] = "scheduler_or_preemption"
    elif result["status"] == "failed":
        result["failure_class"] = "code_or_data"
    elif result["status"] == "completed" and _nonzero_exit(exit_code):
        result["status"] = "failed"
        result["failure_class"] = "code_or_data"
    return result


def merge_status(
    queue: Dict[str, object],
    accounting: Dict[str, object],
) -> Dict[str, object]:
    """Prefer terminal parents; enrich live queue state with accounting detail."""
    if accounting.get("status") in {"completed", "failed", "cancelled"}:
        return dict(accounting)
    if queue:
        merged = dict(accounting)
        merged.update(queue)
        return merged
    return dict(accounting) if accounting else {"status": "unknown"}


def inspect_job(
    job_id: str,
    ssh_host: Optional[str] = None,
    runner: Runner = subprocess.run,
) -> Dict[str, object]:
    """Inspect a Slurm job using fixed, read-only local or SSH queries."""
    if not JOB_ID.fullmatch(job_id):
        raise ValueError("job_id must be a positive numeric Slurm job ID")
    if ssh_host and not SSH_HOST_ALIAS.fullmatch(ssh_host):
        raise ValueError("ssh_host must be an SSH Host alias")
    run_options: Dict[str, object] = {
        "check": False,
        "capture_output": True,
        "text": True,
    }
    squeue_command = [
        "squeue",
        "--noheader",
        f"--jobs={job_id}",
        "--format=%i|%T|%N|%M|%b",
    ]
    sacct_command = [
        "sacct",
        "--noheader",
        "--parsable2",
        f"--jobs={job_id}",
        "--format=JobIDRaw,State,ExitCode,Elapsed,MaxRSS,StdOut,StdErr",
    ]
    if ssh_host:
        squeue_command = ["ssh", ssh_host, shlex.join(squeue_command)]
        sacct_command = ["ssh", ssh_host, shlex.join(sacct_command)]
    try:
        queue_result = runner(squeue_command, **run_options)
    except OSError:
        if ssh_host:
            return {
                "status": "unknown",
                "failure_class": "remote",
                "diagnostic": "SSH transport failed",
            }
        raise
    transport_failure = _remote_transport_failure(ssh_host, queue_result)
    if transport_failure:
        return transport_failure
    inspection_errors = []
    queue = parse_squeue(queue_result.stdout)
    if queue_result.returncode != 0:
        queue = {}
        inspection_errors.append({
            "command": "squeue",
            "return_code": queue_result.returncode,
        })
    try:
        accounting_result = runner(sacct_command, **run_options)
    except OSError:
        if ssh_host:
            if not queue:
                return {
                    "status": "unknown",
                    "failure_class": "remote",
                    "diagnostic": "SSH transport failed",
                }
            accounting = {}
            inspection_errors.append({
                "command": "sacct",
                "failure_class": "remote",
                "diagnostic": "SSH transport failed",
            })
        else:
            raise
    else:
        transport_failure = _remote_transport_failure(ssh_host, accounting_result)
        if transport_failure and not queue:
            return transport_failure
        if transport_failure:
            accounting = {}
            inspection_errors.append({
                "command": "sacct",
                "return_code": accounting_result.returncode,
                "failure_class": "remote",
                "diagnostic": "SSH transport failed",
            })
        else:
            accounting = parse_sacct(accounting_result.stdout)
            if accounting_result.returncode != 0:
                accounting = {}
                inspection_errors.append({
                    "command": "sacct",
                    "return_code": accounting_result.returncode,
                })
    merged = merge_status(queue, accounting)
    if inspection_errors:
        merged["inspection_errors"] = inspection_errors
    return merged


def main(
    argv: Optional[List[str]] = None,
    runner: Runner = subprocess.run,
) -> int:
    """Inspect one local or remote Slurm job and print normalized JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job_id", help="positive numeric Slurm job ID")
    parser.add_argument("--ssh-host", help="existing SSH Host alias")
    arguments = parser.parse_args(argv)
    result = inspect_job(
        arguments.job_id,
        ssh_host=arguments.ssh_host,
        runner=runner,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
