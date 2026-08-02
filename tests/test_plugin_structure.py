import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = (
    "using-research-workflows",
    "framing-research-work",
    "designing-research-experiments",
    "planning-research-changes",
    "validating-research-code",
    "debugging-research-runs",
    "orchestrating-research-agents",
    "verifying-research-evidence",
    "applying-ml-research-profile",
    "applying-llm-research-profile",
    "applying-ai-infra-profile",
)


class PluginStructureTests(unittest.TestCase):
    def test_manifest_identity_and_skills_path(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], "research-engineering")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(
            manifest["author"]["name"], "Research Engineering Contributors"
        )
        self.assertEqual(manifest["interface"]["displayName"], "Research Engineering")

        claude_manifest = json.loads(
            (ROOT / ".claude-plugin/plugin.json").read_text()
        )
        self.assertEqual(claude_manifest["name"], manifest["name"])
        self.assertEqual(claude_manifest["version"], manifest["version"])
        self.assertEqual(claude_manifest["license"], manifest["license"])
        self.assertEqual(
            claude_manifest["author"]["name"], manifest["author"]["name"]
        )

    def test_expected_skill_names_are_unique(self) -> None:
        self.assertEqual(len(EXPECTED_SKILLS), 11)
        self.assertEqual(len(EXPECTED_SKILLS), len(set(EXPECTED_SKILLS)))


if __name__ == "__main__":
    unittest.main()
