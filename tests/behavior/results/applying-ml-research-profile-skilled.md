# Applying ML Research Profile — Skilled Results

Fresh evaluators received the current Skill before the single prompt. They
received no rubric or expected answer and had no access to tools, files, the
workspace, browsing, or delegation. Every response from every iteration is
retained verbatim below.

## Iteration 1: failed regression

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh with-Skill context using the first RED-informed Skill revision. Agent:
`/root/task_16_implementer/t16_skill_primary_1`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and biases the reported result. Choose thresholds using a held-out validation set; reserve the test set for one final evaluation.
> - Changing class sampling can alter the effective training distribution. Keep the class map fixed, document the sampling change, and compare it with the prior setup under otherwise identical conditions.
> - Overall accuracy is insufficient for a highly imbalanced classifier. Report per-class precision, recall, and F1, plus balanced metrics such as balanced accuracy and macro-F1. Inspect confusion matrices and calibration, including per-class calibration where decisions depend on confidence.
> - Confirm train/validation/test identity and non-overlap, fit preprocessing only on training data, and ensure evaluation distribution is explicit.
> - Run the controlled comparison across multiple predeclared seeds and report variability or a statistical comparison.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — checks the class map and compares the sampling change.
- PASS — requires per-class and balanced metrics instead of accuracy alone.
- PASS — checks calibration and preprocessing.
- FAIL — requires multiple seeds and a repeated controlled comparison but does
  not require controlled data order.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

FAIL — 5/6. This regression was retained and excluded from the final arm. The
Skill was minimally revised to require identical data order within paired
control/candidate runs.

## Iteration 2: superseded arm

This complete primary arm passed, but the counter arm exposed a new routing
failure in its second repetition. All seven responses are retained. The arm was
excluded after the Skill was minimally revised again, and both prompts were
rerun in fresh final contexts.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_primary_1`

#### Observed response

> The experiment is not valid for a reliable quality claim:
>
> - Tuning the confidence threshold on the test set leaks test information and inflates reported performance. Select it using a held-out validation set, then evaluate once on an untouched test set.
> - After changing class sampling, explicitly verify the class map, preprocessing, and split identities are unchanged; check for duplicates or overlap. Report the evaluation distribution and compare against the prior sampling setup.
> - Overall accuracy is inadequate for high imbalance. Report per-class precision, recall, and F1, plus balanced accuracy (and preferably confusion matrix / PR-AUC where relevant).
> - If confidence thresholds matter, assess calibration, potentially by class.
> - Compare the sampling change to a fixed control using matched data order and multiple predeclared random seeds, reporting uncertainty.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6, but excluded with the superseded arm.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_primary_2`

#### Observed response

> The experiment is not valid for a reliable quality claim.
>
> - Threshold tuning on the test set leaks test information; tune it on a held-out validation set, then evaluate the final fixed threshold once on test.
> - Changing class sampling requires documenting the class map and evaluating against the intended real-world distribution. Compare against the prior sampling setup with all other factors held fixed and inspect per-class effects.
> - Overall accuracy is inadequate under heavy imbalance. Report per-class precision, recall, and F1, plus balanced metrics such as balanced accuracy or macro-F1. Include calibration assessment if confidence thresholds matter.
> - Use identical split definitions and train-only fitted preprocessing; check for duplicates or overlap across splits.
> - Run paired control/candidate comparisons using identical data order across multiple predeclared seeds, and report uncertainty rather than selecting a single result.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6, but excluded with the superseded arm.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_primary_3`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and inflates reported performance. Choose thresholds using a held-out validation set, then evaluate once on an untouched test set.
> - Changing class sampling can alter the learned decision boundary and apparent aggregate performance. Keep the class map fixed, document the training and evaluation distributions, compare against the prior sampling setup, and inspect per-class effects.
> - Overall accuracy is inadequate under heavy imbalance; it can look high while minority classes fail. Report per-class precision, recall, and F1, plus balanced accuracy (and ideally macro-F1 / PR-AUC where appropriate).
> - If confidence is used operationally, evaluate calibration as well, including class-specific behavior if the risks differ by class.
> - Ensure splits are free of overlapping or duplicate examples and that preprocessing is fit only on training data.
> - Compare the new setup to a controlled baseline with identical data order and paired, predeclared multiple seeds; report variability rather than a single favorable run.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6, but excluded with the superseded arm.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_primary_4`

