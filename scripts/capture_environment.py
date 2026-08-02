"""Capture a fixed, redacted set of local or remote research environment facts."""

import argparse
import json
import os
import re
import secrets
import subprocess
from pathlib import Path
from subprocess import CompletedProcess
from typing import Callable, Dict, List, Optional


SECRET_KEYS = ("TOKEN", "PASSWORD", "SECRET", "KEY", "CREDENTIAL")
SSH_HOST_ALIAS = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")


def redact(value: str) -> str:
    """Redact values associated with secret-shaped keys in diagnostic text."""
    lines = []
    for line in value.splitlines():
        key, separator, _ = line.partition("=")
        if separator and (
            key == "CUDA_VISIBLE_DEVICES"
            or any(word in key.upper() for word in SECRET_KEYS)
        ):
            lines.append(f"{key}=<redacted>")
        else:
            lines.append(line)
    return "\n".join(lines)


def parse_probe(stdout: str) -> Dict[str, object]:
    """Parse the JSON object emitted by the fixed allowlisted probe."""
    value = json.loads(stdout)
    if not isinstance(value, dict):
        raise ValueError("environment probe must return a JSON object")
    return value


PROBE_SOURCE = r'''
import json
import platform
import subprocess

def call(args):
    try:
        result = subprocess.run(args, check=False, capture_output=True, text=True)
    except OSError:
        return None
    return result.stdout.strip() if result.returncode == 0 else None

git_status = call(["git", "status", "--porcelain"])
payload = {
    "python": platform.python_version(),
    "git_commit": call(["git", "rev-parse", "HEAD"]),
    "git_dirty": None if git_status is None else bool(git_status),
    "driver_and_gpus": call([
        "nvidia-smi",
        "--query-gpu=driver_version,name,memory.total",
        "--format=csv,noheader",
    ]),
}
try:
    import torch
    payload.update({
        "torch": torch.__version__,
        "torch_cuda": torch.version.cuda,
        "cuda_available": torch.cuda.is_available(),
        "cuda_device_count": torch.cuda.device_count(),
        "cuda_devices": [
            torch.cuda.get_device_name(index)
            for index in range(torch.cuda.device_count())
        ],
    })
    try:
        nccl_version = torch.cuda.nccl.version()
        payload["nccl_version"] = ".".join(map(str, nccl_version))
    except Exception:
        payload["nccl_version"] = None
except Exception as error:
    payload["torch_error"] = type(error).__name__
print(json.dumps(payload, sort_keys=True))
'''


Runner = Callable[..., CompletedProcess[str]]


def write_output(path: Path, contents: str) -> None:
    """Atomically replace a regular output without following a final symlink."""
    destination = path.expanduser()
    if destination.is_symlink():
        raise ValueError("output path must not be a symlink")
    if destination.exists() and not destination.is_file():
        raise ValueError("output path must be a regular file")

    temporary = destination.with_name(
        f".{destination.name}.{secrets.token_hex(8)}.tmp"
    )
    descriptor: Optional[int] = None
    try:
        descriptor = os.open(
            temporary,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o600,
        )
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            descriptor = None
            handle.write(contents)
            handle.flush()
            os.fsync(handle.fileno())
        if destination.is_symlink():
            raise ValueError("output path must not be a symlink")
        if destination.exists() and not destination.is_file():
            raise ValueError("output path must be a regular file")
        os.replace(temporary, destination)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def capture(ssh_host: Optional[str], runner: Runner = subprocess.run) -> Dict[str, object]:
    """Run the allowlisted probe locally or through a caller-supplied SSH alias."""
    command: List[str] = ["python3", "-c", PROBE_SOURCE]
    run_options: Dict[str, object] = {
        "check": False,
        "capture_output": True,
        "text": True,
    }
    if ssh_host:
        if not SSH_HOST_ALIAS.fullmatch(ssh_host):
            raise ValueError("ssh_host must be an SSH Host alias")
        command = ["ssh", ssh_host, "python3", "-"]
        run_options["input"] = PROBE_SOURCE
    result = runner(command, **run_options)
    if result.returncode != 0:
        raise RuntimeError(
            f"environment probe failed with exit code {result.returncode}"
        )
    return parse_probe(result.stdout)


def main(argv: Optional[List[str]] = None) -> int:
    """Run capture and write JSON to stdout or an explicitly requested file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ssh-host", help="existing SSH Host alias for the probe")
    parser.add_argument("--output", type=Path, help="path for captured JSON")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the capture without creating or updating --output",
    )
    arguments = parser.parse_args(argv)
    rendered = json.dumps(capture(arguments.ssh_host), indent=2, sort_keys=True)

    if arguments.output is not None and not arguments.dry_run:
        write_output(arguments.output, f"{rendered}\n")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
