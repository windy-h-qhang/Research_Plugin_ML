import copy
import unittest

from scripts.summarize_evidence import render_markdown, summarize


class SummarizeEvidenceTests(unittest.TestCase):
    def test_smoke_run_does_not_support_research_conclusion(self) -> None:
        """Treating a smoke pass as science would overstate its evidence."""
        summary = summarize([{
            "run_id": "smoke-1",
            "status": "completed",
            "validation_level": "smoke",
        }], [])

        self.assertEqual(summary["code_verification"], "verified")
        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")

    def test_negative_valid_experiment_is_not_code_failure(self) -> None:
        """Conflating a valid negative result with code failure loses evidence."""
        summary = summarize([{
            "run_id": "exp-1",
            "status": "completed",
            "validation_level": "conclusion",
            "conclusion": "not_supported",
        }], ["Scientific verdict: valid negative result"])

        self.assertEqual(summary["experiment_execution"], "verified")
        self.assertEqual(summary["conclusion_support"], "failed")

    def test_render_names_all_three_states(self) -> None:
        """Omitting a state from the report would hide an evidence dimension."""
        text = render_markdown({
            "code_verification": "verified",
            "experiment_execution": "inconclusive",
            "conclusion_support": "not_verified",
            "missing_evidence": ["three additional seeds"],
            "remaining_risks": ["single-machine evidence may not generalize"],
        })

        self.assertIn("Code verification", text)
        self.assertIn("Experiment execution", text)
        self.assertIn("Conclusion support", text)
        self.assertIn("## Missing evidence\n- three additional seeds", text)
        self.assertIn(
            "## Remaining risks\n- single-machine evidence may not generalize",
            text,
        )

    def test_completed_supported_seed_cannot_hide_failed_required_seed(
        self,
    ) -> None:
        """Selecting a favorable completed seed would hide a required failure."""
        summary = summarize([
            {
                "run_id": "seed-1",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "seed-2",
                "status": "failed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
        ], [], required_run_ids=["seed-1", "seed-2"])

        self.assertEqual(summary["code_verification"], "inconclusive")
        self.assertEqual(summary["experiment_execution"], "failed")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertEqual(
            summary["missing_evidence"],
            ["required run 'seed-2' failed with status 'failed'"],
        )
        self.assertEqual(
            summary["remaining_risks"],
            ["Required evidence is incomplete; the conclusion cannot be verified."],
        )

    def test_completed_conclusion_without_verdict_is_inconclusive(self) -> None:
        """A completed run without a scientific outcome cannot support a conclusion."""
        review = "Scientific review pending metric interpretation"
        summary = summarize([{
            "run_id": "exp-2",
            "status": "completed",
            "validation_level": "conclusion",
        }], [review])

        self.assertEqual(summary["code_verification"], "verified")
        self.assertEqual(summary["experiment_execution"], "verified")
        self.assertEqual(summary["conclusion_support"], "inconclusive")
        self.assertEqual(summary["reviews"], [review])

    def test_completed_smoke_and_failed_regression_make_code_inconclusive(
        self,
    ) -> None:
        """A smoke pass must not hide failure in the same required code evidence."""
        summary = summarize([
            {
                "run_id": "smoke-1",
                "status": "completed",
                "validation_level": "smoke",
            },
            {
                "run_id": "regression-1",
                "status": "failed",
                "validation_level": "regression",
            },
        ], [])

        self.assertEqual(summary["code_verification"], "inconclusive")
        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")

    def test_running_and_missing_required_seeds_are_exactly_reported(self) -> None:
        """Unidentified omissions make an evidence contract unauditable."""
        summary = summarize([
            {
                "run_id": "seed-1",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "seed-2",
                "status": "running",
                "validation_level": "conclusion",
            },
        ], [], required_run_ids=["seed-1", "seed-2", "seed-3"])

        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertEqual(summary["missing_evidence"], [
            "required run 'seed-2' is incomplete with status 'running'",
            "required run 'seed-3' is missing",
        ])

    def test_all_required_completed_positive_runs_verify_conclusion(self) -> None:
        """Requiring completion of every declared run prevents seed selection."""
        summary = summarize([
            {
                "run_id": "seed-1",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "seed-2",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
        ], [], required_run_ids={"seed-1", "seed-2"})

        self.assertEqual(summary["code_verification"], "verified")
        self.assertEqual(summary["experiment_execution"], "verified")
        self.assertEqual(summary["conclusion_support"], "verified")
        self.assertEqual(summary["missing_evidence"], [])
        self.assertEqual(summary["remaining_risks"], [])

    def test_required_contract_does_not_scope_independent_code_evidence(
        self,
    ) -> None:
        """A required conclusion contract must not hide unrelated code failures."""
        runs = [
            {
                "run_id": "seed-1",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "smoke-failed",
                "status": "failed",
                "validation_level": "smoke",
            },
        ]
        reviews = ["review retained"]
        required_run_ids = ["seed-1"]
        original_runs = copy.deepcopy(runs)
        original_reviews = list(reviews)
        original_required_run_ids = list(required_run_ids)

        summary = summarize(
            runs,
            reviews,
            required_run_ids=required_run_ids,
        )

        self.assertEqual(summary["code_verification"], "inconclusive")
        self.assertEqual(summary["experiment_execution"], "verified")
        self.assertEqual(summary["conclusion_support"], "verified")
        self.assertEqual(runs, original_runs)
        self.assertEqual(reviews, original_reviews)
        self.assertEqual(required_run_ids, original_required_run_ids)

    def test_missing_required_seed_does_not_erase_completed_code_evidence(
        self,
    ) -> None:
        """Experiment omissions must not downgrade independent deterministic checks."""
        summary = summarize([
            {
                "run_id": "unit-1",
                "status": "completed",
                "validation_level": "deterministic",
            },
        ], [], required_run_ids=["seed-missing"])

        self.assertEqual(summary["code_verification"], "verified")
        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")

    def test_required_run_must_appear_exactly_once(self) -> None:
        """Duplicate records must not satisfy a one-run evidence obligation."""
        duplicate = {
            "run_id": "seed-1",
            "status": "completed",
            "validation_level": "conclusion",
            "conclusion": "supported",
        }
        summary = summarize(
            [dict(duplicate), dict(duplicate)],
            [],
            required_run_ids=["seed-1"],
        )

        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertEqual(
            summary["missing_evidence"],
            ["required run 'seed-1' appears 2 times"],
        )

    def test_duplicate_ids_in_required_contract_are_rejected(self) -> None:
        """Silently deduplicating obligations would accept an ambiguous contract."""
        runs = [{
            "run_id": "seed-1",
            "status": "completed",
            "validation_level": "conclusion",
            "conclusion": "supported",
        }]

        with self.assertRaisesRegex(
            ValueError,
            "required_run_ids contains duplicate ID: seed-1",
        ):
            summarize(runs, [], required_run_ids=["seed-1", "seed-1"])

    def test_conflicting_completed_outcomes_are_inconclusive(self) -> None:
        """Selecting either side of completed conflicting evidence would overstate it."""
        summary = summarize([
            {
                "run_id": "exp-supported",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "exp-not-supported",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "not_supported",
            },
        ], [])

        self.assertEqual(summary["conclusion_support"], "inconclusive")

    def test_inferred_failed_attempt_prevents_completed_negative_execution(
        self,
    ) -> None:
        """All supplied conclusion attempts belong to the inferred contract."""
        summary = summarize([
            {
                "run_id": "failed-supported",
                "status": "failed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "completed-negative",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "not_supported",
            },
        ], [])

        self.assertEqual(summary["code_verification"], "inconclusive")
        self.assertEqual(summary["experiment_execution"], "failed")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertEqual(
            summary["missing_evidence"],
            ["required run 'failed-supported' failed with status 'failed'"],
        )

    def test_inferred_failed_attempt_prevents_completed_positive_support(
        self,
    ) -> None:
        """A favorable completed attempt cannot be selected from failed attempts."""
        summary = summarize([
            {
                "run_id": "failed-negative",
                "status": "failed",
                "validation_level": "conclusion",
                "conclusion": "not_supported",
            },
            {
                "run_id": "completed-supported",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
        ], [])

        self.assertEqual(summary["code_verification"], "inconclusive")
        self.assertEqual(summary["experiment_execution"], "failed")
        self.assertEqual(summary["conclusion_support"], "not_verified")

    def test_failed_required_code_validation_without_completion_is_failed(
        self,
    ) -> None:
        """A failed required validation is evidence of failure, not absence."""
        summary = summarize([
            {
                "run_id": "regression-1",
                "status": "failed",
                "validation_level": "regression",
            },
        ], [])

        self.assertEqual(summary["code_verification"], "failed")

    def test_cancelled_required_experiment_is_failed_execution(self) -> None:
        """Cancellation is a failed required execution, not missing evidence."""
        summary = summarize([
            {
                "run_id": "seed-cancelled",
                "status": "cancelled",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
        ], [], required_run_ids=["seed-cancelled"])

        self.assertEqual(summary["code_verification"], "failed")
        self.assertEqual(summary["experiment_execution"], "failed")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertEqual(
            summary["missing_evidence"],
            ["required run 'seed-cancelled' failed with status 'cancelled'"],
        )

    def test_required_ids_cannot_hide_unlisted_conflicting_conclusion(
        self,
    ) -> None:
        """Explicit obligations may add evidence, never select favorable evidence."""
        summary = summarize([
            {
                "run_id": "selected-positive",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "unlisted-negative",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "not_supported",
            },
        ], [], required_run_ids=["selected-positive"])

        self.assertEqual(summary["experiment_execution"], "verified")
        self.assertEqual(summary["conclusion_support"], "inconclusive")

    def test_required_ids_cannot_hide_unlisted_failed_conclusion(self) -> None:
        """A supplied failed conclusion attempt remains execution evidence."""
        summary = summarize([
            {
                "run_id": "selected-positive",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            {
                "run_id": "unlisted-failed",
                "status": "failed",
                "validation_level": "conclusion",
            },
        ], [], required_run_ids=["selected-positive"])

        self.assertEqual(summary["experiment_execution"], "failed")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertIn(
            "supplied conclusion run 'unlisted-failed' failed with status "
            "'failed'",
            summary["missing_evidence"],
        )

    def test_required_ids_do_not_promote_unlisted_incomplete_conclusion(
        self,
    ) -> None:
        """Running or unknown supplied attempts prevent verified execution."""
        for status in ("running", "unknown"):
            with self.subTest(status=status):
                summary = summarize([
                    {
                        "run_id": "selected-positive",
                        "status": "completed",
                        "validation_level": "conclusion",
                        "conclusion": "supported",
                    },
                    {
                        "run_id": f"unlisted-{status}",
                        "status": status,
                        "validation_level": "conclusion",
                    },
                ], [], required_run_ids=["selected-positive"])

                self.assertEqual(
                    summary["experiment_execution"],
                    "not_verified",
                )
                self.assertEqual(
                    summary["conclusion_support"],
                    "not_verified",
                )

    def test_required_ids_cannot_hide_unlisted_duplicate_conclusion(self) -> None:
        """An explicit subset must not make duplicate supplied records valid."""
        unlisted = {
            "run_id": "unlisted-duplicate",
            "status": "completed",
            "validation_level": "conclusion",
            "conclusion": "supported",
        }
        summary = summarize([
            {
                "run_id": "selected-positive",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
            dict(unlisted),
            dict(unlisted),
        ], [], required_run_ids=["selected-positive"])

        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertIn(
            "supplied conclusion run 'unlisted-duplicate' appears 2 times",
            summary["missing_evidence"],
        )

    def test_required_ids_must_name_conclusion_level_runs(self) -> None:
        """A deterministic check cannot satisfy a scientific run contract."""
        summary = summarize([
            {
                "run_id": "required-unit",
                "status": "completed",
                "validation_level": "deterministic",
            },
            {
                "run_id": "unrelated-positive",
                "status": "completed",
                "validation_level": "conclusion",
                "conclusion": "supported",
            },
        ], [], required_run_ids=["required-unit"])

        self.assertEqual(summary["experiment_execution"], "not_verified")
        self.assertEqual(summary["conclusion_support"], "not_verified")
        self.assertIn(
            "required run 'required-unit' is not conclusion-level",
            summary["missing_evidence"],
        )


if __name__ == "__main__":
    unittest.main()