#### Observed response

> The experiment is not valid for a model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information. Select it using a held-out validation set, then evaluate once on the untouched test set.
> - Changing class sampling can alter training distribution and potentially class behavior. Keep the class map fixed, document the sampling change, and compare against the prior setup with identical splits and preprocessing.
> - Overall accuracy is misleading under heavy imbalance. Report per-class precision, recall, and F1, plus balanced accuracy; inspect confusion matrices and calibration where confidence thresholds matter.
> - Verify no duplicates or overlapping records cross train/validation/test splits, and that preprocessing was fit only on training data.
> - Support any claimed improvement with paired control-versus-change runs using identical data order across multiple predeclared seeds, reporting uncertainty rather than a selected single run.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6, but excluded with the superseded arm.

### Primary repetition 5

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_primary_5`

#### Observed response

> The experiment is not valid for a model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information; choose it on a held-out validation set, then evaluate the fixed threshold once on test data.
> - After changing class sampling, confirm the class map and preprocessing are unchanged, document the evaluation distribution, and check for split overlap or duplicates.
> - Overall accuracy is insufficient under heavy imbalance. Report per-class precision, recall, and F1, plus balanced accuracy (and appropriate PR-based metrics); inspect minority-class performance explicitly.
> - If confidence scores matter, assess calibration, potentially per class.
> - Compare against the prior sampling setup using paired control runs: same splits, data order, and multiple predeclared random seeds, with uncertainty reported.
>
> Until those changes are made, the reported accuracy cannot establish that the classifier improved.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6, but excluded with the superseded arm.

### Counter-example repetition 1

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_counter_1`

#### Observed response

> This is a pure systems benchmark, so apply the AI Infrastructure Profile—not ML-quality checks. Review p99 using warm-up exclusion, fixed inputs/shapes, synchronized timing, enough repetitions, controlled GPU clocks/load, and report distribution details (sample count, median/p95/p99, outliers, environment). Compare against a stable baseline under identical conditions and repeat runs to quantify variance.

#### Rubric

- PASS — routes the pure systems benchmark to the AI Infrastructure Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3, but excluded with the superseded arm.

### Counter-example repetition 2

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_post_counter_2`

#### Observed response

> Treat this as a pure systems benchmark; ML-quality checks are not applicable.
>
> For p99 latency, use sufficient repeated, warmed-up kernel invocations; synchronize GPU work before reading timings; report the timing method, input shapes/dtypes, hardware/software versions, and whether allocations are excluded. Keep workload and clock/power conditions fixed, report sample count plus p50/p95/p99, and repeat runs to show variability.

#### Rubric

- FAIL — identifies a pure systems benchmark and excludes ML-quality checks but
  does not name the AI Infrastructure Profile as primary.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

FAIL — 2/3. This regression was retained and excluded. The Skill was minimally
revised to require an explicit opening statement that the AI Infrastructure
Profile is primary and the ML Research Profile does not apply.

## Iteration 3: superseded arm after scoring audit

This arm was initially recorded as final. Review against the same strict
standard used for the baseline found that primary repetitions 1 and 4 listed
sampling and per-class metrics separately without stating that sampling changes
can hide or distort per-class behavior. Those two rubric decisions are
corrected below without changing either observed response. Because the primary
arm therefore failed, the Skill was edited again and both prompts were rerun in
fresh contexts.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_primary_1`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and biases the reported result. Select thresholds using a held-out validation set, then evaluate once on the untouched test set.
> - After changing class sampling, explicitly verify the class map and preprocessing are unchanged, document the evaluation distribution, and compare against the prior sampling setup under otherwise identical conditions.
> - Overall accuracy is inadequate for a highly imbalanced classifier; it can look strong while minority classes fail. Report per-class precision, recall, and F1, plus balanced accuracy (and calibration metrics if confidence scores drive decisions).
> - To attribute improvements to sampling or thresholding, compare against a fixed control with identical data order and paired, predeclared multiple seeds; report variation or statistical uncertainty.

#### Rubric

- PASS — test-set threshold leakage.
- FAIL — checks the sampling change and later requires per-class metrics, but
  does not state that sampling changes can hide or distort per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

