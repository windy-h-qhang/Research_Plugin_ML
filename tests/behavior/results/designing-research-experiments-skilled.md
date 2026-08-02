# Designing Research Experiments: Skilled Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each received only
`skills/designing-research-experiments/SKILL.md` and the unchanged case prompt,
and was instructed to answer directly without delegation, tools, files, or
workspace access. No evaluator received the rubric or an expected answer. Every
observed response below is preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_skilled_1`

### Observed response

A 0.7 gain on one seed is promising, but it is only a pilot. Do not tune thresholds on the test set; that would invalidate the final comparison.

- **Experiment ID:** ft-method-vs-current-v1
- **Hypothesis:** The new fine-tuning method improves the predeclared primary score by at least 0.7 points versus the current method on the target evaluation population, under the same training budget.
- **Baselines: []** Current fine-tuning method; no-change model.
- **Independent variables: []** Fine-tuning method (new vs. current).
- **Dependent variables: []** Primary score (TBD exact metric); training/inference cost; failure rate.
- **Controlled variables: []** Dataset, preprocessing, base model, prompt/template, hyperparameters except method-specific required settings, compute allocation, training schedule, evaluator, and decoding settings.
- **Data split:** Keep the existing test set untouched. Use training data for fitting and a fixed validation set for all threshold tuning and design choices.
- **Leakage checks: []** Verify train/validation/test deduplication and entity overlap; fit preprocessing only on train; tune thresholds only on validation; run the locked design once on test.
- **Ablations: []** New method with its proposed component removed, if feasible within the method’s definition; otherwise TBD with justification.
- **Primary metrics: []** Mean paired test-set score difference across seeds; 95% confidence interval.
- **Guardrail metrics: []** No more than 10% training-cost increase; no regression greater than 0.2 points on safety/quality metric (TBD).
- **Seeds: []** 3 predeclared paired seeds: 17, 42, 123.
- **Repetitions:** Run both methods for all three seeds, using each seed as a pair; report every run.
- **Resource request:** 6 training runs total. Fastest valid design: first use the three runs per method on validation to lock any threshold; then one final, no-tuning evaluation of all six saved runs on test.
- **Success rule:** Claim improvement only if the mean paired test-score gain is at least 0.7 points, its 95% confidence interval excludes zero, and all guardrails pass.
- **Negative-result rule:** Reject the claimed improvement if the mean gain is below 0.7, the confidence interval includes zero, or any guardrail fails.
- **Inconclusive rule:** If variance is too high for a decisive interval, if results differ materially by seed, or if leakage checks fail, report inconclusive and expand to more paired seeds rather than claiming superiority.
- **Expected artifacts: []** Versioned configs, split IDs, threshold selected on validation, seed list, logs, checkpoints, per-run metrics, paired aggregate and confidence interval, compute usage, and environment details.

If six runs do not fit the budget, the valid faster outcome is a two-seed pilot labeled “promising but inconclusive”—not a superiority claim.

### Rubric

- PASS — rejects test-set threshold tuning and reserves the locked test set for one final evaluation.
- PASS — explicitly names the new method, current method, and no-change baseline.
- PASS — explicitly defines independent, dependent, and controlled variables.
- PASS — defines train, validation, and test uses plus deduplication, entity-overlap, preprocessing, tuning, and final-test leakage checks.
- PASS — predeclares three paired seeds, runs both methods on all, and reports every run.
- PASS — defines a primary paired score difference and cost and quality guardrails.
- PASS — states explicit success, negative-result, and inconclusive rules.
- PASS — narrows an underfunded design to an explicitly inconclusive pilot rather than weakening validity.

### Verdict

PASS — 8/8 blocking groups pass.

## Repetition 2

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_skilled_2`

### Observed response

A one-seed result is a pilot, not enough to claim superiority. Do not tune thresholds on the test set.

