# Validating Research Code — Skilled Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each received the complete target Skill followed by the exact
case prompt and was prohibited from tools, delegation, or workspace access.
No evaluator received the rubric or an expected answer. Responses are
preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_skilled_1`.

### Observed response

The method is **not validated**. One successful 20-step run only supports limited execution viability, and only if it used fixed data, a named seed, and explicit resource bounds.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None provided. | Add loss tests against hand-computed/reference values and gradients; cover reductions, masks/weights, empty inputs, degenerate inputs, and tolerances. | Not verified |
| Invariants | None provided. | Verify shape, dtype, device, finite outputs, gradient flow, frozen parameters, and optimizer boundaries. Compare one effective batch against equivalent microbatches: normalized loss, gradients/updates, optimizer step count, and `zero_grad` timing must match within tolerance. | Not verified |
| Smoke test | One 20-step run succeeded. | Re-run on tiny fixed data with a named fixed seed and explicit step/time/resource limit; exercise train, evaluation, checkpoint save, and resume. | Not verified — the run details needed to qualify it are absent |
| Regression / benchmark | None provided. | Add a correctness regression versus prior accumulation behavior or a trusted reference. If claiming performance, run a controlled repeated benchmark with predefined thresholds. | Not verified |
| Conclusion | No controlled baseline, multiple predeclared seeds, ablations, guardrail metrics, or uncertainty analysis. | Full experiment is intentionally out of scope. | Not verified |

Separate verdicts:

- **Code correctness:** not verified; deterministic, invariant, and regression evidence are still needed.
- **Execution viability:** partially suggested by the 20-step run, but not verified under a bounded fixed-seed smoke-test protocol.
- **Method conclusion:** not validated. Unit tests, accumulation equivalence checks, and a short successful run cannot establish method effectiveness.

### Rubric

- PASS — specifies hand-computed/reference loss values and gradients with strict edge coverage and tolerances.
- PASS — specifies accumulation equivalence for normalized loss, gradients/updates, step count, and `zero_grad`.
- PASS — specifies shape, dtype, device, finite-value, gradient-flow, and optimizer invariants.
- PASS — specifies tiny fixed data, a named fixed seed, and explicit step/time/resource bounds.
- PASS — limits Smoke evidence to execution viability.
- PASS — marks correctness-regression or controlled-benchmark evidence missing.
- PASS — marks controlled baseline, multi-seed, ablation, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers have an explicit `Not verified` status.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_skilled_2`.

### Observed response

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | One 20-step run is not deterministic evidence. | Unit-test the new loss against hand-computed/reference values and gradients; cover reductions, masks/weights, empty or degenerate inputs, and tolerance boundaries. | Not verified |
| Invariants | None reported. | Test loss/output shapes, dtype/device, finite values, gradient flow, frozen parameters, and optimizer boundaries. Compare one effective batch with equivalent microbatches: normalized loss, gradients/updates, optimizer-step count, and `zero_grad` timing must match within tolerance. Include AMP/distributed/checkpoint invariants if used. | Not verified |
| Smoke test | One successful 20-step run demonstrates limited execution viability, but seed and bounds were not specified. | Repeat as a tiny fixed-data run with a named fixed seed and explicit 20-step/time/resource bounds; exercise train, eval, save, and resume if those paths changed. | Not verified |
| Regression / benchmark | None reported. | Add a correctness regression against prior/reference behavior. If claiming efficiency from changed accumulation, benchmark controlled fixed inputs with warm-up, synchronization, repeated measurements, and predeclared latency/throughput/memory thresholds. | Not verified |
| Conclusion | A single short run cannot establish a method conclusion. | Full experiment would require a controlled baseline, predeclared multiple seeds, ablations isolating the loss and accumulation changes, primary and guardrail metrics, and uncertainty/statistical comparison. | Not verified |

**Code correctness:** not verified until deterministic loss tests, accumulation invariants, and relevant regression checks pass.

**Execution viability:** partially suggested by the 20-step run, but not verified as stated because its seed and explicit bound/path coverage are unspecified.

**Method conclusion:** not validated. Unit tests and a smoke run can establish implementation behavior and viability, not whether the new method improves outcomes.

