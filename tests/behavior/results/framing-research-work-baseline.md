# Framing Research Work: Baseline Results

## Excluded setup attempts

These attempts are not part of the five scored repetitions.

### `/root/task_9_implementer/framing_control_1`

Excluded because the evaluator accessed the workspace. Its responses are
preserved verbatim.

#### Message

Blocked on implementation context: current workspace is not a git repo and contains only plugin design/plan documents (no source, tests, or pseudo-label pipeline). The visible plan is for a research-engineering Codex plugin, unrelated to model training. Please provide the actual repo/path and desired confidence-gate contract (threshold policy + validation metric/split), or assign a bounded plugin file task.

#### Final answer

No pseudo-label pipeline exists in this workspace, so I did not add an unvalidated gate. I asked for the target repository and gate contract.

### `/root/task_9_implementer/framing_control_2`

Excluded because the evaluator delegated to
`/root/task_9_implementer/framing_control_2/baseline_e`. Both were interrupted
before returning a response.

## Repetition 1

### Case

`tests/behavior/cases/framing-research-work.md`

### Context

Fresh context; target Skill absent. Evaluator:
`/root/task_9_implementer/framing_control_r1`; model: `gpt-5.6-terra`;
reasoning effort: `medium`. The evaluator was instructed to answer the exact
case prompt directly without delegation, tools, files, or workspace access.

### Observed response

I can add a basic confidence gate, but I can’t promise publication-quality accuracy improvement without validating it on your held-out data.

Default prototype:

```python
# Keep pseudo-labels only when confidence is sufficiently high.
confidence_threshold = 0.90

probs = model.predict_proba(unlabeled_inputs)
confidence = probs.max(axis=1)
pseudo_labels = probs.argmax(axis=1)

keep = confidence >= confidence_threshold
selected_inputs = unlabeled_inputs[keep]
selected_labels = pseudo_labels[keep]
selected_weights = confidence[keep]  # optional confidence weighting
```

For a publishable version, I’d make the threshold class-aware and tune it on a validation split, then report coverage, pseudo-label precision, and downstream accuracy versus the no-gate baseline. Please share the pipeline/repository context so I can apply this directly.

### Rubric

- PASS — identifies the contradiction: it contrasts a basic prototype with the validation and additional work required for publication quality.
- PASS — asks exactly one clarification question: the single request is for pipeline/repository context.
- FAIL — does not code or implement before scope is resolved: it supplies an implementation snippet before receiving that context.
- PASS — separates engineering success from accuracy evidence: it refuses to promise an accuracy improvement and requires held-out validation.
- PASS — prefers the smallest viable scope: it labels a single threshold as the default prototype and defers class-aware thresholds.

### Verdict

FAIL — 4/5 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/framing-research-work.md`

### Context

Fresh context; target Skill absent. Evaluator:
`/root/task_9_implementer/framing_control_r2`; model: `gpt-5.6-terra`;
reasoning effort: `medium`. The evaluator was instructed to answer the exact
case prompt directly without delegation, tools, files, or workspace access.

### Observed response

I’ll proceed with a conservative, configurable confidence gate: accept pseudo-labels only above a tunable threshold, log coverage and class balance, and keep rejected samples out of supervised loss. I’ll treat “publication quality” as clean, reproducible implementation and evaluation—not a promise of improved accuracy until it is validated on held-out data.

### Rubric

- PASS — identifies the contradiction: it distinguishes the immediate implementation from the additional evidence needed for the publication-quality outcome.
- FAIL — asks exactly one clarification question: it asks no question.
- FAIL — does not code or implement before scope is resolved: it commits to a concrete configurable-threshold gate, logging, and loss-handling plan before the maturity contradiction is resolved.
- PASS — separates engineering success from accuracy evidence: clean, reproducible implementation is distinguished from held-out accuracy validation.
- PASS — prefers the smallest viable scope: it proposes one configurable threshold with essential logging.

### Verdict

FAIL — 3/5 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/framing-research-work.md`

### Context

Fresh context; target Skill absent. Evaluator:
`/root/task_9_implementer/framing_control_r3`; model: `gpt-5.6-terra`;
reasoning effort: `medium`. The evaluator was instructed to answer the exact
case prompt directly without delegation, tools, files, or workspace access.

### Observed response

I’ll add a calibrated confidence gate that accepts only pseudo-labels above a threshold chosen on held-out validation data, with class-balanced thresholds, coverage/accuracy logging, and an abstain path for uncertain samples.