- **Experiment ID:** llm-ft-method-vs-current-v1
- **Hypothesis:** The new finetuning method improves the task’s primary score by at least 0.7 points versus the current method, on the fixed target population, under the same training budget.
- **Baselines: []** Current finetuning method; no-training or prior published baseline if applicable.
- **Independent variables: []** Finetuning method: new vs. current.
- **Dependent variables: []** Primary task score; inference/training cost.
- **Controlled variables: []** Model, data, preprocessing, prompts, compute type, training schedule, checkpoint-selection rule, evaluator.
- **Data split:** Train/validation/test split fixed now; validation selects thresholds and checkpoints; test remains untouched for one final evaluation.
- **Leakage checks: []** Deduplicate and check split overlap; fit preprocessing on train only; tune exclusively on validation; run test only after design lock.
- **Ablations: []** New method with its key component removed.
- **Primary metrics: []** Mean paired test-score difference across seeds, with 95% confidence interval.
- **Guardrail metrics: []** Training GPU-hours, inference latency/cost, safety/quality regressions no worse than 1% absolute.
- **Seeds: []** At least 3 paired seeds, using identical seeds/data order where possible.
- **Repetitions:** Run all 3; report every run.
- **Resource request:** 3 paired runs plus one ablation; if this exceeds budget, run 3 paired runs only and defer ablation.
- **Success rule:** Claim improvement only if mean test improvement is positive, its 95% CI excludes zero, and guardrails pass.
- **Negative-result rule:** Reject the superiority claim if the CI includes zero or the mean improvement is non-positive.
- **Inconclusive rule:** If variance is too high for 3 seeds or guardrails conflict, report inconclusive and do not claim better.
- **Expected artifacts: []** Locked configs, split IDs, validation-tuning logs, per-seed metrics, aggregate CI, environment/GPU details.

Fastest defensible path: use the existing 0.7 result only to set the hypothesis, tune thresholds on validation, then run two additional paired seeds and a single locked test evaluation.

### Rubric

- PASS — rejects test-set threshold tuning and reserves the test set for one locked final evaluation.
- PASS — explicitly names the new method, current method, and optional no-training or published baselines.
- PASS — explicitly defines independent, dependent, and controlled variables.
- PASS — defines train, validation, and test uses plus deduplication, overlap, preprocessing, tuning, and final-test leakage checks.
- PASS — requires at least three paired seeds and reports every run.
- PASS — defines a primary paired score difference and compute, latency, and safety/quality guardrails.
- PASS — states explicit success, negative-result, and inconclusive rules.
- PASS — preserves the three paired runs and saves budget by deferring the ablation rather than weakening the claimed comparison.

### Verdict

PASS — 8/8 blocking groups pass.

## Repetition 3

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_skilled_3`

### Observed response

- **Experiment ID:** ft-method-vs-current-v1
- **Hypothesis:** The new finetuning method improves the target task score by at least 0.3 points versus the current method on the fixed evaluation population, averaged across paired random seeds, without worsening guardrails.
- **Baselines: [**current finetuning method**]**
- **Independent variables: [**finetuning method: new vs. current**]**
- **Dependent variables: [**target task score, training cost, failure rate**]**
- **Controlled variables: [**model base, dataset, preprocessing, prompts, hyperparameters except method-specific required settings, compute type, training schedule, checkpoint selection rule, evaluation harness**]**
- **Data split:** Use training data for fitting, validation data for threshold tuning and checkpoint selection, and an untouched test set for one final locked evaluation.
- **Leakage checks: [**deduplicate and check train/validation/test overlap; fit preprocessing only on training data; tune thresholds only on validation; run test evaluation once after locking the design**]**
- **Ablations: [**new method with its proposed contribution removed**]**
- **Primary metrics: [**mean paired test-score difference across seeds**]**
- **Guardrail metrics: [**no increase in failure rate greater than 1 percentage point; median GPU-hours no more than 20% above baseline**]**
- **Seeds: [**11, 29, 47**]**
- **Repetitions:** Three paired runs: each seed trains both methods under identical conditions.
- **Resource request:** First run a one-seed pilot using the existing 0.7-point result, then run the remaining two paired seeds only if validation results meet the preregistered checkpoint/threshold criteria. Estimate: 6 total training runs; GPU-hours TBD from the pilot. No early stopping for superiority claims.
- **Success rule:** Claim “better” only if the mean paired test improvement is at least 0.3 points, its 95% confidence interval excludes 0, and all guardrails pass.
- **Negative-result rule:** Reject the improvement claim if the mean improvement is ≤0, the confidence interval includes no practically meaningful gain (<0.3), or a guardrail fails.
- **Inconclusive rule:** Mark inconclusive if three seeds cannot establish the success or negative-result rule, variance is excessive, or any leakage/checkpoint-selection violation occurs; do not use the test set to resolve it.
- **Expected artifacts: [**locked configs, code version, split IDs, validation-tuning record, seed-level logs and metrics, aggregate uncertainty calculation, hardware/software environment details**]**

The existing one-seed 0.7-point result is encouraging but only a pilot—not enough to claim superiority. Reusing the test set for threshold tuning would invalidate the final comparison; use validation tuning to save scarce GPU time while preserving a credible final test.

### Rubric

- PASS — rejects test-set threshold tuning and reserves an untouched test set for one final locked evaluation.
- PASS — explicitly names the new method and current finetuning baseline.
- PASS — explicitly defines independent, dependent, and controlled variables.
- PASS — defines train, validation, and test uses plus deduplication, overlap, preprocessing, tuning, and final-test leakage checks.
- PASS — predeclares three paired seeds and three paired runs; the validation-stage gate does not select favorable test seeds and cannot support an early superiority claim.
- PASS — defines a primary paired score difference and failure-rate and GPU-hour guardrails.
- PASS — states explicit success, negative-result, and inconclusive rules.
- PASS — estimates the six-run design and marks any underpowered outcome inconclusive rather than weakening the test.

### Verdict

PASS — 8/8 blocking groups pass.

## Repetition 4

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_skilled_4`

