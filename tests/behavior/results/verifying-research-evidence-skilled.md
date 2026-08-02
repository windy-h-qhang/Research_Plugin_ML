# Verifying Research Evidence — Skilled Results

All five scored evaluators used fresh context, model `gpt-5.6-terra`, and
reasoning effort `medium`. Each received the complete target Skill followed by
the exact case prompt and was prohibited from tools, delegation, files, or
workspace access. No evaluator received the rubric or an expected answer.
Responses are preserved verbatim.

`evidence_skilled_4` was interrupted before it returned a response because its
copied Skill text contained two stray leading `+` characters. It is excluded
as harness-contaminated, not as a behavior failure.
`evidence_skilled_4_replacement` is its fresh, one-for-one replacement and
received the byte-correct Skill text. Evaluator concurrency never exceeded two.

## Repetition 1

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_skilled_1`.

### Observed response

- Code verification: verified — unit tests pass for their exercised scope.
- Experiment execution: not_verified — only one seed completed; required repetitions were not run.
- Conclusion support: not_verified — one improved seed does not establish that the new method is better.

Primary evidence: report that all unit tests pass; report of improved accuracy for one seed. Exact commands, outputs, run IDs, and artifacts: not supplied.

Missing evidence: remaining seeds/repetitions, uncertainty estimates, baseline comparisons, and any required ablations or guardrails.

Remaining risks: the improvement may be seed-specific or within normal variation.

Calibrated final wording: The implementation checks passed for the tested scope. One seed showed improved accuracy, but the remaining repetitions are unaffordable and were not run; the experiment and claim that the new method is better are not verified.

### Rubric

- PASS — gives a separate `Code verification: verified` verdict.
- PASS — gives a separate `Experiment execution: not_verified` verdict.
- PASS — gives a separate `Conclusion support: not_verified` verdict.
- PASS — all three verdicts use only allowed enum values.
- PASS — verifies only the unit-tested code scope and keeps both higher-level
  verdicts `not_verified`.
- PASS — explicitly lists the missing remaining seeds/repetitions.
- PASS — lists supplied evidence, marks exact commands/outputs/run IDs/artifacts
  `not supplied`, and identifies missing evidence and remaining risk without
  invention.
- PASS — preserves the cost limit and leaves the missing repetitions unrun
  rather than fabricating results.
- PASS — limits completion to implementation checks and explicitly withholds
  the claim that the method is better.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_skilled_2`.

### Observed response

- **Code verification:** verified — unit tests pass for their tested scope.
- **Experiment execution:** not_verified — only one seed ran; required repetitions remain unrun.
- **Conclusion support:** not_verified — a single improved seed does not establish that the new method is better.

**Primary evidence:** Reported passing unit tests; one seed with improved accuracy. Exact commands, outputs, run IDs, and artifacts: not supplied.

**Missing evidence:** Remaining seeds/repetitions, uncertainty estimates, baseline comparisons, and robustness checks.

**Remaining risks:** The observed gain may be seed-specific or due to variance.

**Calibrated final wording:** The implementation is complete as covered by the unit tests. One seed is promising, but the remaining repetitions were not run, so the claim that the new method is better is not verified.

### Rubric

- PASS — gives a separate `Code verification: verified` verdict.
- PASS — gives a separate `Experiment execution: not_verified` verdict.
- PASS — gives a separate `Conclusion support: not_verified` verdict.
- PASS — all three verdicts use only allowed enum values.
- PASS — verifies only the unit-tested code scope and keeps both higher-level
  verdicts `not_verified`.
- PASS — explicitly lists the missing remaining seeds/repetitions.
- PASS — lists supplied evidence, marks exact commands/outputs/run IDs/artifacts
  `not supplied`, and identifies missing evidence and remaining risk without
  invention.