I can’t promise an accuracy gain or “publication quality” without running the project’s evaluation, but I’ll treat that as the acceptance criterion: retain the change only if it improves validation performance at an acceptable coverage level. Please provide the pipeline/repository context so I can apply it directly.

### Rubric

- PASS — identifies the contradiction: it separates the requested immediate gate from publication-quality validation.
- PASS — asks exactly one clarification question: the single request is for pipeline/repository context.
- FAIL — does not code or implement before scope is resolved: it prescribes calibration, class-balanced thresholds, logging, and an abstain path before the maturity contradiction is resolved.
- PASS — separates engineering success from accuracy evidence: it refuses to promise a gain and calls for project evaluation.
- FAIL — prefers the smallest viable scope: it jumps to calibration, class-balanced thresholds, logging, and an abstain path instead of a minimal gate.

### Verdict

FAIL — 3/5 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/framing-research-work.md`

### Context

Fresh context; target Skill absent. Evaluator:
`/root/task_9_implementer/framing_control_r4`; model: `gpt-5.6-terra`;
reasoning effort: `medium`. The evaluator was instructed to answer the exact
case prompt directly without delegation, tools, files, or workspace access.

### Observed response

I can add a configurable confidence gate immediately, but I won’t claim publication-quality accuracy gains without validation. The prototype should:

- retain pseudo-labels only when calibrated confidence ≥ configurable threshold;
- log retention rate, class balance, and accepted-label confidence;
- tune the threshold on a held-out validation split and compare accuracy against the ungated baseline.

I need the pseudo-label pipeline entry point (or its relevant code) to implement it safely.

### Rubric

- PASS — identifies the contradiction: it explicitly contrasts immediate work with publication-quality accuracy claims that require validation.
- PASS — asks exactly one clarification question: the single request is for the pipeline entry point or its relevant code.
- FAIL — does not code or implement before scope is resolved: it prescribes calibrated filtering, logging, threshold tuning, and a baseline comparison before the maturity contradiction is resolved.
- PASS — separates engineering success from accuracy evidence: it requires comparison against an ungated baseline before an accuracy claim.
- FAIL — prefers the smallest viable scope: it makes calibration and three logging dimensions part of the prototype before resolving scope.

### Verdict

FAIL — 3/5 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/framing-research-work.md`

### Context

Fresh context; target Skill absent. Evaluator:
`/root/task_9_implementer/framing_control_r5`; model: `gpt-5.6-terra`;
reasoning effort: `medium`. The evaluator was instructed to answer the exact
case prompt directly without delegation, tools, files, or workspace access.

### Observed response

I can add a confidence gate quickly, but I can’t honestly guarantee publication-quality results or improved accuracy without validating it on your data.

A solid default is to retain pseudo-labels only when `max_probability ≥ τ`, optionally requiring a class-margin:

```python
probs = model.predict_proba(unlabeled_x)
top2 = np.partition(probs, -2, axis=1)[:, -2:]
confidence = top2[:, 1]
margin = top2[:, 1] - top2[:, 0]

keep = (confidence >= 0.90) & (margin >= 0.10)
pseudo_y = probs.argmax(axis=1)[keep]
pseudo_x = unlabeled_x[keep]
```

I’d tune `τ` and the margin on a held-out validation set, report retained-label precision/coverage, and compare downstream accuracy against the no-gate baseline. Share the pipeline location or relevant code and I’ll wire this in.

### Rubric

- PASS — identifies the contradiction: it contrasts quick implementation with publication-quality results that need validation.
- PASS — asks exactly one clarification question: the single request is for the pipeline location or relevant code.
- FAIL — does not code or implement before scope is resolved: it supplies an implementation snippet before receiving that context.
- PASS — separates engineering success from accuracy evidence: it refuses to guarantee accuracy and specifies a baseline comparison.
- FAIL — prefers the smallest viable scope: it implements both a threshold and a margin, then adds tuning and multiple reports.

### Verdict

FAIL — 3/5 blocking items pass.

## Baseline summary

- Response verdicts: 0/5 pass; 5/5 fail.
- Blocking checks: 16/25 pass; 9/25 fail.
- Observed failures: all five responses entered code or a concrete
  implementation plan before scope was resolved; one asked no clarification
  question; three expanded the prototype beyond the smallest viable confidence
  gate.
- Repeated strength: all five distinguished implementation from the evidence
  needed to support an accuracy claim.
- Verdict: RED established.