### Observed response

- **Experiment ID:** ft-method-vs-current-v1
- **Hypothesis:** The new finetuning method improves the target evaluation score over the current method by at least 0.3 points on the locked test population, under the same training budget.
- **Baselines: []** Current finetuning method; new finetuning method.
- **Independent variables: []** Finetuning method only.
- **Dependent variables: []** Target score; training cost; inference latency.
- **Controlled variables: []** Dataset, model base, preprocessing, prompts, hyperparameter search budget, training schedule, hardware, evaluator, and decoding settings.
- **Data split:** Fixed train/validation/untouched-test split. Use validation only for threshold tuning and design decisions; test is final-only.
- **Leakage checks: []** Verify example/duplicate overlap across splits; fit preprocessing on train only; tune thresholds only on validation; evaluate the locked configuration once on test.
- **Ablations: []** New method with its proposed component removed, plus the current method.
- **Primary metrics: []** Mean paired test-score difference across seeds, with 95% confidence interval.
- **Guardrail metrics: []** No worse than 5% increase in GPU-hours; no regression greater than 0.1 points on required safety/quality metrics.
- **Seeds: []** At least 3 paired seeds for both methods, using identical seed values and data order where applicable.
- **Repetitions:** Report all three paired runs, including the existing 0.7-point single-seed result; do not select favorable runs.
- **Resource request:** Fastest valid design is three paired full runs plus one validation-only tuning pass. If this cannot fit the budget, treat the result as a pilot and make no superiority claim.
- **Success rule:** Claim improvement only if the mean paired test improvement is at least 0.3 points, its 95% confidence interval excludes zero, and all guardrails pass.
- **Negative-result rule:** Reject the improvement claim if the interval includes zero, mean gain is below 0.3, or a guardrail fails.
- **Inconclusive rule:** If three seeds are too variable, checks fail, or budget prevents the repetitions, report the evidence as inconclusive and run more paired seeds when resources permit.
- **Expected artifacts: []** Versioned configs, split IDs and hashes, validation tuning logs, all seed-level metrics, aggregate confidence interval, compute usage, checkpoints, environment/package versions, and locked test evaluation output.

The 0.7-point result is encouraging, but it is only a pilot. Reusing the test set for tuning would invalidate the eventual comparison; the fastest defensible path is to tune once on validation, lock everything, then run paired multi-seed final evaluation.

### Rubric

