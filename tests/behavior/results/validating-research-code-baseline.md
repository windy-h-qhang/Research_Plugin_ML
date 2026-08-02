# Validating Research Code — Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. They were instructed to answer the exact case prompt directly,
without tools, delegation, or workspace access. No evaluator received the
rubric, target Skill, or an expected answer. Responses are preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_control_1`. No target Skill.

### Observed response

No—the method is not validated by a single successful 20-step run.

At minimum, test that the new loss:
- produces finite values and gradients;
- has the intended effect on a fixed small batch;
- works correctly with gradient accumulation (equivalent updates to a larger effective batch, within tolerance);
- does not break checkpointing, mixed precision, or distributed training if used;
- remains stable over a short multi-seed smoke run.

A short run only validates that the code can execute; it does not establish correctness, stability, or improvement.

### Rubric

- FAIL — the fixed-batch checks lack hand-computed/trusted-reference expected
  values and declared tolerances.
- PASS — checks accumulated updates against an equivalent larger effective batch.
- PASS — checks finite values/gradients and relevant mixed-precision or distributed behavior.
- FAIL — the smoke run is short but has neither an explicit bound nor a fixed seed.
- PASS — says a short run validates only that the code executes.
- FAIL — does not explicitly report missing correctness-regression or controlled-benchmark evidence.
- FAIL — does not explicitly report missing multi-seed, ablation, and statistical-conclusion evidence.
- PASS — explicitly says the method is not validated.
- FAIL — does not report every omitted validation layer as not verified.

### Verdict

FAIL — 4/9 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_control_2`. No target Skill.

### Observed response

No—the method is not validated yet. One successful 20-step run only shows the code can execute briefly.

At minimum, test:

- Loss values and gradients on controlled inputs; ensure the new loss is finite and has the intended scale.
- Gradient-accumulation equivalence: compare one effective batch against the same batch split across accumulation steps, including optimizer-step timing and loss normalization.
- A short multi-seed smoke run that checks for NaNs, exploding norms, and reproducible behavior.
- An ablation comparing the prior loss/configuration to the new one under the same short budget.

That establishes implementation correctness and basic stability—not empirical effectiveness. Validation of the method needs repeated runs and comparison against a baseline on the target metric.

### Rubric

- FAIL — controlled inputs and intended scale are named, but no strict expected-value/reference loss test is specified.
- PASS — checks batch splitting, optimizer timing, and loss normalization under accumulation.
- PASS — checks finite loss, gradients, NaNs, and exploding norms.
- FAIL — the smoke run is short but has neither an explicit bound nor a fixed seed.
- PASS — says the successful short run shows only brief execution.
- PASS — explicitly requires the currently missing comparison against a baseline on the target metric.
- FAIL — mentions an ablation and repeated runs but does not explicitly report missing multi-seed, ablation, and statistical-conclusion evidence as a group.
- PASS — explicitly says the method is not validated yet.
- FAIL — does not report every omitted validation layer as not verified.

### Verdict

FAIL — 5/9 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_control_3`. No target Skill.

### Observed response

No. A single successful 20-step run only shows the code can execute briefly; it does not validate the method.

At minimum, add tests for:

- Loss correctness on known inputs and gradients (including edge cases).
- Gradient-accumulation equivalence: accumulated microbatches should match a single larger batch within tolerance.
- Optimizer/scheduler step counts and scaling after the accumulation change.
- A short deterministic regression run checking finite loss, no NaNs, and reproducible metrics.

Then run several seeds and compare against the prior baseline on a small, fixed validation setup. Only after the new loss consistently improves or at least preserves the intended metric should the method be considered validated.

### Rubric

- PASS — specifies correctness on known inputs, gradients, and edge cases.
- PASS — checks accumulated microbatches against a larger batch and checks step counts/scaling.
- PASS — checks finite loss, NaNs, gradients, and scaling.
- FAIL — the deterministic run is short but has no explicit step/time/data bound or named fixed seed.
- PASS — says the existing successful short run shows only brief execution.
- PASS — explicitly requires the currently missing comparison to the prior baseline on a fixed validation setup.
- FAIL — requires several seeds but does not report missing ablation and statistical-conclusion evidence.
- PASS — explicitly says the method is not currently validated.
- FAIL — does not report every omitted validation layer as not verified.

### Verdict

FAIL — 6/9 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_control_4`. No target Skill.

### Observed response

No. One successful 20-step run only shows the code can execute briefly; it does not validate the method.

Necessary checks:

- Unit-test the new loss and its gradients on controlled inputs.
- Test gradient accumulation matches an equivalent larger batch update.
- Run short, seeded comparisons against the prior baseline across multiple seeds.
- Verify loss, gradients, and optimizer behavior are stable beyond 20 steps.
- Confirm the change improves the intended metric on a held-out validation set.

That is enough for an initial validation pass; a full experiment can wait until these checks pass.

### Rubric

- FAIL — controlled inputs are named, but no strict expected-value/reference loss test is specified.
- PASS — checks accumulated updates against an equivalent larger batch.
- PASS — checks loss, gradients, and optimizer stability.
- FAIL — the comparisons are short and seeded but no fixed seed or explicit execution bound is specified.
- PASS — says the existing short run shows only brief execution.
- PASS — explicitly requires the currently missing prior-baseline comparison and held-out metric.
- FAIL — mentions multiple seeds but does not report missing ablation and statistical-conclusion evidence.
- PASS — explicitly says the method is not currently validated.
- FAIL — does not report every omitted validation layer as not verified.

### Verdict

FAIL — 5/9 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_control_5`. No target Skill.

### Observed response

No. A single successful 20-step run only shows the code can execute briefly; it does not validate the method.

Run focused checks: loss unit tests and gradients, gradient-accumulation equivalence against a larger effective batch, resume/optimizer-step behavior, and a few short seeded training runs compared with the prior baseline. Then confirm the new loss improves or at least preserves the target metric.

### Rubric

- FAIL — loss unit tests are requested without a strict deterministic expected-value/reference case.
- PASS — checks accumulation equivalence against a larger effective batch and optimizer-step behavior.
- FAIL — gradients are named, but relevant tensor and numerical invariants are not specified.
- FAIL — a few short seeded runs do not name a fixed seed or explicit execution bound.
- PASS — says the existing short run shows only brief execution.
- PASS — explicitly requires the currently missing prior-baseline comparison on the target metric.
- FAIL — does not report missing multi-seed, ablation, and statistical-conclusion evidence.
- PASS — explicitly says the method is not validated.
- FAIL — does not report every omitted validation layer as not verified.

### Verdict

FAIL — 4/9 blocking items pass.

## Aggregate verdict

- Per-repetition blocking passes: `4/9`, `5/9`, `6/9`, `5/9`, `4/9`.
- Aggregate blocking passes: `24/45`.
- All five controls fail the complete blocking rubric.
- Repeated failures: no explicitly bounded fixed-seed Smoke Test; no complete
  report of missing conclusion evidence; no five-layer verified/not-verified
  status.
- No evaluator was excluded and no replacement run was required.