### Rubric

- PASS — specifies hand-computed/reference values and gradients with edge cases and tolerance boundaries.
- PASS — specifies accumulation equivalence including normalization, gradients/updates, step count, and `zero_grad`.
- PASS — specifies tensor, device, finite-value, gradient, optimizer, AMP, distributed, and checkpoint invariants as relevant.
- PASS — specifies tiny fixed data, a named fixed seed, and explicit 20-step/time/resource bounds.
- PASS — limits Smoke evidence to execution viability.
- PASS — marks correctness regression and any controlled performance benchmark missing.
- PASS — marks controlled baseline, multiple seeds, ablations, metrics, and uncertainty/statistics missing.
- PASS — explicitly says the method conclusion is not validated.
- PASS — all five layers have an explicit `Not verified` status.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_skilled_3`.

### Observed response

The method is **not validated**. One successful 20-step run only provides limited execution evidence—not correctness, performance, stability, or effectiveness.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None provided | Add hand-computed/reference tests for the new loss: values and gradients; reductions, masks/weights, empty/degenerate inputs, and tolerances. | Not verified |
| Invariants | None provided | Test finite loss/gradients, shape/dtype/device, gradient flow, frozen parameters, optimizer boundaries. Compare identical effective batches with and without microbatch accumulation: normalized loss, gradients/updates, optimizer step count, and `zero_grad` timing must match within tolerance. | Not verified |
| Smoke test | One successful 20-step run | Repeat as a bounded fixed-seed smoke test that exercises train/eval and save/resume where applicable. | Not verified — seed/bounds/path coverage are unspecified |
| Regression or benchmark | None provided | Add a correctness regression against the prior accumulation behavior/reference implementation. Benchmark only if making performance or memory claims. | Not verified |
| Conclusion | One short run; no controlled baseline, seeds, ablations, or uncertainty | Out of scope per request. | Not verified |

Separate verdicts:

- **Code correctness:** not verified until deterministic and accumulation-invariant tests pass.
- **Execution viability:** partially indicated by the run, but not verified as a defined fixed-seed bounded smoke test.
- **Method conclusion:** not validated. A full experiment would require controlled baselines, multiple predeclared seeds, ablations, guardrails, and uncertainty/statistical comparison.

### Rubric

- PASS — specifies reference loss values and gradients with reductions, masks/weights, edge cases, and tolerances.
- PASS — specifies effective-batch/microbatch equivalence for normalization, gradients/updates, step count, and `zero_grad`.
- PASS — specifies finite, tensor, device, gradient, and optimizer invariants.
- PASS — specifies a bounded fixed-seed Smoke Test over the relevant paths.
- PASS — explicitly limits the existing run to execution evidence.
- PASS — marks correctness regression or benchmark evidence missing.
- PASS — marks controlled baselines, multiple seeds, ablations, guardrails, and statistical/uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers have an explicit `Not verified` status.

### Verdict

PASS — 9/9 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_skilled_4`.

### Observed response

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None reported. | Test the loss against hand-computed/reference values and gradients; include reductions, masks/weights, empty inputs, and tolerances. | Not verified |
| Invariants | None reported. | Verify shapes, dtypes, devices, finite values, gradient flow, frozen parameters, and optimizer boundaries. Compare one effective batch against equivalent microbatches for normalized loss, gradients/updates, optimizer-step count, and `zero_grad` timing. | Not verified |
| Smoke test | One successful 20-step run. | Repeat on tiny fixed data with a named fixed seed and explicit resource/time bound; include train/eval and save/resume if affected. | Verified — execution viability only |
| Regression / benchmark | None reported. | Add a correctness regression against prior/reference behavior. If claiming speed or memory improvements, run a controlled repeated benchmark with predeclared thresholds. | Not verified |
| Conclusion | One short run; no controlled baseline, multi-seed results, ablations, or uncertainty analysis. | Run a scoped experiment with predeclared seeds, baseline, primary/guardrail metrics, and an ablation isolating the loss and accumulation changes. | Not verified |