FAIL — 5/6. Retained as a failed regression in this superseded arm.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_primary_2`

#### Observed response

> The experiment is not valid for a model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information; choose it on a held-out validation set, then evaluate once on the untouched test set.
> - After changing class sampling, verify the class map is unchanged, document both training and evaluation distributions, and compare against the prior sampling scheme. Inspect results per class.
> - Overall accuracy is inadequate for a highly imbalanced classifier. Report per-class precision, recall, and F1, plus balanced metrics such as balanced accuracy or macro-F1. Assess calibration as well if confidence thresholds are used.
> - Ensure preprocessing was fit only on training data and that there are no duplicates or overlap between splits.
> - Establish the sampling change with paired control/candidate runs using identical data order and multiple predeclared seeds; report variation or a statistical comparison.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — the sampling comparison explicitly says to inspect results per class.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_primary_3`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and overstates performance. Tune it on a held-out validation set, then evaluate once on an untouched test set.
> - With changed class sampling, document the new sampling policy, preserve a consistent class map, and confirm preprocessing and split identity did not change. Evaluate on the intended real-world class distribution.
> - Overall accuracy is inadequate for a highly imbalanced classifier. Report per-class precision, recall, and F1, plus balanced accuracy (and a confusion matrix); inspect which classes gained or lost performance.
> - If confidence decisions matter, assess calibration, ideally per class, before and after threshold selection.
> - Compare the sampling change against an unchanged control with identical data order and paired, predeclared multiple seeds; report variation or a statistical comparison.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_primary_4`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and biases reported performance. Select it using a held-out validation set, then evaluate once on the untouched test set.
> - Changing class sampling can alter the learned decision boundary and effective class prior. Keep the class map fixed, document the new sampling distribution, compare against the prior setup under otherwise identical conditions, and evaluate on the intended real-world distribution.
> - Overall accuracy is insufficient for a highly imbalanced classifier; it can look strong while minority classes fail. Report per-class precision, recall, and F1, plus balanced accuracy and an appropriate aggregate such as macro F1. Include confusion matrices.
> - If confidence thresholds are operationally important, assess calibration (including class-level behavior where relevant) and set thresholds from validation data.
> - Ensure split integrity and preprocessing consistency, and establish the sampling-change effect with paired control/candidate runs using identical data order across multiple predeclared seeds, reporting uncertainty.

#### Rubric

- PASS — test-set threshold leakage.
- FAIL — discusses sampling and per-class metrics separately without stating
  that sampling changes can hide or distort per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

FAIL — 5/6. Retained as a failed regression in this superseded arm.

### Primary repetition 5

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_primary_5`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information. Choose thresholds using a held-out validation set, then evaluate once on the untouched test set.
> - After changing class sampling, explicitly preserve and verify the class map, preprocessing, split identities, and the test-set distribution. Compare against the prior sampling setup and inspect each class.
> - Overall accuracy is inadequate for a highly imbalanced classifier. Report per-class precision, recall, and F1, plus balanced accuracy (and preferably macro-F1 / PR-AUC where appropriate).
> - If confidence scores drive decisions, assess calibration, including class-specific behavior if material.
> - Establish the sampling change with paired control-versus-candidate runs using identical splits/data order across multiple predeclared seeds, and report variation or a statistical comparison.
>
> Re-run the experiment with threshold selection isolated to validation data and the expanded imbalanced-class evaluation.

#### Rubric

- PASS — test-set threshold leakage.
- PASS — class-map and sampling comparison with per-class behavior.
- PASS — per-class and balanced metrics instead of accuracy alone.
- PASS — calibration and preprocessing consistency.
- PASS — controlled data order, multiple seeds, and repeated comparison.
- PASS — no AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Counter-example repetition 1

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_counter_1`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply.
>
> For p99 latency, use a warm-up phase, synchronize GPU timing correctly, collect enough steady-state samples, report hardware/software configuration, and isolate the kernel from unrelated work. Use a robust percentile calculation, examine outliers, and compare against a controlled baseline under identical clock, power, and workload conditions.

#### Rubric

- PASS — explicitly says the AI Infrastructure Profile is primary and the ML
  Research Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

#### Verdict

PASS — 3/3.

### Counter-example repetition 2

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_counter_2`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure Triton-kernel latency benchmark with no model-quality change.
>
> For p99 latency, use many warm-up iterations, synchronize CUDA around timed regions, exclude compilation/autotuning and one-time allocation, and report the sample count, percentile method, hardware/software versions, clock/power settings, input shapes, and batch sizes. Run repeated benchmark trials and report p50/p95/p99 plus variability; inspect outliers for interference, frequency changes, memory pressure, or asynchronous work leaking into the measurement.

