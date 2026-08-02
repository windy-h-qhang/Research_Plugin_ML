import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageExportTests(unittest.TestCase):
    def test_git_archive_excludes_internal_reports_and_keeps_plugin(self) -> None:
        """The source package must not publish internal SDD control records."""
        attributes = ROOT / ".gitattributes"
        self.assertTrue(attributes.is_file())
        self.assertIn(
            ".superpowers export-ignore",
            attributes.read_text().splitlines(),
        )
        self.assertIn(
            "docs/superpowers export-ignore",
            attributes.read_text().splitlines(),
        )

        tracked_representatives = {
            ".codex-plugin/plugin.json": "{}\n",
            "README.md": "# plugin\n",
            "skills/demo/SKILL.md": "# skill\n",
            "scripts/demo.py": "pass\n",
            "tests/test_demo.py": "pass\n",
            "examples/minimal-project/README.md": "# example\n",
            ".superpowers/sdd/private-report.md": "internal\n",
            "docs/superpowers/plans/internal.md": "/Users/alice/private\n",
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository = Path(temporary_directory) / "repository"
            repository.mkdir()
            (repository / ".gitattributes").write_text(
                attributes.read_text()
            )
            for relative_path, contents in tracked_representatives.items():
                path = repository / relative_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(contents)

            commands = [
                ["git", "init", "-q"],
                ["git", "add", "-f", "."],
                [
                    "git",
                    "-c",
                    "user.name=Package Test",
                    "-c",
                    "user.email=package-test@example.invalid",
                    "commit",
                    "-qm",
                    "fixture",
                ],
            ]
            for command in commands:
                subprocess.run(command, cwd=repository, check=True)
            tracked = subprocess.run(
                ["git", "ls-files"],
                cwd=repository,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            self.assertIn(
                ".superpowers/sdd/private-report.md",
                tracked,
            )

            archive = repository / "plugin.tar"
            with archive.open("wb") as destination:
                subprocess.run(
                    ["git", "archive", "--format=tar", "HEAD"],
                    cwd=repository,
                    check=True,
                    stdout=destination,
                )
            with tarfile.open(archive) as package:
                names = set(package.getnames())

        for expected_path in tracked_representatives:
            if expected_path.startswith((".superpowers/", "docs/superpowers/")):
                self.assertNotIn(expected_path, names)
            else:
                self.assertIn(expected_path, names)


if __name__ == "__main__":
    unittest.main()