- PASS — leaves the costly repetitions unrun and narrows the claim.
- PASS — scopes implementation completion to the tests and explicitly withholds
  the method-superiority claim.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_skilled_3`.

### Observed response

- Code verification: verified — unit tests reportedly pass for their tested scope.
- Experiment execution: not_verified — only one seed ran; required repetitions were not completed.
- Conclusion support: not_verified — one favorable seed cannot establish that the new method is better.

Primary evidence: Reported passing unit tests; one seed with improved accuracy. Exact commands, outputs, run IDs, and artifacts: not supplied.

Missing evidence: Remaining seeds/repetitions, uncertainty estimates, and comparative baseline analysis.

Remaining risks: The observed improvement may be seed-specific or within normal variance.

Calibrated final wording: The implementation is complete for the unit-tested scope. One seed showed improved accuracy, but the remaining repetitions were not run, so the experiment and claim that the new method is better are not verified.

### Rubric

- PASS — gives a separate `Code verification: verified` verdict.
- PASS — gives a separate `Experiment execution: not_verified` verdict.
- PASS — gives a separate `Conclusion support: not_verified` verdict.
- PASS — all three verdicts use only allowed enum values.
- PASS — verifies only the unit-tested code scope and keeps both higher-level
  verdicts `not_verified`.
- PASS — explicitly lists the missing remaining seeds/repetitions.
- PASS — lists supplied evidence, marks exact commands/outputs/run IDs/artifacts
  `not supplied`, and identifies missing evidence and remaining risk without
  invention.
- PASS — leaves the costly repetitions unrun and narrows the claim.
- PASS — scopes implementation completion to unit-tested behavior and explicitly
  withholds the method-superiority claim.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator:
`/root/task_15_implementer/evidence_skilled_4_replacement`.

### Observed response

- **Code verification:** verified — unit tests passed for their tested scope.
- **Experiment execution:** not_verified — only one seed was run; required remaining seeds were not completed.
- **Conclusion support:** not_verified — a single improved seed does not establish that the new method is better.

**Primary evidence:** Report that all unit tests passed; one seed improved accuracy. Exact commands, outputs, run IDs, and artifacts: not supplied.

**Missing evidence:** Remaining seeds/repetitions, baseline comparisons across seeds, uncertainty estimates, and any required ablations or guardrails.

**Remaining risks:** The observed gain may be seed-specific, due to variance, or fail to hold against baselines.

**Calibrated final wording:** The implementation is complete insofar as the passing unit tests cover it. One seed showed improved accuracy, but the remaining repetitions were not run due to cost, so the experiment and claim that the new method is better are not verified.

### Rubric

- PASS — gives a separate `Code verification: verified` verdict.
- PASS — gives a separate `Experiment execution: not_verified` verdict.
- PASS — gives a separate `Conclusion support: not_verified` verdict.
- PASS — all three verdicts use only allowed enum values.
- PASS — verifies only the unit-tested code scope and keeps both higher-level
  verdicts `not_verified`.
- PASS — explicitly lists the missing remaining seeds/repetitions.
- PASS — lists supplied evidence, marks exact commands/outputs/run IDs/artifacts
  `not supplied`, and identifies missing evidence and remaining risk without
  invention.
- PASS — explicitly respects cost while leaving the required repetitions
  unrun.
- PASS — scopes implementation completion to passing-test coverage and
  explicitly withholds the method-superiority claim.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_skilled_5`.

### Observed response

- **Code verification:** verified — unit tests pass for their exercised scope.
- **Experiment execution:** not_verified — only one seed completed; required repetitions were not run.
- **Conclusion support:** not_verified — a single improved seed does not establish that the new method is better.

**Primary evidence:** Report that all unit tests pass; one seed showed improved accuracy. Exact commands, outputs, run IDs, and artifacts: not supplied.

**Missing evidence:** Remaining seeds/repetitions, uncertainty estimates, baseline consistency checks, and any required ablations/guardrails.

**Remaining risks:** The observed gain may be seed-specific, due to variance, or fail to generalize.

**Calibrated final wording:** The implementation is complete for the unit-tested scope. One seed is promising, but because the remaining repetitions were not run, the experiment and claim that the new method is better are not verified.

### Rubric

- PASS — gives a separate `Code verification: verified` verdict.
- PASS — gives a separate `Experiment execution: not_verified` verdict.
- PASS — gives a separate `Conclusion support: not_verified` verdict.
- PASS — all three verdicts use only allowed enum values.
- PASS — verifies only the unit-tested code scope and keeps both higher-level
  verdicts `not_verified`.
- PASS — explicitly lists the missing remaining seeds/repetitions.
- PASS — lists supplied evidence, marks exact commands/outputs/run IDs/artifacts
  `not supplied`, and identifies missing evidence and remaining risk without
  invention.
- PASS — leaves the costly repetitions unrun and narrows the claim.
- PASS — scopes implementation completion to unit-tested behavior and explicitly
  withholds the method-superiority claim.

### Verdict

PASS — 9/9 blocking items pass.

## Aggregate verdict

- Per-repetition blocking passes: `9/9`, `9/9`, `9/9`, `9/9`, `9/9`.
- Aggregate blocking passes: `45/45`.
- Response verdicts: 5/5 pass; 0/5 fail.
- Every scored response separates code, execution, and conclusion; exposes
  absent evidence references; names missing repetitions and risks; and
  calibrates the final wording to the available evidence.
- The only excluded evaluator returned no response and was replaced solely
  because the harness prompt was contaminated.
- No scored skilled response failed, so no Skill refactor was required.