#### Rubric

- PASS — explicitly says the AI Infrastructure Profile is primary and the ML
  Research Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

#### Verdict

PASS — 3/3.

### Counter-example repetition 3

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_counter_3`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply.
>
> For p99 Triton-kernel latency, use warm-up iterations, GPU synchronization around timing, fixed shapes/dtypes/layouts, and a large enough sample count. Report the timing method, percentile definition, hardware/software versions, clock/power settings, and whether data-transfer time is excluded. Compare against a baseline under identical conditions, include median and p50/p99 (plus variance), and repeat runs to assess stability.

#### Rubric

- PASS — explicitly says the AI Infrastructure Profile is primary and the ML
  Research Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

#### Verdict

PASS — 3/3.

### Counter-example repetition 4

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_counter_4`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply.
>
> For a credible Triton-kernel p99 latency measurement, use a warmed-up, synchronized benchmark with fixed tensor shapes, dtypes, strides, device, clock/power conditions, and kernel configuration. Measure many independent iterations with CUDA events (or an equivalent GPU-timing mechanism), exclude compilation and warm-up, report p50/p90/p99 plus sample count, and compare against a stable baseline under identical conditions. Check for outliers from allocation, stream contention, DVFS, or concurrent workloads, and repeat benchmark batches to show p99 stability.

#### Rubric

- PASS — explicitly says the AI Infrastructure Profile is primary and the ML
  Research Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

#### Verdict

PASS — 3/3.

### Counter-example repetition 5

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_final_counter_5`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure systems latency benchmark with no model-quality change.
>
> For a credible p99 result, use a warm-up phase, many timed iterations, CUDA-event timing with synchronization, fixed shapes/dtypes/layouts, and report hardware, driver, CUDA, Triton, and clock/power settings. Separate compilation and cache effects from steady-state timing, control concurrent GPU activity, and report p50/p90/p99 plus sample count and repeated-run variability.

#### Rubric

- PASS — explicitly says the AI Infrastructure Profile is primary and the ML
  Research Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

#### Verdict

PASS — 3/3.

## Aggregate through iteration 3

- Iteration 3 primary per repetition: 5/6, 6/6, 6/6, 5/6, 6/6 =
  28/30.
- Iteration 3 counter-example per repetition: 3/3, 3/3, 3/3, 3/3, 3/3 =
  15/15.
- Iteration 3 total: 43/45.
- Iteration 3 complete passes: primary 3/5; counter-example 5/5.
- Failed regressions retained and excluded: iteration 1 primary (5/6);
  iteration 2 counter-example repetition 2 (2/3); iteration 3 primary
  repetitions 1 and 4 (5/6 each).
- Other superseded responses retained and excluded: iteration 2 primary
  repetitions 1–5 and counter-example repetition 1; iteration 3 primary
  repetitions 2, 3, and 5 and counter-example repetitions 1–5.
- Contamination, interruption, timeout, or replacement samples: none.
- GREEN is not established by any arm recorded above.

## Iteration 4: final post-review arm

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_primary_1`

#### Observed response

> The experiment is not valid for a model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information; choose it using a held-out validation set, then evaluate once on the untouched test set.
> - Overall accuracy is inadequate under heavy class imbalance. Report per-class precision, recall, and F1, plus balanced accuracy (and calibration metrics if confidence is used for decisions).
> - Changing class sampling can materially alter apparent class performance. Keep the class map and evaluation distribution fixed and explicit; compare against the prior sampling setup using the same per-class metrics, not accuracy alone.
> - Verify no train/validation/test overlap or duplicates, and that preprocessing was fit only on training data.
> - To attribute changes to sampling or thresholding, use a controlled comparison: hold other settings fixed, pair candidate/control runs with identical data order per seed, repeat over multiple predeclared seeds, and report uncertainty.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — states that sampling can alter apparent class performance and requires
  the same per-class metrics for the sampling comparison.
