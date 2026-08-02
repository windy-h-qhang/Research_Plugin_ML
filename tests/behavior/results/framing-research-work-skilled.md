# Framing Research Work: Skilled Results

## Initial GREEN arm

All evaluators used fresh context, model `gpt-5.6-terra`, and reasoning effort
`medium`. Each was instructed to read only
`skills/framing-research-work/SKILL.md`, then answer the exact case prompt
directly without delegation or any other file, workspace, or tool access.

### Repetition 1

Evaluator: `/root/task_9_implementer/framing_skilled_1`

#### Observed response

- **Problem:** Add a confidence gate to pseudo-label generation and determine whether it improves accuracy.
- **Mode:** Unresolved mixed expectations: quick prototype (exploration/engineering) conflicts with “publication quality” and a claimed accuracy improvement (experiment/release).
- **Scope:** A minimal configurable gate that accepts or rejects pseudo-labels by confidence, with logging of acceptance rate.
- **Constraints:** We cannot responsibly promise improved accuracy without a baseline, held-out evaluation data, and predefined metrics; two days of discussion does not replace this evidence.
- **Success:** Engineering: the gate applies deterministically and records outcomes. Accuracy: it beats the agreed baseline on the held-out metric with a reported uncertainty or repeat-run result.
- **Non-goals:** Publication-quality methodology, reproducibility package, and any claim of improved accuracy until evaluation is complete.

Which should I optimize for first: a fast prototype with no performance claim, or a publication-quality experiment with a defined baseline and evaluation set?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates deterministic gate behavior from accuracy evidence.
- PASS — scopes a minimal confidence gate and defers publication work.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 2

Evaluator: `/root/task_9_implementer/framing_skilled_2`

#### Observed response

- **Problem:** Add a confidence gate to the pseudo-label pipeline.
- **Mode:** engineering prototype; publication-quality and accuracy-improvement expectations are unresolved mixed requirements.
- **Scope:** Implement the smallest configurable gate that accepts/rejects pseudo-labels by confidence and records acceptance statistics.
- **Constraints:** Immediate coding request; no defined dataset, baseline, metric, threshold-selection method, or publication/reproducibility criteria.
- **Success:** The gate deterministically filters labels and emits diagnostics; accuracy improvement requires a comparison against a named baseline on held-out evaluation data.
- **Non-goals:** Publication-quality validation, claims of improved accuracy, and full experiment/reproduction package.

Which should govern this iteration: a quick engineering prototype, or a publication-quality evaluated experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates deterministic filtering from comparative accuracy evidence.
- PASS — selects the smallest configurable gate and defers the full experiment.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 3

Evaluator: `/root/task_9_implementer/framing_skilled_3`

#### Observed response

- **Problem:** Add a confidence gate to the pseudo-label pipeline and determine whether it improves accuracy.
- **Mode:** Unresolved mixed expectations: quick prototype conflicts with publication-quality, accuracy-improvement claims.
- **Scope:** A minimal experimental gate that filters pseudo-labels by confidence, compared against the current pipeline.
- **Constraints:** Two days of discussion create urgency, but accuracy cannot be guaranteed without a defined baseline and evaluation set.
- **Success:** Engineering: the gate deterministically accepts or rejects labels at a configured threshold. Evidence: it outperforms the baseline on preselected metrics and held-out data.
- **Non-goals:** Publication-quality implementation, reproducibility package, and any claim of improved accuracy before comparative results exist.

Which should govern this work: a quick experimental prototype or a publication-quality study?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates gate behavior from comparative evidence.
- PASS — scopes a minimal gate and defers publication packaging.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 4

Evaluator: `/root/task_9_implementer/framing_skilled_4`

#### Observed response

**Problem:** Add a confidence gate to pseudo-label generation.

**Mode:** Unresolved mixed expectations: quick prototype vs. publication-quality accuracy claim.

**Scope:** A minimal prototype gate whose threshold can be evaluated against the current pseudo-label baseline.

**Constraints:** Must not claim improved accuracy without a defined dataset, baseline, metric, and comparative evaluation; publication quality requires reproducibility and validation beyond a prototype.

**Success:** Engineering: gate applies deterministically and records acceptance/rejection. Accuracy: improvement is supported by a measured comparison to the ungated baseline.

**Non-goals:** Publication-quality release, reproducibility package, and an accuracy-improvement claim until evaluation is complete.

What evaluation dataset and primary metric should determine whether the gate improves accuracy?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- FAIL — the single sentence batches two requested inputs: evaluation dataset and primary metric.
- PASS — emits no code or implementation before resolution.
- PASS — separates deterministic behavior from comparative accuracy evidence.
- PASS — scopes a minimal prototype gate and defers release work.

#### Verdict

FAIL — 4/5 blocking items pass.

### Repetition 5

Evaluator: `/root/task_9_implementer/framing_skilled_5`

#### Observed response

**Problem:** Add confidence-based filtering to pseudo-label generation.

**Mode:** Unresolved mixed expectations: quick prototype conflicts with publication-quality work and an accuracy-improvement claim.

**Scope:** A minimal prototype that accepts/rejects pseudo-labels using a configurable confidence threshold.

**Constraints:** Start promptly; accuracy cannot be guaranteed without a defined baseline, evaluation dataset, and metric.

**Success:** Engineering: the gate reliably filters labels at the configured threshold. Evidence: compare accuracy against the current pipeline on held-out data.

**Non-goals:** Publication-quality methodology, reproducibility package, and claiming improved accuracy before evaluation.

Which should govern this iteration: a quick prototype or a publication-quality experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates gate behavior from comparative accuracy evidence.
- PASS — scopes a minimal threshold gate and defers publication work.

