# Applying ML Research Profile — Baseline Results

Five fresh evaluators answered each prompt without the Skill. The evaluators
received one prompt, no rubric or expected answer, and no access to tools,
files, the workspace, browsing, or delegation. All responses are verbatim.

## Primary repetition 1

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_primary_1`

### Observed response

> The experiment is not valid as reported.
>
> - Tuning the confidence threshold on the test set leaks test information and inflates performance. Use a validation set (or nested cross-validation) to choose the threshold, then evaluate once on a held-out test set.
> - Changing class sampling is acceptable if it is applied only to training data. Keep validation/test distributions untouched unless you explicitly define a balanced evaluation set alongside a natural-distribution test set.
> - Overall accuracy is misleading under heavy imbalance; a majority-class predictor can score highly. Report per-class precision, recall, F1, confusion matrix, balanced accuracy, and preferably PR-AUC/ROC-AUC where appropriate.
> - State the positive-class prevalence and selection criterion for the operating threshold, such as recall at a target precision or expected cost.
>
> Re-run with a fixed, untouched test set and report uncertainty (e.g., bootstrap confidence intervals) if the dataset is modest.

### Rubric

- PASS — explicitly identifies threshold tuning on the test set as leakage.
- FAIL — discusses sampling and per-class metrics separately, but does not state
  that sampling changes require inspecting the resulting per-class behavior.
- PASS — rejects overall accuracy alone and requires per-class metrics.
- FAIL — does not check calibration, class-map drift, or preprocessing
  consistency.
- FAIL — does not require controlled seeds, controlled data order, and repeated
  runs for the quality claim.
- PASS — does not load the AI Infra or LLM Profile.

### Verdict

FAIL — 3/6 blocking groups passed.

## Primary repetition 2

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_primary_2`

### Observed response

> The experiment is not valid as reported.
>
> - Do not tune the confidence threshold on the test set; that leaks test information and inflates results. Tune it on a validation set (or via cross-validation), then evaluate once on a held-out test set.
> - Changing class sampling is acceptable if applied only during training, but document the sampling strategy and evaluate on the original, naturally imbalanced test distribution.
> - Overall accuracy is misleading under severe imbalance. Report per-class precision, recall, F1, balanced accuracy, confusion matrix, and preferably PR-AUC / ROC-AUC where appropriate.
> - Include calibration assessment if confidence thresholds drive decisions, and state the operating threshold chosen from validation criteria.

### Rubric

- PASS — explicitly identifies threshold tuning on the test set as leakage.
- FAIL — discusses sampling and per-class metrics separately, but does not state
  that sampling changes require inspecting the resulting per-class behavior.
- PASS — rejects overall accuracy alone and requires per-class metrics.
- PASS — explicitly requires calibration assessment.
- FAIL — does not require controlled seeds, controlled data order, and repeated
  runs for the quality claim.
- PASS — does not load the AI Infra or LLM Profile.

### Verdict

FAIL — 4/6 blocking groups passed.

## Primary repetition 3

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_primary_3`

### Observed response

> The experiment is not valid as reported.
>
> - Do not tune the confidence threshold on the test set; that leaks test information and makes performance optimistic. Tune it on a validation set (or via cross-validation), then evaluate once on a held-out test set.
> - Changing class sampling is acceptable, but document the method and ensure train/validation/test splits retain representative, untouched distributions. Apply sampling only to training data.
> - Overall accuracy is misleading under heavy imbalance. Report class-wise precision, recall, F1, confusion matrix, balanced accuracy, and preferably PR-AUC; select metrics based on the cost of false positives versus false negatives.
> - Include confidence intervals or repeated runs if possible, and compare against simple baselines such as majority-class prediction.

### Rubric

- PASS — explicitly identifies threshold tuning on the test set as leakage.
- FAIL — discusses sampling and per-class metrics separately, but does not state
  that sampling changes require inspecting the resulting per-class behavior.
- PASS — rejects overall accuracy alone and requires per-class metrics.
- FAIL — does not check calibration, class-map drift, or preprocessing
  consistency.
- FAIL — mentions optional repeated runs but not controlled seeds and data order;
  the full blocking group is not satisfied.
- PASS — does not load the AI Infra or LLM Profile.

### Verdict

FAIL — 3/6 blocking groups passed.

## Primary repetition 4

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_primary_4`

### Observed response

