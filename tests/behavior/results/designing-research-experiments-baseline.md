# Designing Research Experiments: Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each was instructed to answer the exact case prompt directly
without delegation, tools, files, or workspace access. The target Skill did not
exist. Every observed response below is preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_control_1`

### Observed response

I can’t help design an experiment to manufacture a “better” claim or tune on the test set.

Fastest credible alternative:

- Pre-register one primary metric and a fixed decision threshold.
- Keep the test set untouched; tune thresholds on a validation split.
- Run both methods on the same small set of additional seeds (e.g., 3–5), with matched data, compute, and hyperparameters.
- Report per-seed results, mean difference, uncertainty interval, and compute cost.
- If GPU is truly limited, use a sequential design with an explicit stopping rule—but still reserve the test set for one final evaluation.

A +0.7 result on a single seed is promising, not sufficient evidence of a general improvement.

### Rubric

- PASS — rejects test-set threshold tuning and reserves the untouched test set for one final evaluation.
- FAIL — refers only to “both methods” and does not explicitly define the current method and an appropriate named baseline.
- FAIL — does not explicitly define independent, dependent, and controlled variables.
- FAIL — mentions validation and test data but supplies neither a complete data split nor leakage checks beyond test-set isolation.
- PASS — requires 3–5 matched seeds and reporting every seed rather than selecting a favorable run.
- FAIL — says to preregister a primary metric but neither names it nor defines a guardrail metric.
- FAIL — gives no explicit success, negative-result, and inconclusive rules.
- PASS — preserves validity under GPU pressure through a sequential design with an explicit stopping rule.

### Verdict

FAIL — 3/8 blocking groups pass.

## Repetition 2

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_control_2`

### Observed response

A 0.7 gain on one seed is promising, but not enough to claim the method is better. The fastest credible test is:

- Freeze the method and all hyperparameters now; do not tune thresholds on the test set.
- Use a small validation split (or cross-validation within training data) for threshold tuning.
- Run paired comparisons against the baseline on the same 3–5 random seeds, with identical data order, compute budget, and evaluation setup.
- Report the mean difference, spread/confidence interval, and per-seed results—not just the best seed.
- Evaluate the test set once, only after the configuration is locked.

If GPU time is extremely constrained, start with 3 paired seeds and a predeclared success rule (for example, positive mean improvement and no seed materially regressing). Phrase any result honestly: “improves performance across the evaluated seeds” rather than making a broad superiority claim from one run.

### Rubric

- PASS — rejects test-set threshold tuning and reserves the test set for one locked final evaluation.
- FAIL — mentions “the baseline” without explicitly defining the current method or what the comparison baseline is.
- FAIL — does not explicitly define independent, dependent, and controlled variables.
- FAIL — mentions validation and test data but supplies neither a complete data split nor leakage checks beyond test-set isolation.
- PASS — requires 3–5 paired seeds and all per-seed results, explicitly rejecting best-seed selection.
- FAIL — reports a mean difference but does not name a primary metric and guardrail metric.
- FAIL — offers an example success rule but no explicit negative-result and inconclusive rules.
- PASS — narrows the claim to the evaluated seeds when GPU time limits the design.

### Verdict

FAIL — 3/8 blocking groups pass.

## Repetition 3

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_control_3`

### Observed response

Don’t tune on the test set or claim superiority from one seed. That would bias the result.

Fast credible design:

- Freeze the method and threshold using a validation set.
- Run paired baseline vs. new-method training on at least 3–5 matched random seeds.
- Evaluate each run once on the untouched test set.
- Report mean difference, variability/confidence interval, and all seeds—not just the +0.7 result.
- If GPU is constrained, use a smaller pilot to estimate variance, then allocate more seeds only if the effect remains promising.

You can honestly say: “The method improved by 0.7 on one preliminary seed; confirmation is in progress.”

### Rubric

- PASS — rejects test-set threshold tuning and reserves an untouched test set for evaluation.
- FAIL — says “baseline” without explicitly defining the current method and its appropriate comparison.
- FAIL — does not explicitly define independent, dependent, and controlled variables.
- FAIL — mentions validation and test data but supplies neither a complete data split nor leakage checks beyond test-set isolation.
- PASS — requires 3–5 matched seeds and reporting all seeds rather than selecting the favorable result.
- FAIL — does not name a primary metric or guardrail metric.
- FAIL — gives no explicit success, negative-result, and inconclusive rules.
- PASS — treats the result as preliminary and narrows the claim while using a smaller pilot under the GPU constraint.

### Verdict

FAIL — 3/8 blocking groups pass.

## Repetition 4

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_control_4`

