---
name: verifying-research-evidence
description: Use when about to claim research code is complete, an experiment finished, a performance result improved, a negative result is valid, or a hypothesis is supported
---

# Verifying Research Evidence

Require fresh, claim-matched evidence before making a completion or scientific
claim. Never promote evidence from one level into another.

## Return this evidence contract

Use exactly one status from `verified | not_verified | failed | inconclusive`
for each independent verdict:

- **Code verification:** whether current deterministic tests, invariants, smoke
  checks, or reviews support only the implementation scope they exercised.
- **Experiment execution:** whether the predeclared experiment, including all
  required seeds and repetitions, completed as designed.
- **Conclusion support:** whether completed controlled evidence supports the
  stated scientific claim.

Then list:

- **Primary evidence:** exact commands and fresh outputs, run IDs, artifacts,
  and independent reviews that are actually available. Write `not supplied`
  for absent references; never invent one.
- **Missing evidence:** every unrun seed, repetition, baseline, ablation,
  guardrail, uncertainty estimate, or review required by the claim.
- **Remaining risks:** plausible ways the available evidence could mislead.
- **Calibrated final wording:** state only what the verdicts support.

## Assign statuses

| Status | Meaning |
|---|---|
| `verified` | Fresh direct evidence satisfies the claim's declared checks. |
| `not_verified` | Required evidence was not run, is stale, or is unavailable. |
| `failed` | A check failed, or valid completed evidence does not support the tested claim. |
| `inconclusive` | Evidence is completed but underpowered, conflicting, or too uncertain to decide. |

Treat a credible current report that all unit tests pass as possible
`verified` code evidence for the tested scope only; identify missing
commands/output references. Unit tests do not prove convergence, experiment
completion, or method effectiveness. One completed seed is a pilot: remaining
seeds make experiment execution `not_verified` or `inconclusive`, and the
conclusion cannot be `verified`.

A valid negative result is a completed valid experiment whose positive
hypothesis is not supported. Mark experiment execution `verified` and the
positive conclusion `failed`; do not call it a code failure.

## Respect cost without changing truth

When further evidence exceeds the authorized budget, stop. Narrow the claim or
return `not_verified`/`inconclusive`; list the unaffordable evidence as missing.
Never substitute a smoke test, unit suite, or favorable seed for it.

Example final wording: “Implementation checks passed for their tested scope.
One seed is promising, but the remaining repetitions were not run; the
experiment and superiority conclusion are not verified, so the method cannot
yet be called better.”

## Common mistakes

- Do not merge implementation, execution, and conclusion into one verdict.
- Do not turn planned commands or repetitions into evidence.
- Do not call a method better from one seed, even when more runs are costly.