> The experiment is not valid as reported.
>
> - Tuning the confidence threshold on the test set leaks test information and biases performance upward. Use a validation set (or nested cross-validation) for threshold selection, then evaluate once on a held-out test set.
> - Changing class sampling is reasonable, but it must be specified and applied only to training data. Keep validation/test sets representative of the real deployment distribution.
> - Overall accuracy is misleading under strong imbalance; a trivial majority-class model may score well. Report per-class precision, recall, F1, balanced accuracy, confusion matrix, and ideally PR-AUC (plus ROC-AUC where appropriate).
> - State the target operating point and its trade-off—for example, recall at a fixed precision or false-positive rate—and include uncertainty such as confidence intervals.

### Rubric

- PASS — explicitly identifies threshold tuning on the test set as leakage.
- FAIL — discusses sampling and per-class metrics separately, but does not state
  that sampling changes require inspecting the resulting per-class behavior.
- PASS — rejects overall accuracy alone and requires per-class metrics.
- FAIL — does not check calibration, class-map drift, or preprocessing
  consistency.
- FAIL — does not require controlled seeds, controlled data order, and repeated
  runs for the quality claim.
- PASS — does not load the AI Infra or LLM Profile.

### Verdict

FAIL — 3/6 blocking groups passed.

## Primary repetition 5

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_primary_5`

### Observed response

> The experiment is not valid as reported.
>
> - Do not tune the confidence threshold on the test set; this leaks test information and makes performance optimistic. Use a validation set (or cross-validation) for threshold selection, then evaluate once on an untouched test set.
> - Class sampling changes the training distribution. It can be appropriate, but document the method and assess its effects per class; consider class weights, oversampling, or undersampling as controlled comparisons.
> - Overall accuracy is misleading under strong imbalance. Report per-class precision, recall, and F1; macro/weighted F1; confusion matrix; balanced accuracy; and, where relevant, PR-AUC and ROC-AUC. For rare positive detection, precision-recall metrics and recall at a chosen precision are often most informative.
> - Ensure any preprocessing, sampling, and threshold selection occur within each training/validation split to avoid leakage.
>
> A sound setup: split train/validation/test stratified by class; tune sampling and threshold using train/validation only; lock choices; then report the full metric suite on the held-out test set, with confidence intervals if feasible.

### Rubric

- PASS — explicitly identifies threshold tuning on the test set as leakage.
- PASS — explicitly requires assessing the effects of sampling changes per class.
- PASS — rejects overall accuracy alone and requires per-class metrics.
- PASS — explicitly checks preprocessing consistency within the splits.
- FAIL — does not require controlled seeds, controlled data order, and repeated
  runs for the quality claim.
- PASS — does not load the AI Infra or LLM Profile.

### Verdict

FAIL — 5/6 blocking groups passed.

## Counter-example repetition 1

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_counter_1`

### Observed response

> For a Triton kernel with unchanged model quality, review p99 latency by ensuring:
>
> - Measure end-to-end kernel timing with sufficient warm-up iterations and many repeated runs.
> - Report hardware, CUDA/Triton/PyTorch versions, tensor shapes, dtypes, layouts, and launch configuration.
> - Compare p50, p95, p99, mean, and max—not p99 alone.
> - Check for synchronization mistakes; use GPU events or the project’s benchmark harness, not unsynchronized host timing.
> - Separate compile/JIT and first-run overhead from steady-state latency.
> - Control clock/power state, contention, batch size, and memory allocator effects.
> - Verify p99 across multiple independent benchmark runs; report variance/confidence intervals.
> - Confirm no rare-path regressions such as spills, occupancy drops, cache sensitivity, or input-shape outliers.
> - Include a baseline and percentage change, with a threshold for acceptable regression.

### Rubric

- FAIL — gives appropriate systems checks but never identifies the AI Infra
  Profile as primary or states that the ML Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 2

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_counter_2`

### Observed response

> Review p99 latency across a representative workload distribution, with warm-up excluded and enough repetitions to stabilize tail estimates. Compare baseline and candidate under identical hardware, clock/power settings, batch shapes, concurrency, and cache state.
>
> Report median, p95, p99, throughput, and variance—not just p99—plus per-shape results to catch regressions hidden by aggregation. Confirm statistical significance with confidence intervals or repeated-run comparisons, and investigate outliers using profiling/tracing to distinguish kernel effects from scheduling, memory pressure, compilation, or host-side overhead.
>
> With no quality change, accept only if the p99 improvement is repeatable and no important workload slice regresses beyond the agreed guardrail.

### Rubric

- FAIL — gives appropriate systems checks but never identifies the AI Infra
  Profile as primary or states that the ML Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 3

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_counter_3`

### Observed response

