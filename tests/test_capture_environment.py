import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import patch

from scripts.capture_environment import PROBE_SOURCE, capture, main, parse_probe, redact


class CaptureEnvironmentTests(unittest.TestCase):
    def test_fixed_probe_survives_missing_git_and_nvidia_tools(self) -> None:
        """CPU hosts and failed Git inspection must remain representable."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = subprocess.run(
                [sys.executable, "-c", PROBE_SOURCE],
                cwd=temporary_directory,
                env={**os.environ, "PATH": ""},
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertIsNone(payload["git_commit"])
        self.assertIsNone(payload["git_dirty"])
        self.assertIsNone(payload["driver_and_gpus"])

    def test_redact_hides_secret_shaped_values(self) -> None:
        """Removing secret-key handling would expose the supplied credentials."""
        text = "TOKEN=abc123\nPASSWORD=hunter2\nCUDA_VISIBLE_DEVICES=0,1"

        redacted = redact(text)

        self.assertNotIn("abc123", redacted)
        self.assertNotIn("hunter2", redacted)
        self.assertIn("CUDA_VISIBLE_DEVICES=<redacted>", redacted)

    def test_parse_probe_accepts_json_only(self) -> None:
        """Returning raw JSON or a different data shape would break callers."""
        result = parse_probe('{"python":"3.11","torch":"2.7","cuda":"12.8"}')

        self.assertEqual(result["torch"], "2.7")

    def test_parse_probe_rejects_non_object(self) -> None:
        """Accepting a JSON array would violate the probe result contract."""
        with self.assertRaises(ValueError):
            parse_probe('["unexpected"]')

    def test_local_fixture_serializes_nccl_version_as_a_dotted_string(self) -> None:
        """A non-string NCCL version would make environment captures inconsistent."""
        fixture_path = Path(__file__).with_name("fixtures") / "environment-local.json"

        result = parse_probe(fixture_path.read_text())

        self.assertEqual(result["nccl_version"], "2.27.3")

    def test_capture_routes_probe_to_the_supplied_ssh_alias(self) -> None:
        """Passing a multiline probe as a remote argument would be shell-unsafe."""
        calls: list[tuple[list[str], dict[str, object]]] = []
        fixture_path = Path(__file__).with_name("fixtures") / "environment-local.json"
        expected = json.loads(fixture_path.read_text())

        def runner(command: list[str], **kwargs: object) -> CompletedProcess[str]:
            calls.append((command, kwargs))
            return CompletedProcess(command, 0, json.dumps(expected), "")

        result = capture("gpu-lab", runner)

        self.assertEqual(result, expected)
        self.assertEqual(calls, [(
            ["ssh", "gpu-lab", "python3", "-"],
            {
                "check": False,
                "capture_output": True,
                "input": PROBE_SOURCE,
                "text": True,
            },
        )])

    def test_capture_rejects_an_ssh_option_instead_of_a_host_alias(self) -> None:
        """Treating an SSH option as an alias could alter how SSH finds its config."""
        def runner(command: list[str], **_kwargs: object) -> CompletedProcess[str]:
            return CompletedProcess(command, 0, '{"python":"3.11"}', "")

        with self.assertRaises(ValueError):
            capture("-F", runner)

    def test_probe_failure_is_fail_closed_locally_and_over_ssh(self) -> None:
        """Arbitrary probe stderr must never cross the capture boundary."""
        private_stderr = (
            "https://alice:password@example.test/path\n"
            "Authorization: Bearer secret-token\n"
            '{"token":"json-secret"}\n'
            "/Users/alice/private/research"
        )
        for ssh_host in (None, "gpu-lab"):
            with self.subTest(ssh_host=ssh_host):
                def runner(
                    command: list[str],
                    **_kwargs: object,
                ) -> CompletedProcess[str]:
                    return CompletedProcess(command, 23, "", private_stderr)

                with self.assertRaisesRegex(
                    RuntimeError,
                    r"\Aenvironment probe failed with exit code 23\Z",
                ) as raised:
                    capture(ssh_host, runner)

                rendered = str(raised.exception)
                for secret in (
                    "alice",
                    "password",
                    "Bearer",
                    "secret-token",
                    "json-secret",
                    "/Users",
                ):
                    self.assertNotIn(secret, rendered)

    def test_dry_run_does_not_create_the_requested_output_file(self) -> None:
        """Writing an output file during a dry run would make the command mutating."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "environment.json"
            output_path.write_text("previous capture\n")
            stdout = io.StringIO()
            with patch(
                "scripts.capture_environment.capture",
                return_value={"python": "3.11"},
            ):
                with contextlib.redirect_stdout(stdout):
                    exit_code = main(["--output", str(output_path), "--dry-run"])

            self.assertEqual(output_path.read_text(), "previous capture\n")

        self.assertEqual(exit_code, 0)
        self.assertEqual(json.loads(stdout.getvalue()), {"python": "3.11"})

    def test_output_rejects_symlink_without_touching_target(self) -> None:
        """An untrusted checkout must not redirect environment output."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            target = root / "outside.json"
            target.write_text("preserve me\n")
            output = root / "environment.json"
            output.symlink_to(target)

            with patch(
                "scripts.capture_environment.capture",
                return_value={"python": "3.11"},
            ):
                with self.assertRaisesRegex(
                    ValueError, "output path must not be a symlink"
                ):
                    main(["--output", str(output)])

            self.assertEqual(target.read_text(), "preserve me\n")
            self.assertTrue(output.is_symlink())