- PASS — rejects test-set threshold tuning and reserves the test set for final-only evaluation.
- PASS — explicitly names the new method and current finetuning baseline.
- PASS — explicitly defines independent, dependent, and controlled variables.
- PASS — defines train, validation, and test uses plus duplicate-overlap, preprocessing, tuning, and final-test leakage checks.
- PASS — requires at least three paired seeds, reports all runs, and explicitly rejects favorable-run selection.
- PASS — defines a primary paired score difference and GPU-hour and safety/quality guardrails.
- PASS — states explicit success, negative-result, and inconclusive rules.
- PASS — labels an experiment that cannot afford the paired design as a pilot with no superiority claim.

### Verdict

PASS — 8/8 blocking groups pass.

## Repetition 5

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_skilled_5`

### Observed response

- **Experiment ID:** finetune-method-pilot-v1
- **Hypothesis:** The new LLM finetuning method improves the target evaluation score versus the current method by at least 0.7 points on the defined deployment population, under the same training budget.
- **Baselines:** [current finetuning method, new method]
- **Independent variables:** [finetuning method]
- **Dependent variables:** [target evaluation score, training/inference cost, failure rate]
- **Controlled variables:** [model base, data, preprocessing, training schedule, compute allocation, evaluator, prompt format]
- **Data split:** Fixed train/validation/untouched test partitions. Use validation for threshold tuning; keep test locked until the design is fixed.
- **Leakage checks:** [deduplicate and prevent cross-split overlap; fit preprocessing only on train; tune thresholds only on validation; run locked design once on test]
- **Ablations:** [new method with each proposed component removed]
- **Primary metrics:** [mean paired test-score improvement over baseline]
- **Guardrail metrics:** [GPU-hours, latency, failure/safety regressions]
- **Seeds:** [at least 3 paired seeds; ideally 5]
- **Repetitions:** Run every predeclared paired seed for both methods.
- **Resource request:** Fastest valid option: 3 paired seeds as a pilot, plus one final locked test evaluation per seed. If budget cannot support this, the result is exploratory only—not a superiority claim.
- **Success rule:** Claim improvement only if the mean paired improvement is positive, its uncertainty interval excludes zero, the prespecified magnitude threshold is met, and guardrails pass.
- **Negative-result rule:** Reject the predicted improvement if the interval includes no meaningful gain, the mean misses the threshold, or guardrails regress beyond limits.
- **Inconclusive rule:** Mark inconclusive if three seeds yield high variance, mixed outcomes, failed leakage checks, or insufficient budget for repetitions.
- **Expected artifacts:** [configs, split IDs, validation tuning record, logs, per-seed metrics, aggregate uncertainty, environment and compute details]

A single seed with a +0.7 result is a promising pilot, not evidence sufficient to claim the method is better. Reusing the test set for threshold tuning would invalidate the final comparison; scarce GPU time means narrowing the claim or reporting an inconclusive result, not weakening the evaluation.

### Rubric

- PASS — rejects test-set threshold tuning and reserves a locked test set for final evaluation.
- PASS — explicitly names the new method and current finetuning baseline.
- PASS — explicitly defines independent, dependent, and controlled variables.
- PASS — defines train, validation, and test uses plus deduplication, overlap, preprocessing, tuning, and final-test leakage checks.
- PASS — requires at least three paired seeds and every predeclared repetition for both methods.
- PASS — defines a primary paired improvement and compute, latency, failure, and safety guardrails.
- PASS — states explicit success, negative-result, and inconclusive rules.
- PASS — makes an underfunded design exploratory or inconclusive instead of weakening validity.

### Verdict

PASS — 8/8 blocking groups pass.

## Final summary

- Response verdicts: 5/5 pass; 0/5 fail.
- Blocking-group checks: 40/40 pass; 0/40 fail.
- All five responses use the complete experiment-contract shape, reject
  test-set tuning, require paired multi-seed repetitions, and state separate
  success, negative-result, and inconclusive outcomes.
- All five preserve validity under the GPU constraint by narrowing the design
  or claim, deferring an ablation, or labeling an underpowered result
  inconclusive.
- No skilled arm failed, so no refactor or replacement repetition was needed.
- Verdict: GREEN established and retained.