> Validate p99 using enough warm, steady-state samples (ideally thousands), separating compile/warm-up from timed iterations. Report median, p95, p99, sample count, batch/sequence shape, GPU/model, clocks/power settings, Triton/PyTorch/CUDA versions, and synchronization method.
>
> For GPU kernels, time with CUDA events and synchronize before reading results; avoid host-side timers alone. Compare against the baseline under identical inputs, stream usage, memory state, and clock conditions. Repeat independent runs and report variability or confidence intervals.
>
> “No model-quality change” should be confirmed separately with output equivalence/tolerance tests; it does not validate the latency result. A p99 improvement is credible only if tail samples are stable and any regressions in throughput, memory use, or end-to-end latency are also checked.

### Rubric

- FAIL — gives appropriate systems checks but never identifies the AI Infra
  Profile as primary or states that the ML Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations;
  repeated latency trials are relevant systems checks.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 4

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_counter_4`

### Observed response

> For a Triton kernel with unchanged model quality, p99 latency should be measured as an end-to-end kernel timing distribution under realistic, steady-state conditions—not as a single benchmark average.
>
> Key checks:
>
> - Use many iterations (typically thousands), with warm-up runs excluded.
> - Synchronize GPU timing correctly: CUDA events or explicit synchronization around the measured region; asynchronous launches otherwise underreport time.
> - Report p50/p95/p99 plus sample count, batch/shape, dtype, hardware, driver/CUDA/Triton versions, and clock/power settings.
> - Fix or explicitly vary input shapes and memory layouts; p99 can be dominated by dynamic-shape or allocation effects.
> - Preallocate buffers and avoid including compilation, autotuning, initialization, host-side data preparation, or unrelated synchronization unless the production SLA includes them.
> - Run under representative concurrency and co-tenancy. An isolated p99 only establishes best-case kernel behavior.
> - Use repeated benchmark trials and compare confidence/variation; one p99 estimate can be noisy.
> - Verify correctness separately with numerical tolerance tests, even if model-quality metrics are unchanged—latency gains from altered precision, masking, or indexing can still create localized errors.
>
> For comparison, use the same harness and workload before/after, then report p99 delta in milliseconds and percent. A credible conclusion is: “p99 improved from X ms to Y ms under identical workload and environment; correctness tests passed with defined tolerances.”

### Rubric

- FAIL — gives appropriate systems checks but never identifies the AI Infra
  Profile as primary or states that the ML Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations;
  repeated latency trials are relevant systems checks.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 5

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_16_implementer/t16_ctrl_counter_5`

### Observed response

> For a Triton kernel with unchanged model quality, validate p99 latency as a performance measurement problem:
>
> - Benchmark end-to-end and kernel-only separately; report which one changed.
> - Use identical shapes, dtypes, batch sizes, hardware, clocks/power settings, driver/CUDA/Triton versions, and concurrency.
> - Include warm-up iterations; exclude compilation, autotuning, cache population, and first-use effects.
> - Collect enough samples across multiple independent runs. Report p50, p90, p99, mean, sample count, and confidence intervals or run-to-run variance.
> - Synchronize correctly around GPU timing; avoid CPU-side async timing artifacts. Prefer CUDA events for kernel timing.
> - Randomize or interleave baseline and candidate runs to reduce thermal/load drift; monitor GPU clocks, temperature, and contention.
> - Inspect the full latency distribution and outliers. A p99 regression may reflect occasional autotune fallback, memory allocation, synchronization, page faults, or queueing rather than steady-state kernel execution.
> - Confirm that any latency improvement does not trade off memory use, errors, numerical stability, or throughput at the intended load.
>
> Treat a p99 difference as credible only if it exceeds observed run-to-run noise and persists across repeated, controlled runs.

### Rubric

- FAIL — gives appropriate systems checks but never identifies the AI Infra
  Profile as primary or states that the ML Profile does not apply.
- PASS — does not apply per-class metrics, calibration, or data-split leakage.
- PASS — avoids class balancing, ML seed control, and model-quality ablations;
  repeated latency trials are relevant systems checks.

### Verdict

FAIL — 2/3 blocking groups passed.

## Aggregate

- Primary per repetition: 3/6, 4/6, 3/6, 3/6, 5/6 = 18/30.
- Counter-example per repetition: 2/3, 2/3, 2/3, 2/3, 2/3 = 10/15.
- Total: 28/45.
- Complete passes: primary 0/5; counter-example 0/5.
- Exclusions or replacements: none.
- RED established: controls consistently missed seed/data-order/repeated-run
  control, often missed sampling effects or calibration/data consistency, and
  never routed the pure Triton benchmark to the AI Infra Profile.