**Code correctness:** not verified.
**Execution viability:** supported only for the exercised 20-step path.
**Method conclusion:** not validated. A successful short run shows that it can execute; it does not establish that the new loss or accumulation change improves—or even preserves—training behavior.

### Rubric

- PASS — specifies hand-computed/reference loss values and gradients with relevant edge cases and tolerances.
- PASS — specifies accumulation equivalence for normalized loss, gradients/updates, step count, and `zero_grad`.
- PASS — specifies shape, dtype, device, finite, gradient-flow, frozen-parameter, and optimizer invariants.
- FAIL — proposes a future bounded fixed-seed rerun but incorrectly marks the
  existing run `Verified` despite its missing seed and bound.
- PASS — labels the Smoke evidence “execution viability only.”
- PASS — marks correctness regression or any controlled performance benchmark missing.
- PASS — marks controlled baseline, multi-seed, ablation, metrics, and uncertainty evidence missing.
- PASS — explicitly says the method conclusion is not validated.
- FAIL — the missing Smoke qualifications make that layer omitted evidence, but
  it is marked `Verified` rather than `Not verified`.

### Verdict

FAIL — 7/9 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_skilled_5`.

### Observed response

The 20-step run supports only execution viability, not method validation.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | One successful run is not deterministic evidence. | Add loss tests with hand-computed/reference outputs and gradients; cover reductions, masks/weights, empty inputs, degenerate inputs, and tolerances. | Not verified |
| Invariants | None reported. | Verify loss/gradients are finite; shape, dtype, and device handling; gradient flow; frozen parameters; optimizer boundaries. Compare one effective batch with equivalent microbatches: normalized loss, gradients/updates, optimizer step count, and `zero_grad` timing must match within tolerance. Include AMP/distributed invariants if used. | Not verified |
| Smoke test | One 20-step run succeeded, but seed and bounds were not specified. | Repeat on tiny fixed data with a named seed and explicit 20-step/time/resource bound; exercise train, eval, checkpoint save, and resume. | Not verified |
| Regression / benchmark | None reported. | Add a correctness regression against the prior accumulation behavior/reference implementation. If claiming performance effects, run a controlled repeated benchmark with warm-up, synchronization, and predeclared thresholds. | Not verified |
| Conclusion | One short run only. | A controlled baseline, predeclared multiple seeds, ablations isolating the loss vs. accumulation change, primary and guardrail metrics, and uncertainty/statistical comparison. | Not verified |

Separate verdicts:

- **Code correctness:** not verified until deterministic loss tests, accumulation-equivalence invariants, and a reference regression pass.
- **Execution viability:** partially supported by the reported 20-step run; verified only after a bounded, fixed-seed smoke test that includes save/resume.
- **Method conclusion:** not validated. A unit suite and smoke test can establish implementation confidence, but cannot establish that the new loss or accumulation change improves the method.

### Rubric

- PASS — specifies hand-computed/reference loss outputs and gradients with edge cases and tolerances.
- PASS — specifies effective-batch/microbatch equivalence for normalization, gradients/updates, step count, and `zero_grad`.
- PASS — specifies finite, tensor, device, gradient, optimizer, AMP, and distributed invariants as relevant.
- PASS — specifies tiny fixed data, a named seed, and explicit 20-step/time/resource bounds.
- PASS — explicitly limits the reported run to execution viability.
- PASS — marks correctness regression or any controlled performance benchmark missing.
- PASS — marks controlled baseline, multiple seeds, ablations, metrics, and uncertainty/statistics missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers have an explicit `Not verified` status.

### Verdict

PASS — 9/9 blocking items pass.

## Initial skilled-arm aggregate

- Four of five initial skilled repetitions pass all nine blocking items:
  `43/45`.
- Repetition 4 is a blocking failure: it lists a bounded fixed-seed rerun as a
  future check while marking the unqualified existing Smoke run `Verified`.
- No evaluator was excluded and no replacement run was required.
- A post-edit arm is required after the Skill explicitly prevents a planned
  qualification from becoming present evidence.

## Post-edit repetition 1

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_postedit_1`. This fresh
evaluator received the revised Skill.

### Observed response

