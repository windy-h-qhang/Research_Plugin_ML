import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "tests" / "behavior" / "results"
EXPECTED_FINAL_REPETITIONS = {
    "applying-ai-infra-profile-skilled.md": 10,
    "applying-llm-research-profile-skilled.md": 10,
    "applying-ml-research-profile-skilled.md": 10,
    "debugging-research-runs-skilled.md": 5,
    "designing-research-experiments-skilled.md": 5,
    "framing-research-work-skilled.md": 5,
    "orchestrating-research-agents-skilled.md": 5,
    "planning-research-changes-skilled.md": 5,
    "using-research-workflows-skilled.md": 5,
    "validating-research-code-skilled.md": 5,
    "verifying-research-evidence-skilled.md": 5,
}
EQUIVALENT_ARM_CONTEXT = {
    "framing-research-work-skilled.md": {
        "heading": "## Final REFACTOR arm",
        "case_file": ROOT / "tests" / "behavior" / "cases"
        / "framing-research-work.md",
        "markers": ("same isolation", "exact case prompt"),
    },
    "orchestrating-research-agents-skilled.md": {
        "heading": "## Final user-priority gate after override fix",
        "case_file": ROOT / "tests" / "behavior" / "cases"
        / "orchestrating-research-agents.md",
        "markers": (
            "frozen final Skill",
            "fresh context",
            "explicit stop",
            "default fallback",
        ),
    },
}
RESPONSE_HEADING = re.compile(
    r"^#{3,4} (?:Observed response|Verbatim response)\s*$",
    re.MULTILINE,
)
REPETITION_HEADING = re.compile(
    r"^#{2,3} .*repetition \d+\s*$",
    re.IGNORECASE | re.MULTILINE,
)
RUBRIC_HEADING = re.compile(
    r"^#{3,4} (?:Rubric|Rubric evidence)\s*$",
    re.MULTILINE,
)
VERDICT_HEADING = re.compile(
    r"^#{3,4} Verdict\s*$",
    re.MULTILINE,
)
MARKDOWN_HEADING = re.compile(
    r"^#{1,6}(?:[ \t]+[^\n]*)?\s*$",
    re.MULTILINE,
)
INLINE_PASS_VERDICT = re.compile(
    r"^Verdict:\s*\*\*PASS\b",
    re.MULTILINE,
)
ARM_TERMINATOR = re.compile(
    r"^#{2,3} [^\n]*(?:aggregate|summary)[^\n]*$",
    re.IGNORECASE | re.MULTILINE,
)


def _synthetic_repetition(
    number: int,
    *,
    response: str = "auditable response",
    verdict: bool = True,
    equivalent: bool = False,
) -> str:
    response_heading = "Verbatim response" if equivalent else "Observed response"
    rubric_heading = "Rubric evidence" if equivalent else "Rubric"
    if not verdict:
        verdict_text = ""
    elif equivalent:
        verdict_text = "\nVerdict: **PASS — 1/1**.\n"
    else:
        verdict_text = "\n### Verdict\n\nPASS — 1/1.\n"
    case_context = (
        ""
        if equivalent
        else "\n### Case\n\nSynthetic case.\n\n### Context\n\n"
    )
    return (
        f"### Repetition {number}\n"
        f"{case_context}"
        f"Evaluator: `/root/synthetic/evaluator-{number}`\n\n"
        f"### {response_heading}\n\n"
        f"{response}\n\n"
        f"### {rubric_heading}\n\n"
        f"- PASS — synthetic rubric.\n"
        f"{verdict_text}"
    )


