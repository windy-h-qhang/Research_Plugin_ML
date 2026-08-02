import contextlib
import io
import json
import unittest
from pathlib import Path
from subprocess import CompletedProcess

from scripts.inspect_slurm_job import (
    inspect_job,
    main,
    merge_status,
    parse_sacct,
    parse_squeue,
)

FIXTURES = Path(__file__).with_name("fixtures")


class InspectSlurmTests(unittest.TestCase):
    def test_parse_running_queue_job(self) -> None:
        job = parse_squeue((FIXTURES / "squeue-running.txt").read_text())

        self.assertEqual(job["job_id"], "123")
        self.assertEqual(job["status"], "running")

    def test_accounting_completion_overrides_empty_queue(self) -> None:
        final = parse_sacct((FIXTURES / "sacct-completed.txt").read_text())

        merged = merge_status({}, final)

        self.assertEqual(merged["status"], "completed")
        self.assertEqual(merged["stdout_path"], "/logs/job-123.out")
        self.assertEqual(merged["stderr_path"], "/logs/job-123.err")

    def test_oom_is_classified_as_resource_failure(self) -> None:
        final = parse_sacct((FIXTURES / "sacct-oom.txt").read_text())

        self.assertEqual(final["failure_class"], "resource")

    def test_official_terminal_failure_states_are_not_unknown(self) -> None:
        cases = {
            "BOOT_FAIL": ("failed", "scheduler_or_preemption"),
            "DEADLINE": ("failed", "scheduler_or_preemption"),
            "PREEMPTED": ("failed", "scheduler_or_preemption"),
            "LAUNCH_FAILED": ("failed", "scheduler_or_preemption"),
            "RECONFIG_FAIL": ("failed", "scheduler_or_preemption"),
            "NODE_FAIL": ("failed", "resource"),
            "OUT_OF_MEMORY": ("failed", "resource"),
            "TIMEOUT": ("failed", "resource"),
        }
        for raw_state, (status, failure_class) in cases.items():
            with self.subTest(raw_state=raw_state):
                final = parse_sacct(
                    f"123|{raw_state}|0:0|00:01:00|1G\n"
                )
                self.assertEqual(final["status"], status)
                self.assertEqual(final["failure_class"], failure_class)

    def test_official_nonterminal_states_preserve_liveness(self) -> None:
        running_states = (
            "SUSPENDED",
            "STOPPED",
            "SIGNALING",
            "RESIZING",
            "STAGE_OUT",
        )
        queued_states = (
            "EXPEDITING",
            "REQUEUED",
            "REQUEUE_FED",
            "REQUEUE_HOLD",
            "RESV_DEL_HOLD",
            "SPECIAL_EXIT",
            "CONFIGURING",
            "POWER_UP_NODE",
        )
        for raw_state in running_states:
            with self.subTest(raw_state=raw_state, status="running"):
                self.assertEqual(
                    parse_sacct(
                        f"123|{raw_state}|0:0|00:01:00|1G\n"
                    )["status"],
                    "running",
                )
                self.assertEqual(
                    parse_squeue(
                        f"123|{raw_state}|node01|00:01:00|gpu:1\n"
                    )["status"],
                    "running",
                )
        for raw_state in queued_states:
            with self.subTest(raw_state=raw_state, status="queued"):
                accounting = parse_sacct(
                    f"123|{raw_state}|0:0|00:01:00|1G\n"
                )
                self.assertEqual(accounting["status"], "queued")
                self.assertEqual(
                    parse_squeue(
                        f"123|{raw_state}|node01|00:01:00|gpu:1\n"
                    )["status"],
                    "queued",
                )
                self.assertNotIn("failure_class", accounting)

        for raw_state in ("SUSPENDED", "REQUEUED", "SPECIAL_EXIT"):
            with self.subTest(raw_state=raw_state, classification="nonterminal"):
                accounting = parse_sacct(
                    f"123|{raw_state}|0:0|00:01:00|1G\n"
                )
                self.assertNotIn("failure_class", accounting)

    def test_federation_revocation_is_terminal_without_code_failure(self) -> None:
        revoked = parse_sacct(
            "123|REVOKED|0:0|00:01:00|1G\n"
        )

        self.assertEqual(revoked["status"], "cancelled")
        self.assertEqual(
            revoked["failure_class"],
            "scheduler_or_preemption",
        )

    def test_nonterminal_states_ignore_stale_nonzero_exit_codes(self) -> None:
        cases = {
            "SPECIAL_EXIT": "queued",
            "REQUEUED": "queued",
            "REQUEUE_FED": "queued",
            "REQUEUE_HOLD": "queued",
            "RESV_DEL_HOLD": "queued",
            "SUSPENDED": "running",
            "STOPPED": "running",
            "SIGNALING": "running",
            "RESIZING": "running",
            "STAGE_OUT": "running",
        }
        for raw_state, expected_status in cases.items():
            with self.subTest(raw_state=raw_state):
                accounting = parse_sacct(
                    f"123|{raw_state}|1:0|00:01:00|1G\n"
                )
                self.assertEqual(accounting["status"], expected_status)
                self.assertNotIn("failure_class", accounting)

    def test_child_resource_failure_refines_failed_parent_without_replacing_it(
        self,
    ) -> None:
        """A decisive child OOM must refine, not replace, parent job evidence."""
        final = parse_sacct(
            (FIXTURES / "sacct-parent-failed-child-oom.txt").read_text()
        )

        self.assertEqual(final["status"], "failed")
        self.assertEqual(final["failure_class"], "resource")
        self.assertEqual(final["job_id"], "123")
        self.assertEqual(final["raw_state"], "FAILED")
        self.assertEqual(final["exit_code"], "1:0")
        self.assertEqual(final["stdout_path"], "/logs/job-123.out")
        self.assertEqual(final["stderr_path"], "/logs/job-123.err")
        self.assertEqual(
            final["decisive_step"]["job_id"],
            "123.batch",
        )
        self.assertEqual(
            final["decisive_step"]["raw_state"],
            "OUT_OF_MEMORY",
        )
        self.assertEqual(final["steps"], [final["decisive_step"]])

    def test_live_queue_keeps_parent_status_and_structured_child_failure(
        self,
    ) -> None:
        """A nonterminal parent must not be replaced by a terminal child step."""
        queue = parse_squeue((FIXTURES / "squeue-running.txt").read_text())
        accounting = parse_sacct(
            (FIXTURES / "sacct-parent-running-child-oom.txt").read_text()
        )

        self.assertEqual(accounting["job_id"], "123")
        self.assertEqual(accounting["status"], "running")
        self.assertEqual(accounting["stdout_path"], "/logs/job-123.out")
        self.assertEqual(accounting["stderr_path"], "/logs/job-123.err")
        self.assertEqual(
            [step["job_id"] for step in accounting["steps"]],
            ["123.batch", "123.extern"],
        )
        self.assertEqual(accounting["steps"][0]["failure_class"], "resource")
        self.assertEqual(accounting["steps"][0]["max_rss"], "20G")

        merged = merge_status(queue, accounting)

        self.assertEqual(merged["job_id"], "123")
        self.assertEqual(merged["status"], "running")
        self.assertEqual(merged["node"], "node01")
        self.assertEqual(merged["elapsed"], "00:03:10")
        self.assertEqual(merged["stdout_path"], "/logs/job-123.out")
        self.assertEqual(merged["stderr_path"], "/logs/job-123.err")
        self.assertEqual(merged["steps"], accounting["steps"])

    def test_completed_parent_retains_child_resource_measurement(self) -> None:
        """Blank parent MaxRSS must not discard stable child resource evidence."""
        final = parse_sacct(
            (FIXTURES / "sacct-parent-completed-child-rss.txt").read_text()
        )

        self.assertEqual(final["job_id"], "123")
        self.assertEqual(final["status"], "completed")
        self.assertEqual(final["max_rss"], "")
        self.assertEqual(final["steps"][0]["job_id"], "123.batch")
        self.assertEqual(final["steps"][0]["max_rss"], "4G")
        self.assertEqual(final["stdout_path"], "/logs/job-123.out")
        self.assertEqual(final["stderr_path"], "/logs/job-123.err")

    def test_malformed_row_does_not_hide_valid_terminal_step(self) -> None:
        """Treating an empty job ID as a parent would mask valid step evidence."""
        final = parse_sacct(
            "||||\n123.batch|FAILED|1:0|00:01:00|1G\n"
        )

        self.assertEqual(final["job_id"], "123.batch")
        self.assertEqual(final["status"], "failed")
        self.assertEqual(final["failure_class"], "code_or_data")

    def test_resource_state_without_job_id_is_not_decisive(self) -> None:
        """A malformed resource row must not override valid parent evidence."""
        final = parse_sacct(
            "123|COMPLETED|0:0|00:01:00|1G\n"
            "|OUT_OF_MEMORY|0:125|00:01:00|20G\n"
        )

        self.assertEqual(final["job_id"], "123")
        self.assertEqual(final["status"], "completed")
        self.assertNotIn("failure_class", final)

    def test_nonzero_application_exit_is_classified_pending_diagnosis(self) -> None:
        """Ignoring a nonzero process exit would hide code or data evidence."""
        final = parse_sacct("123|COMPLETED|2:0|00:01:00|1G\n")

        self.assertEqual(final["raw_state"], "COMPLETED")
        self.assertEqual(final["status"], "failed")
        self.assertEqual(final["exit_code"], "2:0")
        self.assertEqual(final["failure_class"], "code_or_data")

    def test_sparse_accounting_rows_are_trimmed_without_parse_errors(self) -> None:
        """Leaving Slurm column padding intact would corrupt preserved evidence."""
        final = parse_sacct(
            "\n  123 | CANCELLED by 1000 | 0:15 | 00:02:00 \n"
        )

        self.assertEqual(final["job_id"], "123")
        self.assertEqual(final["raw_state"], "CANCELLED by 1000")
        self.assertEqual(final["status"], "cancelled")
        self.assertEqual(final["exit_code"], "0:15")
        self.assertEqual(final["max_rss"], "")
        self.assertEqual(parse_squeue("\n \n"), {})

    def test_local_inspection_uses_fixed_read_only_queries(self) -> None:
        """Changing either fixed query would weaken stable status inspection."""
        calls: list[tuple[list[str], dict[str, object]]] = []
        responses = [
            CompletedProcess([], 0, "123|RUNNING|node01|00:03:10|gpu:1\n", ""),
            CompletedProcess([], 0, "", ""),
        ]

        def runner(command: list[str], **kwargs: object) -> CompletedProcess[str]:
            calls.append((command, kwargs))
            return responses.pop(0)

        result = inspect_job("123", runner=runner)

        self.assertEqual(result["status"], "running")
        self.assertEqual(calls, [
            (
                [
                    "squeue",
                    "--noheader",
                    "--jobs=123",
                    "--format=%i|%T|%N|%M|%b",
                ],
                {"check": False, "capture_output": True, "text": True},
            ),
            (
                [
                    "sacct",
                    "--noheader",
                    "--parsable2",
                    "--jobs=123",
                    "--format=JobIDRaw,State,ExitCode,Elapsed,MaxRSS,StdOut,StdErr",
                ],
                {"check": False, "capture_output": True, "text": True},
            ),
        ])

    def test_terminal_sacct_wins_over_failed_squeue_with_sanitized_evidence(
        self,
    ) -> None:
        """Failed-query output must not create false or unsafe evidence."""
        responses = [
            CompletedProcess(
                [],
                1,
                "123|RUNNING|node01|00:03:10|gpu:1\n",
                "TOKEN=abc123\n/private/squeue/path",
            ),
            CompletedProcess([], 0, "123|COMPLETED|0:0|00:10:00|4G\n", ""),
        ]

        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            response = responses.pop(0)
            response.args = command
            return response

        result = inspect_job("123", runner=runner)

        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["inspection_errors"], [
            {"command": "squeue", "return_code": 1},
        ])
        self.assertNotIn("abc123", str(result))
        self.assertNotIn("/private", str(result))

    def test_nonzero_empty_query_is_not_treated_like_zero_empty(self) -> None:
        """Silently accepting an empty failed query would hide inspection failure."""
        cases = [
            (
                [
                    CompletedProcess([], 1, "", "squeue private detail"),
                    CompletedProcess([], 0, "", ""),
                ],
                {"command": "squeue", "return_code": 1},
            ),
            (
                [
                    CompletedProcess([], 0, "", ""),
                    CompletedProcess([], 2, "", "sacct private detail"),
                ],
                {"command": "sacct", "return_code": 2},
            ),
        ]
        for responses, expected_error in cases:
            with self.subTest(command=expected_error["command"]):
                def runner(
                    command: list[str],
                    **_kwargs: object,
                ) -> CompletedProcess[str]:
                    response = responses.pop(0)
                    response.args = command
                    return response

                result = inspect_job("123", runner=runner)

                self.assertEqual(result["status"], "unknown")
                self.assertEqual(result["inspection_errors"], [expected_error])
                self.assertNotIn("private detail", str(result))
                self.assertNotEqual(result.get("failure_class"), "remote")

    def test_remote_inspection_quotes_fixed_formats_and_falls_back_to_sacct(
        self,
    ) -> None:
        """Passing raw pipe tokens to SSH would let its remote shell alter the query."""
        calls: list[tuple[list[str], dict[str, object]]] = []
        responses = [
            CompletedProcess([], 0, "\n", ""),
            CompletedProcess([], 0, "123|COMPLETED|0:0|00:10:00|4G\n", ""),
        ]

        def runner(command: list[str], **kwargs: object) -> CompletedProcess[str]:
            calls.append((command, kwargs))
            return responses.pop(0)

        result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

        self.assertEqual(result["status"], "completed")
        self.assertEqual(calls, [
            (
                [
                    "ssh",
                    "gpu-lab",
                    "squeue --noheader --jobs=123 "
                    "'--format=%i|%T|%N|%M|%b'",
                ],
                {"check": False, "capture_output": True, "text": True},
            ),
            (
                [
                    "ssh",
                    "gpu-lab",
                    "sacct --noheader --parsable2 --jobs=123 "
                    "--format=JobIDRaw,State,ExitCode,Elapsed,MaxRSS,StdOut,StdErr",
                ],
                {"check": False, "capture_output": True, "text": True},
            ),
        ])

    def test_running_queue_survives_remote_accounting_inspection_failures(
        self,
    ) -> None:
        """Accounting transport loss must not erase authoritative live queue evidence."""
        cases = [
            (
                CompletedProcess(
                    [],
                    255,
                    "",
                    "TOKEN=abc123 /Users/person/.ssh/private-config",
                ),
                None,
                {
                    "command": "sacct",
                    "return_code": 255,
                    "failure_class": "remote",
                    "diagnostic": "SSH transport failed",
                },
            ),
            (
                None,
                OSError("TOKEN=abc123 /Users/person/.ssh/private-config"),
                {
                    "command": "sacct",
                    "failure_class": "remote",
                    "diagnostic": "SSH transport failed",
                },
            ),
            (
                CompletedProcess(
                    [],
                    2,
                    "",
                    "TOKEN=abc123 /Users/person/private-accounting",
                ),
                None,
                {"command": "sacct", "return_code": 2},
            ),
        ]
        for accounting_response, accounting_error, expected_error in cases:
            with self.subTest(expected_error=expected_error):
                call_count = 0

                def runner(
                    command: list[str],
                    **_kwargs: object,
                ) -> CompletedProcess[str]:
                    nonlocal call_count
                    call_count += 1
                    if call_count == 1:
                        return CompletedProcess(
                            command,
                            0,
                            "123|RUNNING|node01|00:03:10|gpu:1\n",
                            "",
                        )
                    if accounting_error:
                        raise accounting_error
                    assert accounting_response is not None
                    accounting_response.args = command
                    return accounting_response

                result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

                self.assertEqual(result["status"], "running")
                self.assertEqual(result["raw_state"], "RUNNING")
                self.assertEqual(result["inspection_errors"], [expected_error])
                self.assertNotIn("abc123", str(result))
                self.assertNotIn("/Users/person", str(result))

    def test_inspection_rejects_option_and_shell_injection_inputs(self) -> None:
        """Accepting unsafe caller input would alter local or remote commands."""
        def runner(
            _command: list[str],
            **_kwargs: object,
        ) -> CompletedProcess[str]:
            self.fail("invalid input must be rejected before running a command")

        invalid_inputs = [
            ("--help", None),
            ("123;scancel 7", None),
            ("123", "-F"),
            ("123", "gpu-lab;whoami"),
        ]
        for job_id, ssh_host in invalid_inputs:
            with self.subTest(job_id=job_id, ssh_host=ssh_host):
                with self.assertRaises(ValueError):
                    inspect_job(job_id, ssh_host=ssh_host, runner=runner)

    def test_ssh_transport_failure_is_classified_without_leaking_stderr(self) -> None:
        """Returning raw SSH stderr could disclose aliases, paths, or credentials."""
        calls: list[list[str]] = []

        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            calls.append(command)
            return CompletedProcess(
                command,
                255,
                "",
                "TOKEN=abc123\nssh: /Users/person/.ssh/private-config",
            )

        result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

        self.assertEqual(result["status"], "unknown")
        self.assertEqual(result["failure_class"], "remote")
        self.assertEqual(result["query_exit_code"], 255)
        self.assertNotIn("abc123", str(result))
        self.assertNotIn("/Users/person", str(result))
        self.assertEqual(len(calls), 1)

    def test_sacct_transport_failure_is_classified_as_remote(self) -> None:
        """Losing SSH after squeue must not be mistaken for a missing job."""
        responses = [
            CompletedProcess([], 0, "", ""),
            CompletedProcess([], 255, "", "connection reset by peer"),
        ]

        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            response = responses.pop(0)
            response.args = command
            return response

        result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

        self.assertEqual(result["status"], "unknown")
        self.assertEqual(result["failure_class"], "remote")
        self.assertEqual(result["query_exit_code"], 255)

    def test_ssh_invocation_error_is_classified_without_error_details(self) -> None:
        """An SSH launch exception must not leak its potentially sensitive text."""
        def runner(
            _command: list[str],
            **_kwargs: object,
        ) -> CompletedProcess[str]:
            raise OSError("private path /Users/person/.ssh/control")

        result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

        self.assertEqual(result["status"], "unknown")
        self.assertEqual(result["failure_class"], "remote")
        self.assertNotIn("/Users/person", str(result))

    def test_sacct_invocation_error_is_classified_as_remote(self) -> None:
        """A transport exception during fallback must not become a missing job."""
        call_count = 0

        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return CompletedProcess(command, 0, "", "")
            raise OSError("connection closed")

        result = inspect_job("123", ssh_host="gpu-lab", runner=runner)

        self.assertEqual(result["status"], "unknown")
        self.assertEqual(result["failure_class"], "remote")

    def test_cli_renders_remote_status_as_json(self) -> None:
        """Failing to serialize the result would make the script unusable directly."""
        responses = [
            CompletedProcess([], 0, "", ""),
            CompletedProcess([], 0, "123|COMPLETED|0:0|00:10:00|4G\n", ""),
        ]

        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            response = responses.pop(0)
            response.args = command
            return response

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exit_code = main(
                ["123", "--ssh-host", "gpu-lab"],
                runner=runner,
            )

        self.assertEqual(exit_code, 0)
        self.assertEqual(json.loads(stdout.getvalue())["status"], "completed")
