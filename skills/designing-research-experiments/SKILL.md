---
name: designing-research-experiments
description: Use when testing a machine learning hypothesis, comparing methods, planning ablations, selecting metrics, or interpreting experimental evidence
---

# Designing Research Experiments

## Core rule

Write a falsifiable experiment contract before a formal run. Fill every field
with a concrete value or an explicit `TBD`; do not omit fields.

## Experiment contract

Use this exact shape:

- **Experiment ID:** Stable identifier.
- **Hypothesis:** Name the proposed method, its current comparison method, the
  population, the predicted direction and magnitude, and the conditions of the
  claim.
- **Baselines: []** Name the current method and appropriate comparators.
- **Independent variables: []** State what changes between conditions.
- **Dependent variables: []** State the measured outcomes.
- **Controlled variables: []** Hold data, preprocessing, compute, training
  schedule, evaluation, and other confounders constant.
- **Data split:** Define train, validation, and untouched test partitions.
- **Leakage checks: []** Check overlap and duplicates; fit preprocessing on
  training data only; tune only on validation data; evaluate the locked design
  on the test set once.
- **Ablations: []** Isolate the proposed contribution, or state why none is
  required.
- **Primary metrics: []** Predeclare the metric that decides the hypothesis.
- **Guardrail metrics: []** Predeclare regressions, cost, safety, or quality
  limits that can block success.
- **Seeds: []** Predeclare multiple paired seeds.
- **Repetitions:** Run and report every predeclared repetition; never select
  favorable seeds or runs.
- **Resource request:** Estimate GPU-hours and state any valid stopping design.
- **Success rule:** State the effect, uncertainty, and guardrail thresholds that
  support the claim.
- **Negative-result rule:** State what evidence rejects or fails to support the
  predicted improvement.
- **Inconclusive rule:** State what insufficient power, excessive variance,
  failed checks, or mixed metrics require another study.
- **Expected artifacts: []** Include configuration, split identifiers, logs,
  per-run metrics, aggregate uncertainty, and environment details.

## Validity under pressure

- Never tune thresholds, hyperparameters, prompts, checkpoints, or metrics on
  the test set. Reserve it for final evaluation after the design is locked.
- Never infer superiority from one seed or report only favorable repetitions.
- If the GPU budget cannot support the proposed conclusion, narrow the
  hypothesis, population, or design and state the narrower claim; otherwise
  mark the result inconclusive. Never silently weaken validity to fit budget.

## Common mistakes

| Pressure | Valid response |
|---|---|
| “Use the test set to save time” | Tune on validation; keep test final-only. |
| “One seed is enough” | Treat it as a pilot; run paired repetitions. |
| “The budget is fixed” | Narrow the claim/design or return inconclusive. |