def _final_response_sections(path: Path) -> list[tuple[str, str, str]]:
    text = path.read_text()
    expected_count = EXPECTED_FINAL_REPETITIONS[path.name]
    repetition_matches = list(REPETITION_HEADING.finditer(text))
    if len(repetition_matches) < expected_count:
        raise AssertionError(
            f"{path.name}: expected at least {expected_count} repetitions, "
            f"found {len(repetition_matches)}"
        )

    selected = repetition_matches[-expected_count:]
    equivalent_context = EQUIVALENT_ARM_CONTEXT.get(path.name)
    if equivalent_context is not None:
        arm_heading = equivalent_context["heading"]
        arm_heading_pattern = re.compile(
            rf"^{re.escape(arm_heading)}\s*$",
            re.MULTILINE,
        )
        arm_heading_matches = list(
            arm_heading_pattern.finditer(text, 0, selected[0].start())
        )
        if not arm_heading_matches:
            raise AssertionError(
                f"{path.name}: selected final arm is missing heading "
                f"{arm_heading!r}"
            )
        arm_start = arm_heading_matches[-1].start()
        arm_preamble = text[arm_start : selected[0].start()]
        for marker in equivalent_context["markers"]:
            if marker.lower() not in arm_preamble.lower():
                raise AssertionError(
                    f"{path.name}: selected final-arm preamble is missing "
                    f"{marker!r}"
                )
        case_file = equivalent_context["case_file"]
        if not case_file.is_file():
            raise AssertionError(
                f"{path.name}: declared case metadata does not exist: "
                f"{case_file}"
            )

    sections = []
    repetition_ids = set()
    evaluator_ids = set()
    for index, repetition_match in enumerate(selected):
        next_repetition_start = (
            selected[index + 1].start()
            if index + 1 < len(selected)
            else len(text)
        )
        terminator_match = ARM_TERMINATOR.search(
            text,
            repetition_match.end(),
            next_repetition_start,
        )
        if terminator_match is not None and index + 1 < len(selected):
            raise AssertionError(
                f"{path.name}: selected repetitions cross an arm boundary "
                f"before {selected[index + 1].group(0).strip()}"
            )
        end = (
            terminator_match.start()
            if terminator_match is not None
            else next_repetition_start
        )
        section = text[repetition_match.start() : end]
        response_matches = list(RESPONSE_HEADING.finditer(section))
        if len(response_matches) != 1:
            raise AssertionError(
                f"{path.name} {repetition_match.group(0).strip()}: expected "
                f"exactly one response, found {len(response_matches)}"
            )
        response_match = response_matches[0]
        rubric_matches = list(RUBRIC_HEADING.finditer(section))
        if len(rubric_matches) != 1:
            raise AssertionError(
                f"{path.name} {repetition_match.group(0).strip()}: expected "
                f"exactly one rubric, found {len(rubric_matches)}"
            )
        rubric_match = rubric_matches[0]
        if rubric_match.start() <= response_match.end():
            raise AssertionError(
                f"{path.name} {repetition_match.group(0).strip()}: rubric "
                "must follow the response"
            )
        response = section[response_match.end() : rubric_match.start()]
        if not response.strip():
            raise AssertionError(
                f"{path.name} {repetition_match.group(0).strip()}: response "
                "is empty"
            )

        preamble = section[: response_match.start()]
        if equivalent_context is None:
            has_case = (
                re.search(
                    r"^#{3,4} Case\s*$",
                    preamble,
                    re.MULTILINE,
                )
                is not None
            )
            has_context = (
                re.search(
                    r"^#{3,4} Context\s*$",
                    preamble,
                    re.MULTILINE,
                )
                is not None
            )
            if not (has_case and has_context):
                raise AssertionError(
                    f"{path.name} {repetition_match.group(0).strip()}: "
                    "missing Case or Context"
                )

        repetition_id = repetition_match.group(0).strip()
        if repetition_id in repetition_ids:
            raise AssertionError(
                f"{path.name}: duplicate repetition identity: {repetition_id}"
            )
        repetition_ids.add(repetition_id)
        root_ids = re.findall(r"`(/root/[^`\n]+)`", preamble)
        if not root_ids:
            raise AssertionError(
                f"{path.name} {repetition_id}: missing evaluator identity"
            )
        evaluator_id = root_ids[-1].rstrip(".")
        if evaluator_id in evaluator_ids:
            raise AssertionError(
                f"{path.name}: duplicate evaluator identity: {evaluator_id}"
            )
        evaluator_ids.add(evaluator_id)

        verdict_region = section[rubric_match.end() :]
        response_heading = response_match.group(0)
        first_later_heading = MARKDOWN_HEADING.search(verdict_region)
        if "Verbatim response" in response_heading:
            inline_verdicts = list(
                INLINE_PASS_VERDICT.finditer(verdict_region)
            )
            if len(inline_verdicts) != 1:
                raise AssertionError(
                    f"{path.name} {repetition_id}: expected one inline PASS "
                    f"verdict, found {len(inline_verdicts)}"
                )
            if (
                first_later_heading is not None
                and first_later_heading.start() < inline_verdicts[0].start()
            ):
                raise AssertionError(
                    f"{path.name} {repetition_id}: heading "
                    f"{first_later_heading.group(0).strip()!r} appears before "
                    "the inline verdict"
                )
        else:
            if first_later_heading is None:
                raise AssertionError(
                    f"{path.name} {repetition_id}: missing Verdict heading"
                )
            if VERDICT_HEADING.fullmatch(
                first_later_heading.group(0)
            ) is None:
                raise AssertionError(
                    f"{path.name} {repetition_id}: first heading after the "
                    f"rubric is {first_later_heading.group(0).strip()!r}, "
                    "not Verdict"
                )
            next_heading = MARKDOWN_HEADING.search(
                verdict_region,
                first_later_heading.end(),
            )
            verdict_end = (
                next_heading.start()
                if next_heading is not None
                else len(verdict_region)
            )
            verdict_text = verdict_region[
                first_later_heading.end() : verdict_end
            ].lstrip()
            if re.match(r"PASS\b", verdict_text) is None:
                raise AssertionError(
                    f"{path.name} {repetition_id}: final verdict is not PASS"
                )

        sections.append(
            (
                repetition_id,
                preamble,
                section[response_match.end() :],
            )
        )
    return sections