- PASS — rejects accuracy alone and requires per-class and balanced metrics.
- PASS — checks preprocessing and split consistency.
- PASS — requires identical data order, multiple predeclared seeds, and repeated
  controlled comparisons.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_primary_2`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> Tuning the confidence threshold on the test set leaks test information and makes the reported result optimistically biased. Select the threshold using a held-out validation set, lock it, then evaluate once on the untouched test set.
>
> With changed class sampling, overall accuracy is insufficient and may be misleading. Keep the class mapping and test distribution explicit, compare against the prior sampling setup under otherwise identical conditions, and report per-class precision, recall, and F1 plus balanced metrics such as balanced accuracy or macro F1. Inspect how sampling changed each class’s behavior, not just the aggregate.
>
> For a credible comparison, use matched control/candidate runs with identical data order across multiple predeclared seeds, and report uncertainty or statistical comparisons.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — explicitly requires inspecting how sampling changed each class's
  behavior rather than only the aggregate.
- PASS — rejects accuracy alone and requires per-class and balanced metrics.
- PASS — keeps the class mapping explicit for the comparison.
- PASS — requires identical data order, multiple predeclared seeds, and repeated
  matched comparisons.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_primary_3`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> Tuning the confidence threshold on the test set leaks test information and inflates reported performance. Select the threshold on a held-out validation set, lock it, then evaluate once on the untouched test set.
>
> With changed class sampling, overall accuracy is inadequate and may be misleading. Keep the class map and test distribution explicit, compare against the prior sampling setup under matched conditions, and report per-class precision, recall, and F1 plus balanced metrics such as balanced accuracy or macro-F1. Inspect those per-class results at the same comparison point as the sampling change, since sampling can mask degraded minority-class behavior.
>
> For a defensible conclusion, fit preprocessing only on training data, verify no split overlap or duplicates, and run the sampling change against a control with identical data order and paired predeclared seeds across multiple runs, reporting uncertainty.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — states that sampling can mask degraded minority-class behavior and
  requires per-class inspection in the same comparison point.
- PASS — rejects accuracy alone and requires per-class and balanced metrics.
- PASS — checks preprocessing and split consistency.
- PASS — requires identical data order, paired predeclared seeds, and multiple
  controlled runs.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_primary_4`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Threshold tuning on the test set leaks test information; choose it on a held-out validation set, then evaluate the fixed threshold once on test.
> - Overall accuracy is inadequate under heavy imbalance. Report per-class precision, recall, and F1, plus balanced accuracy (and calibration where confidence decisions matter).
> - The class-sampling change must preserve an explicit, stable class map and evaluation distribution. Compare it to the prior sampling setup using the same per-class metrics, since sampling can conceal minority-class regressions.
> - Verify no split overlap/duplicates or train–test preprocessing mismatch; fit preprocessing only on training data.
> - Establish the sampling effect with paired control/candidate runs using identical data order and multiple predeclared seeds, reporting uncertainty rather than one selected run.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — states that sampling can conceal minority-class regressions and
  requires the same per-class metrics for the sampling comparison.
- PASS — rejects accuracy alone and requires per-class and balanced metrics.
- PASS — checks class-map, preprocessing, and split consistency.
- PASS — requires identical data order, multiple predeclared seeds, and repeated
  paired comparisons.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Primary repetition 5

#### Case

Primary prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_primary_5`

#### Observed response

> The experiment is not valid for a reliable model-quality claim.
>
> - Tuning the confidence threshold on the test set leaks test information and biases the reported result. Choose thresholds using a held-out validation set, then evaluate once on the untouched test set.
> - Overall accuracy is inadequate for a highly imbalanced classifier; it can look strong while minority classes fail. Report per-class precision, recall, and F1, plus balanced accuracy (and appropriate aggregate metrics such as macro-F1).
> - Changing class sampling changes the training distribution and can materially alter class-wise behavior. Keep the class mapping and test/evaluation distribution fixed, document the sampling change, and compare per-class metrics against the prior sampling setup at the same review point.
> - For a defensible comparison, hold all other settings fixed; pair control and changed-sampling runs with identical data order per seed, repeat across predeclared seeds, and report uncertainty or a statistical comparison.
> - If confidence scores are used operationally, assess calibration—potentially per class—on validation data as well.

#### Rubric

- PASS — identifies test-set threshold tuning as leakage.
- PASS — states that sampling can materially alter class-wise behavior and
  requires per-class comparison in the same review point.