No—the method is **not validated** by one successful 20-step run.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None provided. | Unit-test the loss against hand-computed/reference values and gradients; cover reductions, masks/weights, empty or degenerate inputs, and tolerances. | Not verified |
| Invariants | None provided. | Verify loss/output shapes, dtype/device, finite values, gradients, frozen parameters, and optimizer boundaries. Compare equivalent effective batches: one full batch vs. accumulation microbatches, checking normalized loss, gradients/updates, optimizer step count, and `zero_grad` timing. Include AMP/distributed invariants if used. | Not verified |
| Smoke test | One 20-step successful run; seed, bounds, and paths exercised are unspecified. | Run a tiny fixed dataset with a named fixed seed and explicit 20-step/resource bound; exercise train, evaluation, checkpoint save, and resume as relevant. | Not verified |
| Regression / benchmark | None provided. | Add a correctness regression against prior/reference behavior. If claiming performance effects, run a controlled repeated benchmark with warm-up, synchronization, and predeclared thresholds. | Not verified |
| Conclusion | No baseline, multi-seed comparison, ablations, guardrails, or uncertainty analysis. | A controlled experiment with predeclared multiple seeds, baseline, loss/accumulation ablations, primary and guardrail metrics, and uncertainty comparison. | Not verified |

Separate verdicts:

- **Code correctness:** Not verified until the deterministic, invariant, and regression checks pass.
- **Execution viability:** Not verified as described; the 20-step run becomes a smoke-test result only if it is fixed-seed and bounded with the relevant paths exercised.
- **Method conclusion:** Not verified. Do not infer effectiveness from unit tests, accumulation equivalence, or a short successful run.

### Rubric

- PASS — specifies strict hand-computed/reference loss and gradient tests with edge cases and tolerances.
- PASS — specifies full-batch/microbatch equivalence for loss, gradients/updates, step count, and `zero_grad`.
- PASS — specifies shape, dtype, device, finite, gradient, optimizer, AMP, and distributed invariants.
- PASS — specifies tiny fixed data, named fixed seed, and explicit step/resource bound.
- PASS — limits Smoke evidence to execution viability.
- PASS — explicitly marks correctness-regression or controlled-benchmark evidence missing.
- PASS — explicitly marks baseline, multi-seed, ablation, guardrail, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers are `Not verified`, including the unqualified Smoke run.

### Verdict

PASS — 9/9 blocking items pass.

## Post-edit repetition 2

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_postedit_2`. This fresh
evaluator received the revised Skill.

### Observed response

Run these tests before treating the code change as correct:

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | One 20-step run is not deterministic evidence. | Unit-test the loss against hand-computed/reference values and gradients; cover reductions, masks/weights, empty or degenerate inputs, and tolerances. | Not verified |
| Invariants | None provided. | Compare identical examples as one effective batch vs. accumulated microbatches: normalized loss, gradients, parameter updates, optimizer-step count, and `zero_grad` timing must match within tolerance. Also check shapes, dtypes, devices, finite values, gradient flow, and frozen parameters. | Not verified |
| Smoke test | A successful 20-step run provides limited execution evidence only if seed, data, and resource/step bounds were fixed and the relevant train/eval/save/resume path ran. | Repeat as a tiny fixed-data, named-seed smoke test with explicit limits. | Not verified |
| Regression or benchmark | None. | Add a correctness regression against the prior/reference accumulation behavior. Benchmark only if making performance claims. | Not verified |
| Conclusion | No controlled baseline, multiple seeds, ablations, metrics, or uncertainty analysis. | Out of scope per request; leave this layer unverified. | Not verified |

**Code correctness:** not supported yet; it needs the deterministic, accumulation-invariant, and regression checks above.

**Execution viability:** one 20-step run suggests it may execute, but is not verified unless it was a bounded, fixed-seed smoke test covering the relevant path.

**Method conclusion:** **not validated**. A short successful run cannot establish that the new loss improves the method.

### Rubric

- PASS — specifies strict hand-computed/reference loss and gradient tests with edge cases and tolerances.
- PASS — specifies full-batch/microbatch equivalence for normalization, gradients/updates, step count, and `zero_grad`.
- PASS — specifies shape, dtype, device, finite, gradient, and frozen-parameter invariants.
- PASS — specifies tiny fixed data, a named seed, and explicit limits.
- PASS — limits the successful run to possible execution evidence only.
- PASS — explicitly marks correctness-regression or benchmark evidence missing.
- PASS — explicitly marks baseline, multi-seed, ablation, metric, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers are `Not verified`, including the unqualified Smoke run.

### Verdict

PASS — 9/9 blocking items pass.

## Post-edit repetition 3

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_postedit_3`. This fresh
evaluator received the revised Skill.