class BehaviorEvidenceTests(unittest.TestCase):
    def test_evaluator_identities_are_unique_across_complete_result_files(
        self,
    ) -> None:
        """Misplaced transcript copies must not impersonate fresh repetitions."""
        pattern = re.compile(
            r"^Evaluator(?: identity)?:\s*`(/root/[^`\n]+)`",
            re.MULTILINE,
        )
        for path in sorted(RESULTS_DIR.glob("*-skilled.md")):
            identities = pattern.findall(path.read_text())
            duplicates = sorted({
                identity for identity in identities
                if identities.count(identity) > 1
            })
            self.assertEqual(duplicates, [], path.name)

    def test_router_skill_defines_complete_agent_policy_precedence(self) -> None:
        """Removing any policy tier would make Router output under-specified."""
        skill = (
            ROOT / "skills" / "using-research-workflows" / "SKILL.md"
        ).read_text()
        normalized = " ".join(skill.split())
        for rule in (
            "exploration=single",
            "experiment=reviewed",
            "engineering=reviewed",
            "release=multi-role",
            "high-risk cross-domain/multi-environment=multi-role",
            "explicit user Agent policy overrides",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, normalized)

    def test_observed_verdict_cannot_follow_unknown_scorecard_heading(self) -> None:
        text = "# Synthetic skilled results\n\n"
        text += "".join(_synthetic_repetition(i) for i in range(1, 5))
        text += _synthetic_repetition(5, verdict=False)
        text += "\n## Final scorecard\n\n### Verdict\n\nPASS — aggregate only.\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = (
                Path(temp_dir)
                / "debugging-research-runs-skilled.md"
            )
            path.write_text(text)
            with self.assertRaises(AssertionError):
                _final_response_sections(path)

    def test_verbatim_verdict_cannot_follow_unknown_results_heading(self) -> None:
        text = (
            "# Synthetic skilled results\n\n"
            "## Final gate after explicit-output Skill edits\n\n"
            "These responses used the frozen final Skill in fresh context.\n\n"
        )
        text += "".join(
            _synthetic_repetition(i, equivalent=True)
            for i in range(1, 5)
        )
        text += _synthetic_repetition(5, equivalent=True, verdict=False)
        text += "\n## Overall results\n\nVerdict: **PASS — aggregate only**.\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = (
                Path(temp_dir)
                / "orchestrating-research-agents-skilled.md"
            )
            path.write_text(text)
            with self.assertRaises(AssertionError):
                _final_response_sections(path)

    def test_last_repetition_cannot_borrow_pass_from_eof_aggregate(self) -> None:
        text = "# Synthetic skilled results\n\n"
        text += "".join(_synthetic_repetition(i) for i in range(1, 5))
        text += _synthetic_repetition(5, verdict=False)
        text += "\n## Aggregate verdict\n\nVerdict: PASS\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = (
                Path(temp_dir)
                / "debugging-research-runs-skilled.md"
            )
            path.write_text(text)
            with self.assertRaises(AssertionError):
                _final_response_sections(path)

    def test_repetition_cannot_borrow_pass_from_later_repetition(self) -> None:
        text = "# Synthetic skilled results\n\n"
        text += "".join(_synthetic_repetition(i) for i in range(1, 4))
        text += _synthetic_repetition(4, verdict=False)
        text += _synthetic_repetition(5)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = (
                Path(temp_dir)
                / "debugging-research-runs-skilled.md"
            )
            path.write_text(text)
            with self.assertRaises(AssertionError):
                _final_response_sections(path)

    def test_empty_observed_response_is_rejected(self) -> None:
        text = "# Synthetic skilled results\n\n"
        text += "".join(_synthetic_repetition(i) for i in range(1, 5))
        text += _synthetic_repetition(5, response="   ")
        with tempfile.TemporaryDirectory() as temp_dir:
            path = (
                Path(temp_dir)
                / "debugging-research-runs-skilled.md"
            )
            path.write_text(text)
            with self.assertRaises(AssertionError):
                _final_response_sections(path)

    def test_equivalent_context_must_belong_to_selected_final_arm(self) -> None:
        for filename, equivalent, final_heading in (
            (
                "framing-research-work-skilled.md",
                False,
                "## Final REFACTOR arm",
            ),
            (
                "orchestrating-research-agents-skilled.md",
                True,
                "## Final user-priority gate after override fix",
            ),
        ):
            with self.subTest(file=filename):
                text = (
                    "# Synthetic skilled results\n\n"
                    "## Old superseded arm\n\n"
                    "This old arm used the exact case prompt in fresh context.\n\n"
                    f"{final_heading}\n\n"
                    "No final-arm provenance is declared here.\n\n"
                )
                text += "".join(
                    _synthetic_repetition(i, equivalent=equivalent)
                    for i in range(1, 6)
                )
                with tempfile.TemporaryDirectory() as temp_dir:
                    path = Path(temp_dir) / filename
                    path.write_text(text)
                    with self.assertRaises(AssertionError):
                        _final_response_sections(path)

    def test_protocol_uses_one_file_per_arm_and_complete_repetitions(self) -> None:
        protocol = (ROOT / "tests" / "behavior" / "README.md").read_text()
        normalized = " ".join(protocol.split())
        self.assertNotIn("one result file per repetition", normalized)
        self.assertIn("one result file per case/Skill arm", normalized)
        self.assertIn(
            "Each fresh repetition must have one complete response section",
            normalized,
        )
        self.assertIn(
            "Observed response (or a documented equivalent)",
            normalized,
        )
        self.assertIn("failed, superseded, or excluded", normalized)

    def test_all_skilled_files_have_auditable_final_formal_arms(self) -> None:
        paths = sorted(RESULTS_DIR.glob("*-skilled.md"))
        self.assertEqual(
            {path.name for path in paths},
            set(EXPECTED_FINAL_REPETITIONS),
        )

        evaluator_ids = set()
        for path in paths:
            sections = _final_response_sections(path)
            expected_count = EXPECTED_FINAL_REPETITIONS[path.name]
            self.assertEqual(len(sections), expected_count, path.name)

            for repetition, preamble, _body in sections:
                with self.subTest(file=path.name, repetition=repetition):
                    root_ids = re.findall(r"`(/root/[^`\n]+)`", preamble)
                    evaluator_id = root_ids[-1].rstrip(".")
                    self.assertNotIn(
                        evaluator_id,
                        evaluator_ids,
                        f"duplicate evaluator identity: {evaluator_id}",
                    )
                    evaluator_ids.add(evaluator_id)

    def test_failed_superseded_and_excluded_history_is_retained(self) -> None:
        required_history = {
            "applying-ai-infra-profile-skilled.md": (
                "Iteration 1 — failed and superseded",
                "Excluded primary attempt",
            ),
            "applying-llm-research-profile-skilled.md": (
                "Iteration 1 — failed and superseded",
                "Iteration 2 — failed and superseded",
            ),
            "applying-ml-research-profile-skilled.md": (
                "Iteration 1: failed regression",
                "Iteration 3: superseded arm after scoring audit",
            ),
            "orchestrating-research-agents-skilled.md": (
                "retained in the regression history as a failed",
                "sample and replaced",
            ),
            "using-research-workflows-skilled.md": (
                "## Attempt 1",
                "superseded failed arm",
            ),
            "validating-research-code-skilled.md": (
                "initial skilled arm scored `43/45`",
                "failed two blocking",
            ),
            "verifying-research-evidence-skilled.md": (
                "was interrupted before it returned a response",
                "is excluded",
            ),
        }
        for filename, markers in required_history.items():
            text = (RESULTS_DIR / filename).read_text()
            for marker in markers:
                with self.subTest(file=filename, marker=marker):
                    self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
