import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import scripts.init_research_state as init_module
from scripts.init_research_state import initialize

ROOT = Path(__file__).resolve().parents[1]


class InitResearchStateTests(unittest.TestCase):
    def test_initialize_creates_expected_tree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            created = initialize(root, ROOT / "templates")
            self.assertIn(root / ".research/context.md", created)
            self.assertTrue((root / ".research/experiments").is_dir())
            self.assertTrue((root / ".research/runs").is_dir())
            self.assertTrue((root / ".research/reviews").is_dir())
            self.assertTrue((root / ".research/local").is_dir())
            self.assertIn("local/", (root / ".research/.gitignore").read_text())

    def test_initialize_preserves_existing_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / ".research/context.md"
            target.parent.mkdir(parents=True)
            target.write_text("user content\n")
            initialize(root, ROOT / "templates")
            self.assertEqual(target.read_text(), "user content\n")

    def test_initialize_is_idempotent(self) -> None:
        """Reinitializing must preserve every existing research-state file."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            initialize(root, ROOT / "templates")
            context = root / ".research/context.md"
            context.write_text("project-specific context\n")

            initialize(root, ROOT / "templates")

            self.assertEqual(context.read_text(), "project-specific context\n")
            self.assertTrue((root / ".research/runs").is_dir())

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            planned = initialize(root, ROOT / "templates", dry_run=True)
            self.assertGreater(len(planned), 0)
            self.assertFalse((root / ".research").exists())

    def test_cli_rejects_research_symlink_without_external_writes_or_leaks(self) -> None:
        """Following .research would let initialization escape the requested root."""
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "root"
            outside = base / "outside-secret-token"
            root.mkdir()
            outside.mkdir()
            marker = outside / "marker"
            marker.write_text("unchanged\n")
            (root / ".research").symlink_to(outside, target_is_directory=True)

            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/init_research_state.py"),
                    "--root",
                    str(root),
                ],
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "unchanged\n")
            self.assertEqual(sorted(path.name for path in outside.iterdir()), ["marker"])
            self.assertNotIn("outside-secret-token", result.stdout + result.stderr)

    def test_initialize_rejects_symlink_directory_destination(self) -> None:
        """A linked child directory must not be accepted as initialized state."""
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "root"
            outside = base / "outside"
            research = root / ".research"
            research.mkdir(parents=True)
            outside.mkdir()
            marker = outside / "marker"
            marker.write_text("unchanged\n")
            (research / "runs").symlink_to(outside, target_is_directory=True)

            with self.assertRaises(ValueError):
                initialize(root, ROOT / "templates")

            self.assertEqual(marker.read_text(), "unchanged\n")
            self.assertEqual(sorted(path.name for path in outside.iterdir()), ["marker"])

    def test_initialize_rejects_file_destination_symlinks(self) -> None:
        """Existing and dangling file links must never be preserved or followed."""
        for dangling in (False, True):
            with self.subTest(dangling=dangling):
                with tempfile.TemporaryDirectory() as tmp:
                    base = Path(tmp)
                    root = base / "root"
                    outside = base / "outside"
                    research = root / ".research"
                    research.mkdir(parents=True)
                    outside.mkdir()
                    target = outside / "external-context"
                    if not dangling:
                        target.write_text("secret_token=unchanged\n")
                    (research / "context.md").symlink_to(target)

                    with self.assertRaises(ValueError):
                        initialize(root, ROOT / "templates")

                    if dangling:
                        self.assertFalse(target.exists())
                    else:
                        self.assertEqual(
                            target.read_text(), "secret_token=unchanged\n"
                        )

    def test_initialize_missing_source_leaves_no_destination_and_can_retry(self) -> None:
        """A source-open failure must not leave an empty file that blocks retry."""
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "root"
            templates = base / "templates"
            root.mkdir()
            shutil.copytree(ROOT / "templates", templates)
            expected = (templates / "context.md").read_text()
            (templates / "context.md").unlink()
            destination = root / ".research/context.md"

            with self.assertRaises(ValueError):
                initialize(root, templates)

            self.assertFalse(destination.exists())
            self.assertEqual(list(destination.parent.glob(".context.md.*.tmp")), [])

            (templates / "context.md").write_text(expected)
            initialize(root, templates)

            self.assertEqual(destination.read_text(), expected)

    def test_initialize_mid_copy_failure_leaves_no_partial_file_and_can_retry(
        self,
    ) -> None:
        """A failed copy must publish neither partial content nor a temp file."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            destination = root / ".research/context.md"
            expected = (ROOT / "templates/context.md").read_text()

            def fail_mid_copy(source: object, target: object) -> None:
                target.write(source.read(8))  # type: ignore[attr-defined]
                raise OSError("simulated copy failure")

            with mock.patch.object(
                init_module.shutil,
                "copyfileobj",
                side_effect=fail_mid_copy,
            ):
                with self.assertRaises(ValueError):
                    initialize(root, ROOT / "templates")

            self.assertFalse(destination.exists())
            self.assertEqual(list(destination.parent.glob(".context.md.*.tmp")), [])

            initialize(root, ROOT / "templates")

            self.assertEqual(destination.read_text(), expected)

    def test_initialize_fails_closed_when_secure_primitives_are_unavailable(
        self,
    ) -> None:
        """Missing no-follow primitives must fail before creating state."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(
                init_module,
                "_secure_operations_supported",
                return_value=False,
                create=True,
            ):
                with self.assertRaisesRegex(RuntimeError, "secure file operations"):
                    initialize(root, ROOT / "templates")

            self.assertFalse((root / ".research").exists())