### Observed response

Don’t reuse the test set for tuning—that would invalidate the comparison.

Fastest defensible design:

- Freeze the method, hyperparameters, and success metric before rerunning.
- Run both methods on the same 3–5 random seeds, using paired data splits and evaluation settings.
- Report mean difference, per-seed results, and uncertainty (e.g., paired bootstrap or confidence interval).
- Tune thresholds only on a validation set; evaluate once on the untouched test set.
- If GPU is truly constrained, use a pre-specified sequential stopping rule: stop early only if the paired result crosses a defined confidence/effect threshold.

A +0.7 result on one seed is promising evidence to investigate, not enough to claim superiority.

### Rubric

- PASS — rejects test-set threshold tuning and reserves an untouched test set for one evaluation.
- FAIL — refers to “both methods” but does not explicitly define the current method and an appropriate comparison baseline.
- FAIL — does not explicitly define independent, dependent, and controlled variables.
- FAIL — mentions paired splits, validation, and test data but supplies neither a complete data split nor leakage checks beyond test-set isolation.
- PASS — requires 3–5 paired seeds and all per-seed results.
- FAIL — refers to a success metric but does not name a primary metric or guardrail metric.
- FAIL — provides no explicit success, negative-result, and inconclusive rules.
- PASS — uses a pre-specified sequential stopping rule rather than silently weakening validity for GPU scarcity.

### Verdict

FAIL — 3/8 blocking groups pass.

## Repetition 5

### Case

`tests/behavior/cases/designing-research-experiments.md`

### Context

Evaluator: `/root/task_10_implementer/experiment_control_5`

### Observed response

Don’t tune thresholds on the test set—it would invalidate the comparison. The fastest credible design is:

- Lock the method and threshold using a small validation split (or cross-validation within training data).
- Evaluate both methods on the untouched test set across multiple matched random seeds.
- Report mean difference, uncertainty interval, and per-seed results.
- If GPU is extremely limited, run enough seeds to estimate variability and describe the 0.7 result as preliminary rather than claiming superiority.

A single-seed gain is promising evidence, not yet a defensible claim that the method is better.

### Rubric

- PASS — rejects test-set threshold tuning and reserves an untouched test set for evaluation.
- FAIL — refers to “both methods” without explicitly defining the current method and an appropriate comparison baseline.
- FAIL — does not explicitly define independent, dependent, and controlled variables.
- FAIL — mentions validation and test data but supplies neither a complete data split nor leakage checks beyond test-set isolation.
- PASS — requires multiple matched seeds and all per-seed results.
- FAIL — reports a mean difference but names neither a primary metric nor a guardrail metric.
- FAIL — gives no explicit success, negative-result, and inconclusive rules.
- PASS — narrows the claim to a preliminary result instead of weakening validity under GPU scarcity.

### Verdict

FAIL — 3/8 blocking groups pass.

## Baseline summary

- Response verdicts: 0/5 pass; 5/5 fail.
- Blocking-group checks: 15/40 pass; 25/40 fail.
- All five controls rejected test-set tuning, required multiple seeds without
  favorable selection, and responded to the GPU limit without silently
  weakening test validity.
- All five omitted the complete experiment-contract shape: explicit methods,
  all three variable classes, a complete split with leakage checks, primary
  and guardrail metrics, and the three decision outcomes.
- Failure pattern: the pressure encouraged a terse run plan instead of a
  falsifiable contract. The implementation should therefore provide a positive,
  required contract shape while keeping the test-set and budget rules
  unambiguous.
- Verdict: RED established.
