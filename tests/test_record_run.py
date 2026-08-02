import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import scripts.record_run as record_module
from scripts.record_run import main, upsert_run, validate_record


class RecordRunTests(unittest.TestCase):
    def test_planned_record_does_not_invent_a_start_time(self) -> None:
        """A planned command is valid before execution has started."""
        record = {
            "run_id": "r1",
            "experiment_id": "e1",
            "status": "planned",
            "environment_id": "local",
            "command": "python train.py",
        }

        self.assertEqual(validate_record(record), [])

    def test_started_at_is_required_after_planning(self) -> None:
        """Execution states require a durable start timestamp."""
        record = {
            "run_id": "r1",
            "experiment_id": "e1",
            "status": "running",
            "environment_id": "local",
            "command": "python train.py",
        }

        self.assertIn("started_at is required", validate_record(record))

    def test_validate_requires_identity_and_execution_fields(self) -> None:
        """Removing required-field validation would admit incomplete run records."""
        errors = validate_record({"run_id": "r1"})

        self.assertIn("experiment_id is required", errors)
        self.assertIn("status is required", errors)

    def test_validate_rejects_unsupported_status(self) -> None:
        """Allowing an unrecognized state would make run progress ambiguous."""
        errors = validate_record({
            "run_id": "r1",
            "experiment_id": "e1",
            "status": "paused",
            "environment_id": "local",
            "command": "python train.py",
            "started_at": "2026-07-29T00:00:00Z",
        })

        self.assertIn("unsupported status: paused", errors)

    def test_upsert_preserves_unknown_fields(self) -> None:
        """Replacing rather than merging a record would discard user metadata."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "r1.json"
            path.write_text('{"run_id":"r1","custom":{"owner":"lab"}}')

            result = upsert_run(path, {
                "experiment_id": "e1",
                "status": "planned",
                "environment_id": "local",
                "command": "python train.py",
                "started_at": "2026-07-29T00:00:00Z",
            })

            self.assertEqual(result["custom"], {"owner": "lab"})
            self.assertTrue(path.exists())

    def test_dry_run_does_not_write(self) -> None:
        """Writing a run record during a dry run would make inspection mutating."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "r1.json"

            result = upsert_run(path, {
                "run_id": "r1",
                "experiment_id": "e1",
                "status": "planned",
                "environment_id": "local",
                "command": "python train.py",
                "started_at": "2026-07-29T00:00:00Z",
            }, dry_run=True)

            self.assertEqual(result["run_id"], "r1")
            self.assertFalse(path.exists())

    def test_cli_records_repeated_artifact_references_under_root(self) -> None:
        """Dropping artifacts or using another directory would lose reproducibility data."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            with contextlib.redirect_stdout(io.StringIO()):
                exit_code = main([
                    "--root", str(root),
                    "--run-id", "r1",
                    "--experiment-id", "e1",
                    "--status", "completed",
                    "--environment-id", "local",
                    "--command", "python train.py",
                    "--started-at", "2026-07-29T00:00:00Z",
                    "--artifact", "outputs/metrics.json",
                    "--artifact", "checkpoints/r1.ckpt",
                ])

            record_path = root / ".research/runs/r1.json"
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                upsert_run(record_path, {}, dry_run=True)["artifacts"],
                ["outputs/metrics.json", "checkpoints/r1.ckpt"],
            )

    def test_cli_rejects_run_id_that_escapes_runs_directory(self) -> None:
        """Accepting path components in a run ID could write outside run metadata."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    main([
                        "--root", str(root),
                        "--run-id", "../outside",
                        "--experiment-id", "e1",
                        "--status", "planned",
                        "--environment-id", "local",
                        "--command", "python train.py",
                        "--started-at", "2026-07-29T00:00:00Z",
                    ])

            self.assertFalse((root / ".research/runs/outside.json").exists())

    def test_cli_rejects_research_symlink_outside_requested_root(self) -> None:
        """Following an in-root symlink would let the CLI write outside its root."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "root"
            outside = Path(temporary_directory) / "outside"
            root.mkdir()
            outside.mkdir()
            (root / ".research").symlink_to(outside, target_is_directory=True)

            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    main([
                        "--root", str(root),
                        "--run-id", "r1",
                        "--experiment-id", "e1",
                        "--status", "planned",
                        "--environment-id", "local",
                        "--command", "python train.py",
                        "--started-at", "2026-07-29T00:00:00Z",
                    ])

            self.assertFalse((outside / "runs/r1.json").exists())

    def test_cli_rejects_runs_symlink_outside_requested_root(self) -> None:
        """Following the runs directory would let a record escape its root."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "root"
            outside = Path(temporary_directory) / "outside"
            (root / ".research").mkdir(parents=True)
            outside.mkdir()
            (root / ".research/runs").symlink_to(
                outside, target_is_directory=True
            )

            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    main([
                        "--root", str(root),
                        "--run-id", "r1",
                        "--experiment-id", "e1",
                        "--status", "planned",
                        "--environment-id", "local",
                        "--command", "python train.py",
                        "--started-at", "2026-07-29T00:00:00Z",
                    ])

            self.assertEqual(list(outside.iterdir()), [])

    def test_upsert_rejects_linked_research_parent_before_creating_runs(self) -> None:
        """Direct API use must not create runs through a linked .research parent."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "root"
            outside = base / "outside"
            outside_runs = outside / "runs"
            root.mkdir()
            outside_runs.mkdir(parents=True)
            (root / ".research").symlink_to(
                outside, target_is_directory=True
            )

            with self.assertRaises(ValueError):
                upsert_run(root / ".research/runs/r1.json", {
                    "run_id": "r1",
                    "experiment_id": "e1",
                    "status": "planned",
                    "environment_id": "local",
                    "command": "python train.py",
                    "started_at": "2026-07-29T00:00:00Z",
                })

            self.assertFalse((outside_runs / "r1.json").exists())

    def test_upsert_rejects_dotdot_components_before_path_traversal(self) -> None:
        """Normalizing a supplied parent must not erase traversal components."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            runs = root / ".research/runs"
            runs.mkdir(parents=True)
            path = runs / ".." / "runs" / "r1.json"

            with self.assertRaises(ValueError):
                upsert_run(path, {
                    "run_id": "r1",
                    "experiment_id": "e1",
                    "status": "planned",
                    "environment_id": "local",
                    "command": "python train.py",
                    "started_at": "2026-07-29T00:00:00Z",
                })

            self.assertFalse((runs / "r1.json").exists())

    def test_upsert_rejects_dotdot_escape_before_following_research_link(self) -> None:
        """Traversal syntax must not bypass the anchored .research walk."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "root"
            outside = base / "outside"
            outside_runs = outside / "runs"
            root.mkdir()
            outside_runs.mkdir(parents=True)
            (root / ".research").symlink_to(
                outside, target_is_directory=True
            )
            path = root / ".research/runs/../runs/r1.json"

            with self.assertRaises(ValueError):
                upsert_run(path, {
                    "run_id": "r1",
                    "experiment_id": "e1",
                    "status": "planned",
                    "environment_id": "local",
                    "command": "python train.py",
                    "started_at": "2026-07-29T00:00:00Z",
                })

            self.assertFalse((outside_runs / "r1.json").exists())

    def test_upsert_rejects_intermediate_symlink_after_research_anchor(self) -> None:
        """Every supplied parent below .research must be opened without follow."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "root"
            research = root / ".research"
            outside = base / "outside"
            outside_nested = outside / "nested"
            research.mkdir(parents=True)
            outside_nested.mkdir(parents=True)
            (research / "linked").symlink_to(
                outside, target_is_directory=True
            )

            with self.assertRaises(ValueError):
                upsert_run(research / "linked/nested/r1.json", {
                    "run_id": "r1",
                    "experiment_id": "e1",
                    "status": "planned",
                    "environment_id": "local",
                    "command": "python train.py",
                    "started_at": "2026-07-29T00:00:00Z",
                })

            self.assertFalse((outside_nested / "r1.json").exists())

    def test_upsert_accepts_normal_anchored_research_path(self) -> None:
        """A normalized .research path must retain ordinary direct-API behavior."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            path = root / ".research/runs/r1.json"

            result = upsert_run(path, {
                "run_id": "r1",
                "experiment_id": "e1",
                "status": "planned",
                "environment_id": "local",
                "command": "python train.py",
                "started_at": "2026-07-29T00:00:00Z",
            })

            self.assertEqual(result["run_id"], "r1")
            self.assertTrue(path.is_file())

    def test_upsert_fails_closed_when_secure_primitives_are_unavailable(
        self,
    ) -> None:
        """Missing no-follow primitives must fail before creating a record."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            path = root / ".research/runs/r1.json"

            with mock.patch.object(
                record_module,
                "_secure_operations_supported",
                return_value=False,
                create=True,
            ):
                with self.assertRaisesRegex(RuntimeError, "secure file operations"):
                    upsert_run(path, {
                        "run_id": "r1",
                        "experiment_id": "e1",
                        "status": "planned",
                        "environment_id": "local",
                        "command": "python train.py",
                        "started_at": "2026-07-29T00:00:00Z",
                    })

            self.assertFalse((root / ".research").exists())

    def test_cli_rejects_linked_record_before_reading_external_json(self) -> None:
        """A final record link must not expose or replace external JSON content."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "root"
            runs = root / ".research/runs"
            outside = base / "outside"
            runs.mkdir(parents=True)
            outside.mkdir()
            external = outside / "record.json"
            secret = "secret_token=do-not-print"
            original = json.dumps({
                "run_id": "r1",
                "experiment_id": "e1",
                "status": "planned",
                "environment_id": "local",
                "command": "python train.py",
                "started_at": "2026-07-29T00:00:00Z",
                "secret_token": secret,
            })
            external.write_text(original)
            (runs / "r1.json").symlink_to(external)
            stdout = io.StringIO()
            stderr = io.StringIO()

            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                with self.assertRaises(SystemExit):
                    main([
                        "--root", str(root),
                        "--run-id", "r1",
                        "--experiment-id", "e1",
                        "--status", "completed",
                        "--environment-id", "local",
                        "--command", "python train.py",
                        "--started-at", "2026-07-29T01:00:00Z",
                    ])

            self.assertEqual(external.read_text(), original)
            self.assertNotIn(secret, stdout.getvalue() + stderr.getvalue())

    def test_cli_rejects_dangling_record_symlink(self) -> None:
        """A dangling final link must not be mistaken for a new record path."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "root"
            runs = root / ".research/runs"
            outside = base / "outside"
            runs.mkdir(parents=True)
            outside.mkdir()
            external = outside / "new-record.json"
            record = runs / "r1.json"
            record.symlink_to(external)

            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                io.StringIO()
            ):
                with self.assertRaises(SystemExit):
                    main([
                        "--root", str(root),
                        "--run-id", "r1",
                        "--experiment-id", "e1",
                        "--status", "planned",
                        "--environment-id", "local",
                        "--command", "python train.py",
                        "--started-at", "2026-07-29T00:00:00Z",
                    ])

            self.assertTrue(record.is_symlink())
            self.assertFalse(external.exists())

    def test_upsert_removes_partial_temp_file_after_serialization_failure(self) -> None:
        """A serialization error must not leave a hidden partial record behind."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "r1.json"
            original = json.dumps({
                "run_id": "r1",
                "experiment_id": "e1",
                "status": "planned",
                "environment_id": "local",
                "command": "python train.py",
                "started_at": "2026-07-29T00:00:00Z",
            })
            path.write_text(original)

            with self.assertRaises(TypeError):
                upsert_run(path, {"custom": {"not", "json"}})

            self.assertEqual(path.read_text(), original)
            self.assertEqual(list(path.parent.glob(".r1.json.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