- PASS — rejects accuracy alone and requires per-class and balanced metrics.
- PASS — checks class mapping and calibration.
- PASS — requires identical data order, multiple predeclared seeds, and repeated
  controlled comparisons.
- PASS — does not load the AI Infra or LLM Profile.

#### Verdict

PASS — 6/6.

### Counter-example repetition 1

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_counter_1`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure kernel-latency benchmark with no model-quality change.
>
> For p99 latency, verify warm-up is excluded, synchronization correctly brackets timing, input shapes/dtypes/layouts are fixed and representative, clocks and GPU contention are controlled, and enough repeated measurements are collected to estimate the tail reliably. Report the percentile method, sample count, hardware/software versions, and distribution alongside p50/p99. Compare against a fixed baseline under identical conditions, preferably across multiple independent benchmark runs.

#### Rubric

- PASS — explicitly makes the AI Infrastructure Profile primary and excludes
  the ML Research Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3.

### Counter-example repetition 2

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_counter_2`

#### Observed response

> AI Infrastructure Profile is primary; the ML Research Profile does not apply.
>
> For p99 latency, use many steady-state kernel invocations after warmup, synchronize the CUDA stream around timing boundaries, and measure with CUDA events rather than host wall-clock time. Report the full sample count, p50/p95/p99, units, GPU/model/driver/Triton versions, clock/power settings, and whether inputs, shapes, strides, and cache conditions match production. Exclude compilation and first-run effects, avoid accidental synchronization or allocation in the timed region, and repeat the benchmark across independent runs to show p99 stability.

#### Rubric

- PASS — explicitly makes the AI Infrastructure Profile primary and excludes
  the ML Research Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3.

### Counter-example repetition 3

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_counter_3`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure kernel-latency measurement with no model-quality change.
>
> For p99, verify a warm-up phase excluded from results, enough timed iterations to make the tail estimate stable, synchronization around timing, consistent input shapes/dtypes/layouts, and isolated GPU conditions. Report the latency distribution alongside p50/p90/p99, hardware/software versions, clock/power settings, and whether measurements include launch overhead, transfers, or only kernel execution.

#### Rubric

- PASS — explicitly makes the AI Infrastructure Profile primary and excludes
  the ML Research Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3.

### Counter-example repetition 4

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_counter_4`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure kernel-performance measurement with no model-quality change.
>
> For a credible p99 latency result, verify warm-up is excluded, GPU work is explicitly synchronized before timing, and timings use a suitable GPU-event clock. Measure enough independent iterations to stabilize the tail, report the exact percentile method and sample count, and avoid batching effects that conceal per-call latency. Hold GPU model, clocks/power state, driver/CUDA/Triton versions, input shapes, memory layout, and competing workloads fixed. Compare against a control under the same conditions, repeat runs, and report p50/p90/p99 plus run-to-run variation—not only a single p99.

#### Rubric

- PASS — explicitly makes the AI Infrastructure Profile primary and excludes
  the ML Research Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3.

### Counter-example repetition 5

#### Case

Counter-example prompt.

#### Context

Fresh with-Skill context. Agent:
`/root/task_16_implementer/t16_review_counter_5`

#### Observed response

> The AI Infrastructure Profile is primary; the ML Research Profile does not apply because this is a pure kernel-latency benchmark with no model-quality change.
>
> For a credible p99 measurement, verify warm-up is excluded, synchronize CUDA around timing, use sufficient repetitions, report the latency distribution and sample count, and keep GPU, clocks/power settings, input shapes, dtypes, strides, and competing workload fixed. Compare against a clear baseline under the identical harness, and repeat across runs to show p99 stability.

#### Rubric

- PASS — explicitly makes the AI Infrastructure Profile primary and excludes
  the ML Research Profile.
- PASS — does not apply ML-specific checks.
- PASS — avoids irrelevant ML ceremony.

#### Verdict

PASS — 3/3.

## Final aggregate

- Final primary per repetition: 6/6, 6/6, 6/6, 6/6, 6/6 = 30/30.
- Final counter-example per repetition: 3/3, 3/3, 3/3, 3/3, 3/3 =
  15/15.
- Final total: 45/45.
- Complete final passes: primary 5/5; counter-example 5/5.
- All earlier failed regressions and superseded responses remain verbatim.
- Contamination, interruption, timeout, or replacement samples: none.
- GREEN is established only by iteration 4 after the review-driven Skill edit.
