import json
import re
import unittest
from pathlib import Path

from tests.skill_assertions import validate_skill
from tests.test_plugin_structure import EXPECTED_SKILLS

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXAMPLES_DIR = ROOT / "examples" / "minimal-project"


class IntegrationTests(unittest.TestCase):
    def test_skill_word_budgets_are_enforced(self) -> None:
        for skill_name in EXPECTED_SKILLS:
            body = (
                SKILLS_DIR / skill_name / "SKILL.md"
            ).read_text().split("---", 2)[2]
            limit = 200 if skill_name == "using-research-workflows" else 500
            self.assertLessEqual(
                len(body.split()), limit, f"{skill_name} exceeds {limit} words"
            )

    def test_runtime_contracts_cover_profiles_language_and_ssh_sync(self) -> None:
        router = (
            SKILLS_DIR / "using-research-workflows" / "SKILL.md"
        ).read_text()
        planner = (
            SKILLS_DIR / "planning-research-changes" / "SKILL.md"
        ).read_text()
        self.assertIn("Load every matching Profile Skill", router)
        self.assertIn("user's language", router)
        self.assertIn("existing project sync mechanism", planner)
        self.assertIn("confirm a method before any remote overwrite", planner)

    def test_planned_run_schema_does_not_require_execution_time(self) -> None:
        schema = json.loads((ROOT / "templates" / "run.schema.json").read_text())
        self.assertNotIn("started_at", schema["required"])
        self.assertIn("allOf", schema)

    def test_readme_documents_user_priority_for_agent_fallback(self) -> None:
        readme = (ROOT / "README.md").read_text()
        self.assertIn("用户显式要求停止", readme)
        self.assertIn("未指定降级偏好", readme)

    def test_all_manifest_skills_are_valid(self) -> None:
        self.assertEqual(len(EXPECTED_SKILLS), 11)
        for skill_name in EXPECTED_SKILLS:
            with self.subTest(skill=skill_name):
                skill_path = SKILLS_DIR / skill_name / "SKILL.md"
                errors = validate_skill(skill_path)
                self.assertEqual(
                    errors,
                    [],
                    f"Skill {skill_name} has validation errors: {errors}",
                )

    def test_example_run_is_a_planned_synthetic_record_not_execution_evidence(
        self,
    ) -> None:
        run_path = EXAMPLES_DIR / ".research" / "runs" / "demo-smoke.json"
        self.assertTrue(
            run_path.exists(), f"Expected run file at {run_path}"
        )
        data = json.loads(run_path.read_text())
        expected = {
            "run_id": "demo-smoke",
            "experiment_id": "demo-confidence-gate",
            "environment_id": "local-demo",
            "command": (
                "python train.py --config configs/demo.yaml "
                "--max-steps 20 --seed 7"
            ),
            "status": "planned",
            "validation_level": "smoke",
            "conclusion": "not_verified",
        }
        for field, value in expected.items():
            with self.subTest(field=field):
                self.assertEqual(data.get(field), value)
        for execution_fact in (
            "exit_code",
            "started_at",
            "finished_at",
            "environment",
        ):
            with self.subTest(execution_fact=execution_fact):
                self.assertNotIn(execution_fact, data)
        serialized = json.dumps(data).lower()
        self.assertNotIn("a100", serialized)
        self.assertNotIn("cuda", serialized)

    def test_local_connection_state_is_ignored(self) -> None:
        gitignore_path = EXAMPLES_DIR / ".research" / ".gitignore"
        self.assertTrue(
            gitignore_path.exists(), f"Expected .gitignore at {gitignore_path}"
        )
        contents = gitignore_path.read_text()
        self.assertIn(
            "local/",
            contents,
            ".research/.gitignore must exclude local/ directory",
        )

    def test_example_context_selects_the_ml_profile(self) -> None:
        context_path = EXAMPLES_DIR / ".research" / "context.md"
        context = context_path.read_text()
        self.assertIn("- mode: experiment", context)
        self.assertIn("- profiles: [ML]", context)
        self.assertIn("- resource: local-cpu", context)
        self.assertNotIn("- mode: exploration", context)

    def test_example_contract_uses_predeclared_confidence_boundaries(self) -> None:
        experiment_path = (
            EXAMPLES_DIR / ".research" / "experiments" / "demo.md"
        )
        experiment = experiment_path.read_text()
        self.assertNotIn("not significant at p<0.05", experiment)
        self.assertIn(
            "- Success rule: the 95% CI over paired seed-level precision "
            "deltas has a lower bound of at least 2pp, and the 95% CI over "
            "paired seed-level recall deltas has a lower bound of at least "
            "-1pp",
            experiment,
        )
        self.assertIn(
            "- Negative-result rule: the 95% CI over paired seed-level "
            "precision deltas has an upper bound below 2pp, or the 95% CI "
            "over paired seed-level recall deltas has an upper bound below "
            "-1pp",
            experiment,
        )
        self.assertIn(
            "- Inconclusive rule: neither the success nor negative-result "
            "rule is met, including when a 95% CI crosses a predeclared "
            "boundary or statistical power is insufficient",
            experiment,
        )

    def test_example_contract_uses_paired_multi_seed_comparisons(self) -> None:
        experiment_path = (
            EXAMPLES_DIR / ".research" / "experiments" / "demo.md"
        )
        experiment = experiment_path.read_text()
        self.assertIn("- Seeds: [7, 17, 29, 43, 71]", experiment)
        self.assertIn("- Repetitions: 5", experiment)
        self.assertIn(
            "- Comparison design: for each seed, run paired baseline and "
            "candidate arms with identical data order",
            experiment,
        )
        self.assertIn(
            "- Uncertainty unit: paired seed-level deltas",
            experiment,
        )
        self.assertNotIn(
            "- Controlled variables: [model-architecture, dataset, seed]",
            experiment,
        )

    def test_readme_uses_a_supported_local_marketplace_flow(self) -> None:
        readme = (ROOT / "README.md").read_text()
        self.assertNotIn(
            "unzip research-engineering-0.1.0.zip -d ~/.codex/plugins/",
            readme,
        )
        self.assertIn(
            "~/.agents/plugins/marketplace.json",
            readme,
        )
        self.assertIn('"name": "personal"', readme)
        self.assertIn('"path": "./plugins/research-engineering"', readme)
        self.assertIn(
            "codex plugin marketplace add /path/to/marketplace-root",
            readme,
        )
        self.assertIn(
            "codex plugin add research-engineering@personal",
            readme,
        )
        self.assertIn(
            "codex plugin remove research-engineering@personal",
            readme,
        )
        self.assertIn("不需要执行\n`codex plugin marketplace add`", readme)
        self.assertIn("$env:USERPROFILE\\.agents\\plugins\\marketplace.json", readme)
        self.assertIn("claude --plugin-dir .\\research-engineering", readme)
        self.assertIn("/research-engineering:using-research-workflows", readme)
        self.assertNotIn("/Users/", readme)
        self.assertNotIn("@gmail.com", readme)
        self.assertIn("新 task", readme)
        self.assertRegex(
            readme,
            r"卸载插件不会删除研究\s+项目中的 `\.research/`",
        )
        marketplace_match = re.search(
            r"`~/\.agents/plugins/marketplace\.json`"
            r" 的最小内容为：\n\n```json\n(.*?)\n```",
            readme,
            re.DOTALL,
        )
        self.assertIsNotNone(marketplace_match)
        marketplace = json.loads(marketplace_match.group(1))
        self.assertEqual(marketplace["name"], "personal")
        self.assertEqual(
            marketplace["plugins"][0]["source"],
            {
                "source": "local",
                "path": "./plugins/research-engineering",
            },
        )

    def test_readme_quick_start_matches_the_router_contract(self) -> None:
        readme = (ROOT / "README.md").read_text()
        expected_router = """\
- Mode: experiment
- Profiles: ML
- Environment: local
- Cost gate: auto-approved
- Reason: confidence-gate formal comparison→experiment; classifier quality→ML; explicit local CPU→local; bounded no-paid 20-step Smoke Test→auto-approved
- Agent policy: reviewed
- Override: user may override classification/workflow mode; platform safety remains binding
- Next Skill: framing-research-work→designing-research-experiments"""
        self.assertIn(expected_router, readme)
        self.assertIn("用户指令始终覆盖自动判断", readme)
        self.assertIn("不能取消平台安全边界", readme)

    def test_example_review_discloses_that_no_training_was_executed(self) -> None:
        review_path = (
            EXAMPLES_DIR / ".research" / "reviews" / "demo-scientific.md"
        )
        review = review_path.read_text()
        self.assertNotIn("- Verdict: PASS", review)
        self.assertNotIn("- Verdict: INCONCLUSIVE", review)
        self.assertIn("- Verdict: NEEDS_FIXES", review)
        self.assertIn(
            "- Evidence: [synthetic planned record only; no run was executed]",
            review,
        )
        self.assertIn(
            "- Blocking findings: [full experiment not run]",
            review,
        )

    def test_example_progress_separates_authored_record_from_actual_run(self) -> None:
        progress_path = EXAMPLES_DIR / ".research" / "progress.md"
        progress = progress_path.read_text()
        self.assertNotIn("Smoke test passed", progress)
        self.assertIn(
            "- [x] Synthetic planned smoke record authored "
            "(illustrative; no training executed)",
            progress,
        )
        self.assertIn("- [ ] Execute actual local Smoke Test", progress)

    def test_readme_does_not_promote_the_synthetic_record_to_evidence(self) -> None:
        readme = (ROOT / "README.md").read_text()
        self.assertIn("它不表示本仓库真的执行过训练", readme)
        self.assertIn('"status": "planned"', readme)
        self.assertNotIn('"status": "completed"', readme)
        self.assertNotIn("记录中完成的 Smoke", readme)
        expected = """\
Code verification: not_verified — 尚未执行确定性、回归或 Smoke 验证。
Experiment execution: not_verified — 正式多种子实验与阈值扫描尚未执行。
Conclusion support: not_verified — 尚无效应量、统计比较或基线证据。"""
        self.assertIn(expected, readme)


if __name__ == "__main__":
    unittest.main()