### Observed response

No—the method is not validated. One 20-step run only suggests it may execute; without a named fixed seed and recorded resource/time bound, even smoke-test evidence is incomplete.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None reported. | Add hand-calculated/reference tests for the new loss: values and gradients, reductions, masks/weights, empty or degenerate inputs, and tolerances. Add a regression test for the original behavior where applicable. | Not verified |
| Invariants | None reported. | Test loss/output shapes, dtypes, devices, finite values, gradient flow, frozen parameters, optimizer-step boundaries. Compare identical examples as one effective batch vs. accumulated microbatches: normalized loss, gradients/updates, step count, and `zero_grad` timing must match within tolerance. Include AMP/distributed/checkpoint invariants if used. | Not verified |
| Smoke Test | A successful 20-step run was reported, but seed and explicit resource/time bounds were not. | Run tiny fixed data with a named fixed seed, 20-step bound, and explicit time/resource limit; exercise train, evaluation, save, and resume as relevant. | Not verified |
| Regression or benchmark | None reported. | Run a controlled correctness regression against prior/reference accumulation behavior. Benchmark only if making performance claims. | Not verified |
| Conclusion | No controlled baseline, multi-seed runs, ablations, or uncertainty analysis. | Out of scope per request; leave this layer unverified. | Not verified |

- **Code correctness:** not verified until deterministic, invariant, and regression evidence passes.
- **Execution viability:** not verified from the reported run; it becomes supported after the bounded fixed-seed smoke test.
- **Method conclusion:** not verified. A full experiment is required for that claim, so do not describe the method as validated.

### Rubric

- PASS — specifies strict hand-calculated/reference loss and gradient tests with edge cases and tolerances.
- PASS — specifies full-batch/microbatch equivalence for loss, gradients/updates, step count, and `zero_grad`.
- PASS — specifies tensor, numerical, gradient, optimizer, AMP, distributed, and checkpoint invariants.
- PASS — specifies named fixed seed, 20-step bound, and explicit time/resource limit.
- PASS — says the current run only suggests execution and the qualified Smoke establishes viability.
- PASS — explicitly marks correctness-regression or benchmark evidence missing.
- PASS — explicitly marks controlled baseline, multi-seed, ablation, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers are `Not verified`, including the unqualified Smoke run.

### Verdict

PASS — 9/9 blocking items pass.

