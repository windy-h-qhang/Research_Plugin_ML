import tempfile
import unittest
from pathlib import Path

from tests.skill_assertions import validate_skill


class SkillAssertionTests(unittest.TestCase):
    def write_skill(self, directory: str, content: str) -> Path:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        path = Path(temporary_directory.name) / directory / "SKILL.md"
        path.parent.mkdir()
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_skill_has_no_errors(self) -> None:
        path = self.write_skill(
            "validating-example",
            "---\n"
            "name: validating-example\n"
            "description: Use when an example requires validation\n"
            "---\n\n"
            "# Validating Example\n\nApply the validation contract.\n",
        )

        self.assertEqual(validate_skill(path), [])

    def test_valid_skill_accepts_quoted_frontmatter_scalars(self) -> None:
        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: 'quoted-values'\n"
            'description: "Use when checking quoted scalars"\n'
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(validate_skill(path), [])

    def test_malformed_single_quoted_scalar_is_rejected(self) -> None:
        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: quoted-values\n"
            "description: 'Use when user's request'\n"
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(
            validate_skill(path),
            ['description must start with "Use when"'],
        )

    def test_unbalanced_single_quoted_scalar_is_rejected(self) -> None:
        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: quoted-values\n"
            "description: 'Use when checking quote balance\n"
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(
            validate_skill(path),
            ['description must start with "Use when"'],
        )

    def test_malformed_or_unbalanced_double_quoted_scalar_is_rejected(self) -> None:
        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: quoted-values\n"
            'description: "Use when checking quote balance\n'
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(
            validate_skill(path),
            ['description must start with "Use when"'],
        )

        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: quoted-values\n"
            'description: "Use when checking an invalid \\q escape"\n'
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(
            validate_skill(path),
            ['description must start with "Use when"'],
        )

    def test_valid_doubled_single_quote_scalar_is_accepted(self) -> None:
        path = self.write_skill(
            "quoted-values",
            "---\n"
            "name: quoted-values\n"
            "description: 'Use when checking a researcher''s scalar'\n"
            "---\n\n"
            "# Quoted Values\n",
        )

        self.assertEqual(validate_skill(path), [])

    def test_missing_skill_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing" / "SKILL.md"

            self.assertEqual(validate_skill(path), ["skill file does not exist"])

    def test_frontmatter_must_have_opening_and_closing_delimiters(self) -> None:
        path = self.write_skill("bad", "name: bad\ndescription: Use when testing\n")

        self.assertEqual(validate_skill(path), ["missing opening frontmatter delimiter"])

        path.write_text("---\nname: bad\ndescription: Use when testing\n", encoding="utf-8")

        self.assertEqual(validate_skill(path), ["missing closing frontmatter delimiter"])

    def test_name_and_description_must_each_appear_once(self) -> None:
        path = self.write_skill(
            "bad",
            "---\n"
            "name: bad\n"
            "name: duplicate\n"
            "---\n"
            "Body.\n",
        )

        self.assertEqual(
            validate_skill(path),
            [
                'frontmatter must contain exactly one "name" field',
                'frontmatter must contain exactly one "description" field',
            ],
        )

    def test_name_must_be_kebab_case_and_match_its_directory(self) -> None:
        path = self.write_skill(
            "different-directory",
            "---\n"
            "name: Bad_Name\n"
            "description: Use when testing names\n"
            "---\n"
            "Body.\n",
        )

        self.assertEqual(
            validate_skill(path),
            [
                "skill name must use kebab-case",
                "skill directory name must match the skill name",
            ],
        )

    def test_description_must_start_with_use_when(self) -> None:
        path = self.write_skill(
            "bad",
            "---\nname: bad\ndescription: Helpful rules\n---\nBody.\n",
        )

        self.assertEqual(
            validate_skill(path),
            ['description must start with "Use when"'],
        )

    def test_skill_body_must_not_be_empty(self) -> None:
        path = self.write_skill(
            "empty-body",
            "---\n"
            "name: empty-body\n"
            "description: Use when testing empty bodies\n"
            "---\n\n \t\n",
        )

        self.assertEqual(validate_skill(path), ["skill body must not be empty"])
