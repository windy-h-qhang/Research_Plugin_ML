---
name: validating-research-code
description: Use when selecting tests or evidence for PyTorch, LLM, or AI infrastructure changes, especially when training outcomes are stochastic, costly, or represented by only a short run
---

# Validating Research Code

Never promote evidence from one layer into another. A passing lower layer does
not verify a higher layer.

## Build the validation matrix

Report every layer with `Evidence`, `Next check`, and `Status`. Use `Verified`,
`Not verified`, or `Not applicable` with a reason. A planned test is not
evidence. Mark every omitted relevant layer `Not verified`. If evidence lacks
any required qualification, its status must remain `Not verified`; never mark
it `Verified` while listing the qualifying test under `Next check`.

| Layer | Required evidence |
|---|---|
| 1. Deterministic | Test-first checks for deterministic modules and confirmed bug regressions. For a PyTorch loss, use hand-computed or trusted-reference values and gradients; cover reduction, masks, weights, empty/degenerate inputs, and declared tolerances. |
| 2. Invariants | Check shape, dtype, device, finite values, numerical tolerance, gradient flow, frozen parameters, and optimizer boundaries. For accumulation, compare the same examples as one effective batch versus microbatches: normalized loss, parameter gradients/updates, step count, and `zero_grad` timing must agree within tolerance. Add AMP, checkpoint, rank, sharding, collective, or kernel invariants when relevant. |
| 3. Smoke Test | Run tiny fixed data with a named fixed seed and an explicit step/time/resource bound. Exercise the relevant train/eval/save/resume or service path. This verifies execution viability only—not correctness, performance, stability, or method effectiveness. |
| 4. Regression or benchmark | Require a correctness regression against the previous/reference behavior. For performance claims, use a controlled benchmark with fixed inputs/configuration, warm-up, synchronization, repeated measurements, and predeclared thresholds for latency, throughput, or memory. |
| 5. Conclusion | Require a controlled baseline, multiple predeclared seeds, contribution-isolating ablations, primary and guardrail metrics, and uncertainty or an appropriate statistical comparison. |

## State separate verdicts

Conclude with:

- **Code correctness:** supported only by applicable deterministic, invariant,
  and regression evidence.
- **Execution viability:** supported only by the bounded Smoke Test.
- **Method conclusion:** supported only by layer 5 evidence.

Do not call a method validated from unit tests, invariants, one seed, one short
run, or a Smoke Test. If a full experiment is out of scope, explicitly state
that regression/benchmark and conclusion layers remain `Not verified`.

## Common mistakes

- Do not make full training convergence a unit test.
- Do not replace controlled regression evidence with “it ran.”
- Do not turn absent multi-seed, ablation, or statistical evidence into a
  positive conclusion.