## Post-edit repetition 4

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_postedit_4`. This fresh
evaluator received the revised Skill.

### Observed response

A 20-step run shows only that the training path can execute. The method is not validated.

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None provided. | Add unit tests for the new loss against hand-computed/reference values and gradients; cover reductions, masks/weights, empty or degenerate inputs, and tolerances. | Not verified |
| Invariants | None provided. | Check loss/gradient finiteness, shapes, dtypes, devices, gradient flow, frozen parameters, and optimizer boundaries. For accumulation, compare one effective batch with equivalent microbatches: normalized loss, gradients/updates, optimizer step count, and `zero_grad` timing must agree within tolerance. | Not verified |
| Smoke test | One successful 20-step run; seed, bounds, and exercised paths unspecified. | Run tiny fixed data with a named fixed seed and explicit step/time/resource bound, including the relevant train/eval/save/resume path. | Not verified |
| Regression or benchmark | None provided. | Add a correctness regression against prior/reference behavior. If making performance claims, run a controlled repeated benchmark with warm-up and predeclared thresholds. | Not verified |
| Conclusion | No controlled baseline, multiple seeds, ablations, guardrails, or uncertainty analysis. | Out of scope for now; predefine and run a multi-seed baseline/ablation experiment before drawing a method conclusion. | Not verified |

- **Code correctness:** not supported yet.
- **Execution viability:** not verified from the stated run, though it is encouraging.
- **Method conclusion:** not validated.

The efficient scope is loss unit tests plus accumulation-equivalence/invariant tests, then a bounded fixed-seed smoke test. A full experiment is unnecessary for this change, but the regression/benchmark and method-conclusion layers remain not verified.

### Rubric

- PASS — specifies strict hand-computed/reference loss and gradient tests with edge cases and tolerances.
- PASS — specifies accumulation equivalence for normalized loss, gradients/updates, step count, and `zero_grad`.
- PASS — specifies finite, tensor, device, gradient, frozen-parameter, and optimizer invariants.
- PASS — specifies tiny fixed data, named fixed seed, and explicit step/time/resource bound.
- PASS — limits the current run to execution and the qualified Smoke to viability.
- PASS — explicitly marks correctness-regression or controlled-benchmark evidence missing.
- PASS — explicitly marks controlled baseline, multi-seed, ablation, guardrail, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers are `Not verified`, including the unqualified Smoke run.

### Verdict

PASS — 9/9 blocking items pass.

## Post-edit repetition 5

### Case

`tests/behavior/cases/validating-research-code.md`

### Context

Evaluator: `/root/task_12_implementer/validation_postedit_5`. This fresh
evaluator received the revised Skill.

### Observed response

| Layer | Evidence | Next check | Status |
|---|---|---|---|
| Deterministic | None provided. | Add hand-computed/reference tests for the new loss: value and gradients; reductions, masks/weights, empty or degenerate inputs, and declared tolerances. | Not verified |
| Invariants | None provided. | Test accumulation against one equivalent full batch: normalized loss, gradients, parameter updates, optimizer step count, and `zero_grad` timing must match within tolerance. Also check shape, dtype, device, finite values, and gradient flow. Include AMP/distributed invariants if used. | Not verified |
| Smoke Test | One successful 20-step run, but seed and resource bound were not specified. | Run tiny fixed data with a named fixed seed and explicit 20-step/time/resource limit, exercising training plus checkpoint save/resume if affected. | Not verified |
| Regression or benchmark | None provided. | Add a correctness regression against prior/reference behavior. If claiming speed or memory improvement, run a controlled repeated benchmark with warm-up, synchronization, and predeclared thresholds. | Not verified |
| Conclusion | No controlled baseline, multiple seeds, ablations, or uncertainty analysis. | Out of scope for now; retain as unverified. | Not verified |

Necessary tests are the deterministic loss tests and the equivalent-full-batch versus microbatch accumulation test; they are the minimum needed to support code correctness.

**Code correctness:** not verified until those deterministic and invariant checks pass.
**Execution viability:** not verified from the current run alone; a bounded, fixed-seed smoke test is needed.
**Method conclusion:** not validated. One 20-step run, even if successful, cannot establish method effectiveness.

### Rubric

- PASS — specifies strict hand-computed/reference loss and gradient tests with edge cases and tolerances.
- PASS — specifies full-batch/microbatch equivalence for normalization, gradients/updates, step count, and `zero_grad`.
- PASS — specifies tensor, numerical, gradient, AMP, and distributed invariants.
- PASS — specifies tiny fixed data, named fixed seed, and explicit step/time/resource limit.
- PASS — limits the current run to possible execution and the qualified Smoke to viability.
- PASS — explicitly marks correctness-regression or controlled-benchmark evidence missing.
- PASS — explicitly marks controlled baseline, multiple seeds, ablations, and uncertainty evidence missing.
- PASS — explicitly says the method is not validated.
- PASS — all five layers are `Not verified`, including the unqualified Smoke run.

### Verdict

PASS — 9/9 blocking items pass.

## Final aggregate verdict

- The initial skilled arm scored `43/45`; repetition 4 failed two blocking
  items because it promoted an unqualified Smoke run to `Verified`.
- The revised Skill closes that loophole by requiring all qualifications
  before `Verified` and forbidding planned checks from counting as evidence.
- All five fresh post-edit repetitions pass all nine blocking items: `45/45`.
- No post-edit evaluator was excluded and no replacement run was required.