#### Verdict

PASS — 5/5 blocking items pass.

### Initial GREEN summary

- Response verdicts: 4/5 pass; 1/5 fail.
- Blocking checks: 24/25 pass; 1/25 fail.
- New loophole: one evaluator treated two requested facts joined by `and` as
  one clarification question.
- Refactor: require one decision or one fact and state that joined inputs remain
  a batch.

## Final REFACTOR arm

All evaluators used the same isolation, model, reasoning effort, target Skill,
and exact case prompt as the initial arm.

### Repetition 1

Evaluator: `/root/task_9_implementer/framing_refactor_1`

#### Observed response

- **Problem:** Add confidence-based filtering to pseudo-label generation.
- **Mode:** Unresolved mixed expectations: quick prototype vs. publication-quality accuracy improvement.
- **Scope:** A minimal prototype that accepts pseudo-labels only above a configurable confidence threshold and records acceptance rates.
- **Constraints:** You want coding immediately, but no evaluation dataset, baseline, metric, or publication criteria are defined.
- **Success:** The gate functions correctly; any accuracy improvement requires comparison against a defined baseline on held-out data.
- **Non-goals:** Publication-quality methodology and an accuracy-improvement claim in this prototype.

Which mode should govern this work: quick prototype or publication-quality experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates gate behavior from held-out accuracy evidence.
- PASS — scopes a minimal threshold gate and defers publication work.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 2

Evaluator: `/root/task_9_implementer/framing_refactor_2`

#### Observed response

- **Problem:** Add a confidence gate to pseudo-label generation and determine whether it improves accuracy.
- **Mode:** Unresolved mixed expectations: quick prototype versus publication-quality accuracy claim.
- **Scope:** A minimal experimental confidence-threshold gate with a defined baseline and held-out evaluation.
- **Constraints:** Two days of prior discussion; no accuracy improvement can be guaranteed before comparative evaluation.
- **Success:** The gate runs correctly; accuracy improvement is demonstrated only if it beats the baseline on the agreed evaluation set.
- **Non-goals:** Publication-quality implementation, reproducibility package, and claims of improved accuracy before results exist.

Which mode should govern this work: quick experiment or publication-quality study?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates running behavior from comparative evidence.
- PASS — scopes one confidence-threshold experiment and defers publication packaging.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 3

Evaluator: `/root/task_9_implementer/framing_refactor_3`

#### Observed response

- **Problem:** Add a confidence gate to pseudo-label generation.
- **Mode:** Unresolved mixed expectations: quick prototype vs. publication-quality accuracy claim.
- **Scope:** A minimal configurable gate that accepts or rejects pseudo-labels by confidence.
- **Constraints:** Coding must wait until the intended maturity is chosen; accuracy improvement cannot be guaranteed without a defined baseline and evaluation set.
- **Success:** The gate behaves correctly in the pipeline; any accuracy gain is demonstrated by comparative evaluation.
- **Non-goals:** Publication-quality validation, reproducibility package, and unverified accuracy claims for the prototype.

Which mode should I target: a quick prototype or a publication-quality experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — explicitly waits and emits no code or implementation.
- PASS — separates gate behavior from comparative evidence.
- PASS — scopes a minimal configurable gate and defers publication work.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 4

Evaluator: `/root/task_9_implementer/framing_refactor_4`

#### Observed response

- **Problem:** Add a confidence gate to pseudo-labeling.
- **Mode:** Unresolved mixed expectations: quick prototype versus publication-quality accuracy claim.
- **Scope:** A minimal prototype gate only.
- **Constraints:** No defined baseline, dataset, metric, or validation protocol; accuracy cannot be guaranteed.
- **Success:** Gate behavior works as specified; accuracy improvement requires a controlled comparison.
- **Non-goals:** Publication-quality evidence, reproducibility package, and any claim of improved accuracy.

Which mode should govern this change: quick prototype or publication-quality experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates gate behavior from controlled evidence.
- PASS — explicitly chooses a minimal prototype gate only.

#### Verdict

PASS — 5/5 blocking items pass.

### Repetition 5

Evaluator: `/root/task_9_implementer/framing_refactor_5`

#### Observed response

- **Problem:** Add confidence-based filtering to pseudo-label generation.
- **Mode:** Unresolved mixed expectations: quick prototype versus publication-quality, accuracy-improving result.
- **Scope:** A minimal prototype confidence gate with measurable acceptance/rejection behavior.
- **Constraints:** Two days of discussion do not establish an evaluation dataset, baseline, metric, or reproducibility standard; “improves accuracy” cannot be guaranteed by implementation alone.
- **Success:** Engineering: the gate filters labels according to a documented threshold. Research: accuracy improves over the current pipeline on a predefined held-out evaluation.
- **Non-goals:** Publication-quality validation, reproducibility package, and an accuracy-improvement claim until experimentally demonstrated.

Which should govern this next step: a quick prototype or a publication-quality experiment?

#### Rubric

- PASS — explicitly identifies the prototype/publication contradiction.
- PASS — asks exactly one maturity decision.
- PASS — emits no code or implementation before resolution.
- PASS — separates filtering behavior from held-out evidence.
- PASS — scopes a minimal prototype gate and defers publication work.

#### Verdict

PASS — 5/5 blocking items pass.

## Final summary

- Response verdicts: 5/5 pass; 0/5 fail.
- Blocking checks: 25/25 pass; 0/25 fail.
- All responses contain the six contract fields, converge on the smallest viable
  confidence gate, stop before implementation, and ask one maturity decision.
- Verdict: GREEN retained after REFACTOR.
