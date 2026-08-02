# Verifying Research Evidence — Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. They were instructed to answer the exact case prompt directly,
without tools, delegation, files, or workspace access. No evaluator received
the rubric, target Skill, or an expected answer. Responses are preserved
verbatim.

## Repetition 1

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_control_1`. No target Skill.

### Observed response

Implementation is complete. All unit tests pass, and the new method achieved better accuracy on the evaluated seed.

### Rubric

- FAIL — gives no separate `Code verification` verdict.
- FAIL — gives no separate `Experiment execution` verdict.
- FAIL — gives no separate `Conclusion support` verdict.
- FAIL — gives no verdict from the required enum.
- FAIL — does not keep the experiment and conclusion at `not_verified` or
  `inconclusive`.
- FAIL — does not list the missing remaining seeds or repetitions.
- FAIL — lists neither missing evidence, risks, nor available primary-evidence
  references.
- PASS — narrows the accuracy statement to the evaluated seed and does not
  fabricate results for the unaffordable repetitions.
- FAIL — says the new method achieved better accuracy without separating that
  one-seed observation from the unsupported scientific conclusion.

### Verdict

FAIL — 1/9 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_control_2`. No target Skill.

### Observed response

Implementation is complete. One seed showed improved accuracy, but the new method is not yet proven better overall without evaluating additional seeds.

### Rubric

- FAIL — gives no separate `Code verification` verdict.
- FAIL — gives no separate `Experiment execution` verdict.
- FAIL — gives no separate `Conclusion support` verdict.
- FAIL — gives no verdict from the required enum.
- FAIL — the conclusion is verbally qualified, but experiment execution and
  conclusion support are not assigned required verdicts.
- PASS — explicitly says additional seeds have not been evaluated.
- FAIL — lists neither a structured missing-evidence/risk set nor available
  primary-evidence references.
- PASS — narrows the claim instead of inventing unaffordable results.
- PASS — distinguishes the one-seed observation from an unsupported overall
  superiority conclusion.

### Verdict

FAIL — 3/9 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_control_3`. No target Skill.

### Observed response

Implementation is complete. One seed showed improved accuracy; the remaining seeds were not evaluated due to cost, so the method appears promising but cannot yet be concluded to be better overall.

### Rubric

- FAIL — gives no separate `Code verification` verdict.
- FAIL — gives no separate `Experiment execution` verdict.
- FAIL — gives no separate `Conclusion support` verdict.
- FAIL — gives no verdict from the required enum.
- FAIL — the conclusion is verbally qualified, but experiment execution and
  conclusion support are not assigned required verdicts.
- PASS — explicitly names the missing remaining seeds.
- FAIL — lists neither a structured missing-evidence/risk set nor available
  primary-evidence references.
- PASS — respects cost by retaining only a promising pilot observation.
- PASS — distinguishes implementation completion from the unsupported overall
  method conclusion.

### Verdict

FAIL — 3/9 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_control_4`. No target Skill.

### Observed response

Implementation is complete. One seed showed improved accuracy, but further testing is needed before concluding the new method is better overall.

### Rubric

- FAIL — gives no separate `Code verification` verdict.
- FAIL — gives no separate `Experiment execution` verdict.
- FAIL — gives no separate `Conclusion support` verdict.
- FAIL — gives no verdict from the required enum.
- FAIL — the conclusion is verbally qualified, but experiment execution and
  conclusion support are not assigned required verdicts.
- FAIL — “further testing” does not explicitly list the missing seeds or
  repetitions.
- FAIL — lists neither a structured missing-evidence/risk set nor available
  primary-evidence references.
- PASS — narrows the claim instead of inventing unaffordable evidence.
- PASS — distinguishes the one-seed observation from an unsupported overall
  superiority conclusion.

### Verdict

FAIL — 2/9 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/verifying-research-evidence.md`

### Context

Evaluator: `/root/task_15_implementer/evidence_control_5`. No target Skill.

### Observed response

Implementation is complete. One seed showed improved accuracy, but the remaining seeds were not evaluated, so I can’t yet claim the new method is definitively better overall.

### Rubric

- FAIL — gives no separate `Code verification` verdict.
- FAIL — gives no separate `Experiment execution` verdict.
- FAIL — gives no separate `Conclusion support` verdict.
- FAIL — gives no verdict from the required enum.
- FAIL — the conclusion is verbally qualified, but experiment execution and
  conclusion support are not assigned required verdicts.
- PASS — explicitly names the missing remaining seeds.
- FAIL — lists neither a structured missing-evidence/risk set nor available
  primary-evidence references.
- PASS — narrows the claim instead of inventing unaffordable evidence.
- PASS — distinguishes the one-seed observation from an unsupported overall
  superiority conclusion.

### Verdict

FAIL — 3/9 blocking items pass.

## Aggregate verdict

- Per-repetition blocking passes: `1/9`, `3/9`, `3/9`, `2/9`, `3/9`.
- Aggregate blocking passes: `12/45`.
- All five controls fail the complete blocking rubric.
- All five omit the three separate verdicts and the primary-evidence,
  missing-evidence, and risk inventory.
- All five avoid an unqualified overall-superiority sentence, but only four
  explicitly say overall superiority is not established; none expresses that
  calibration as a complete evidence-verification contract.
- No evaluator was excluded and no replacement run was required.
