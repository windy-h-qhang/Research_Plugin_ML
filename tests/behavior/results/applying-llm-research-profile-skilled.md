# Applying LLM Research Profile — Skilled Results

Fresh evaluators received the current Skill inline before one prompt. They
received no rubric or expected answer and had no access to tools, files, the
workspace, browsing, or delegation. All responses are verbatim.

## Iteration 1 — failed and superseded

Iteration 1 stopped after two primary repetitions because a blocking failure
requires a Skill revision and complete fresh-context restart of both prompts.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill_1`

#### Observed response

> No. The comparison is confounded, so it cannot establish that the finetune is better.
>
> - A changed chat template and packing alter token boundaries and loss support; losses are not directly comparable unless tokenizer revision, special tokens, template, masks, positions, and document-attention boundaries are controlled.
> - Prompt tokens are included in labels, so the SFT loss measures prompt prediction as well as assistant/completion quality. Mask prompt labels with the ignore index and recompute.
> - Possible benchmark presence in pretraining makes evaluation vulnerable to contamination; audit and document training data and use a clean held-out benchmark.
> - A temperature change invalidates a direct generation-quality comparison. Hold temperature, decoding parameters, evaluator configuration, and checkpoint state constant.
>
> Verify the intended checkpoint as well—base-model revision, adapter/merged weights, resume state, and quantization compatibility—then rerun a controlled evaluation before making a quality claim.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and explicitly says the
  changed template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt labels so loss measures
  assistant/completion output.
- FAIL — connects packing to boundaries and names masks and positions, but only
  requires them to be controlled; it does not require recomputing attention
  masks, position ids, and label masks after packing.
- PASS — identifies benchmark contamination and requires an audited clean
  held-out benchmark.
- PASS — says changed temperature invalidates direct comparison and requires
  fixed decoding and evaluator settings.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — rejects the confounded comparison and requires the named controls,
  intended checkpoint, and a rerun of controlled evaluation before making a
  quality claim.

#### Verdict

FAIL — 6/7 blocking groups passed.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill_2`

#### Observed response

> No. The comparison is confounded, so it cannot support a claim that the finetune is better.
>
> - Changing the chat template and packing changes token sequences and sequence boundaries; the resulting SFT losses are not directly comparable unless tokenizer revision, special tokens, template, masks, positions, and document-boundary isolation are controlled.
> - Including prompt tokens in labels means loss is not restricted to assistant/completion output, invalidating the intended SFT-loss interpretation. Prompt labels must use the ignore index.
> - Possible benchmark presence in pretraining data makes evaluation vulnerable to contamination; audit and document training-data sources and benchmark splits.
> - Changing temperature invalidates a direct generation-quality comparison. Hold temperature, all decoding settings, and evaluator configuration fixed.
> - Also confirm the same intended checkpoint/base revision and any adapter/merged-weight and quantization state.
>
> Re-run with these controls before making a quality claim.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and explicitly says the
  changed template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt labels so loss is restricted to
  assistant/completion output.
- FAIL — connects packing to boundaries and names masks and positions, but only
  requires them to be controlled; it does not require recomputing attention
  masks, position ids, and label masks after packing.
- PASS — identifies benchmark contamination and requires auditing data sources
  and benchmark splits.
- PASS — says changed temperature invalidates direct comparison and requires
  fixed decoding and evaluator settings.
- FAIL — checks intended checkpoint, merged weights, and quantization, but omits
  checkpoint resume state.
- PASS — says the current comparison cannot support better-finetune quality and
  requires rerunning with the template, packing, masking, contamination,
  decoding, evaluator, and checkpoint controls before claiming improvement.

#### Verdict

FAIL — 5/7 blocking groups passed.

### Iteration 1 aggregate

- Primary: 6/7, 5/7 = 11/14; 0/2 complete.
- Counter-example: not run after the blocking primary failure.
- Status: failed and superseded; neither response is part of the final arm.
- Excluded or replaced samples: none. These are valid failed samples retained
  verbatim, not excluded samples.

## Iteration 2 — failed and superseded

Iteration 2 restarted after the first revision and stopped after four primary
repetitions because repetition 3 had a blocking failure.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill2_1`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> - The chat-template change changes the token sequence and loss support; pin the tokenizer revision, special tokens, and template before comparing SFT loss.
> - Labels currently include prompt tokens. Set the ignore index on every prompt token so loss measures only assistant/completion tokens.
> - Packing changes sequence boundaries. Recompute attention masks, position IDs, and label masks, and block attention across packed document boundaries; treat it as a separate experimental condition.
> - Possible benchmark presence in pretraining is contamination. Audit and document training-data sources and benchmark splits before treating scores as generalization.
> - A generation-temperature change invalidates a direct quality comparison. Hold temperature, all decoding parameters, and evaluator settings fixed.
> - Confirm both runs use the intended checkpoint: resume/optimizer state, base-model revision, adapter vs. merged PEFT weights and folding, plus compatible quantization.
>
> Rerun matched evaluations with those controls. Only then can you assess whether the finetune improved.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention
  masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing data sources and
  benchmark splits.
- PASS — says changed temperature invalidates comparison and requires fixed
  decoding and evaluator settings.
- PASS — checks intended checkpoint, resume state, merged PEFT weights, and
  quantization compatibility.
- PASS — rejects the confounded evidence and requires matched evaluations with
  the named controls before assessing whether the finetune improved.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill2_2`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> 1. Changing the chat template changes tokenization and loss support; pin the tokenizer revision, special tokens, and template before comparing SFT loss.
>
> 2. Prompt tokens are included in labels. Assign the ignore index to every prompt token so loss measures assistant/completion tokens only.
>
> 3. Packing changes sequence boundaries. Recompute attention masks, position IDs, and label masks, and prevent attention across document boundaries; truncation must be handled equivalently.
>
> 4. Benchmark examples may be in pretraining data, so audit and document pretraining/finetuning sources and splits for contamination.
>
> 5. Generation temperature changed. Hold temperature and every other decoding and evaluator setting constant for a quality comparison.
>
> 6. Confirm both evaluations use the intended checkpoint state: base-model revision, resume/optimizer state, and any PEFT adapter versus merged-weight or quantization configuration.
>
> 7. Until these controls are fixed, the lower loss and generation results cannot demonstrate that the finetune improved.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention
  masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing pretraining/finetuning
  sources and splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization configuration.
- PASS — says lower loss and generation results cannot demonstrate improvement
  until the template, packing, masking, contamination, decoding/evaluator, and
  checkpoint controls are fixed for a comparable quality evaluation.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill2_3`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> - Tokenizer/chat template: changing the chat template changes token sequences and loss support; pin the tokenizer revision, special tokens, and template before comparing SFT loss.
> - Label masking: prompt tokens are included in labels, so the reported loss is not assistant/completion-only. Apply the ignore index to every prompt token.
> - Packing/truncation: if packing changed too, treat it as a boundary change—recompute attention, positions, and label masks, and block cross-document attention.
> - Contamination: benchmark examples may be in pretraining data. Audit and document pretraining/finetuning sources and benchmark splits before treating scores as generalization.
> - Decoding: changed temperature invalidates a direct generation-quality comparison. Hold temperature and every other decoding/evaluator setting constant.
> - Checkpoint: also verify the intended training state was evaluated—base revision, resume/optimizer state, and any PEFT adapter versus merged weights.
>
> Re-run a controlled comparison with these settings fixed; only then can the results support a “better finetune” claim.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention,
  position, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing pretraining/finetuning
  sources and benchmark splits.
- PASS — says changed temperature invalidates comparison and requires fixed
  decoding and evaluator settings.
- FAIL — checks intended checkpoint, resume state, and merged weights, but omits
  quantization compatibility; the checkpoint group is all-or-nothing.
- PASS — rejects the confounded evidence and explicitly requires a controlled
  comparison with the named settings fixed before supporting a
  better-finetune claim.

#### Verdict

FAIL — 6/7 blocking groups passed.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill2_4`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> - The chat-template change alters tokenization and loss support; pin the tokenizer revision, special tokens, and template before comparing SFT loss.
> - Prompt tokens are included in labels. Assign the ignore index to every prompt token so loss measures assistant/completion tokens only.
> - Packing changes sequence boundaries; recompute attention, position, and label masks, and block cross-document attention.
> - Possible benchmark presence in pretraining is contamination. Audit and document all training-data sources and evaluation splits.
> - The generation temperature changed. Hold temperature, all decoding parameters, and evaluator settings fixed for a quality comparison.
> - Confirm both runs evaluate the intended checkpoints, including resume/optimizer state, base revision, and any PEFT adapter/merged-weight or quantization compatibility.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention,
  position, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing training sources and
  evaluation splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — says the current evidence cannot support a better-finetune claim and
  requires correcting the template, masking, packing, and contamination issues
  and fixing decoding/evaluator settings for a quality comparison.

#### Verdict

PASS — 7/7 blocking groups passed.

### Iteration 2 aggregate

- Primary: 7/7, 7/7, 6/7, 7/7 = 27/28; 3/4 complete.
- Counter-example: not run after the blocking primary failure.
- Status: failed and superseded; none of these responses is part of the final
  arm.
- Excluded or replaced samples: none. These are valid failed/superseded samples
  retained verbatim, not excluded samples.

## Iteration 3 — final

Iteration 3 used the final Skill revision and fresh contexts for all ten
formal repetitions.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill3_1`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> 1. The chat-template change changes tokenization/loss support; pin tokenizer revision, special tokens, and template before comparing SFT loss.
> 2. Labels currently include prompt tokens; mask prompt tokens with the ignore index so loss covers assistant/completion tokens only.
> 3. If packing changed, recompute attention masks, position ids, and label masks, and block attention across document boundaries.
> 4. Possible benchmark presence in pretraining must be audited and documented by source and split; contamination invalidates a clean evaluation claim.
> 5. Temperature changed, so generation-quality results are not directly comparable. Hold temperature, all decoding parameters, and evaluator settings fixed.
> 6. Confirm the intended checkpoint: resume and optimizer state, base revision, PEFT adapter versus merged weights and correct folding, plus quantization compatibility.
> 7. Claim limit: the observed loss improvement may reflect template, label-support, packing, or decoding differences—not improved finetuning quality.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention
  masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires an audit by data source and
  split.
- PASS — says changed temperature makes results incomparable and requires fixed
  decoding and evaluator settings.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — limits the claim to confounded loss rather than improved quality and
  requires the named corrections plus fixed settings for a comparable
  generation-quality evaluation.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill3_2`

#### Observed response

> No. The evidence is confounded and cannot establish that the finetune is better.
>
> 1. The chat-template change alters tokenization/loss support; pin the tokenizer revision, special tokens, and template before comparing SFT loss.
> 2. Prompt tokens are included in labels; mask them with the ignore index so loss covers only assistant/completion tokens.
> 3. Packing changes sequence boundaries; recompute attention masks, position ids, and label masks, and block attention across document boundaries.
> 4. Possible benchmark presence in pretraining data is contamination; audit and document all data sources and evaluation splits.
> 5. Temperature changed; hold it, every decoding parameter, and evaluator settings constant for generation-quality comparisons.
> 6. Confirm the intended checkpoint: resume and optimizer state, adapter versus merged weights, adapter folding, base-model revision, and quantization compatibility.
> 7. Until these controls are satisfied, neither the lower loss nor evaluation results support a claim that the finetune is better.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention
  masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing data sources and
  evaluation splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  generation-quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — says neither lower loss nor evaluation results support improvement
  until the template, masking, packing, contamination, decoding/evaluator, and
  checkpoint controls are satisfied.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill3_3`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> 1. The chat template changed; pin the tokenizer revision, special tokens, and chat template before comparing SFT loss, since these change token sequences and loss support.
> 2. Labels currently include prompt tokens; mask prompt tokens with the ignore index so loss covers assistant/completion tokens only.
> 3. If packing or truncation changed, treat it as a boundary change: recompute attention masks, position IDs, and label masks, and block attention across document boundaries.
> 4. Benchmark examples may be in pretraining data; audit and document pretraining/finetuning sources and splits before treating evaluation as valid.
> 5. Generation temperature changed; hold temperature and every other decoding and evaluator setting constant for a quality comparison.
> 6. Verify the checkpoint is the intended state: resume and optimizer state, PEFT adapter versus merged weights and correct folding, base-model revision, and quantization compatibility.
> 7. Until these controls are in place, the improved loss and any generation results are not comparable and cannot establish that the finetune improved.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing/truncation to boundaries and requires recomputed
  attention masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing pretraining/finetuning
  sources and splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — says the current loss and generation results are incomparable and
  cannot establish improvement until all named controls are in place for a
  valid quality evaluation.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill3_4`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> 1. The chat template changed; pin the tokenizer revision, special tokens, and template before comparing SFT loss, because they change token sequences and loss support.
> 2. Labels currently include prompt tokens; apply the ignore index to all prompt tokens so loss measures assistant/completion tokens only.
> 3. If packing or truncation changed, treat it as a boundary change: recompute attention masks, position IDs, and label masks, and block attention across document boundaries.
> 4. Benchmark examples may be in pretraining data; audit and document pretraining/finetuning sources and splits to rule out contamination.
> 5. Temperature changed; hold temperature, all decoding parameters, and evaluator settings constant for a generation-quality comparison.
> 6. Confirm the intended checkpoint: resume and optimizer state, PEFT adapter versus merged weights, correct adapter folding, base-model revision, and quantization compatibility.
> 7. Until these controls are in place, the improved loss and generation results are not comparable and cannot establish that the finetune improved.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing/truncation to boundaries and requires recomputed
  attention masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing pretraining/finetuning
  sources and splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  generation-quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — says the current loss and generation results are incomparable and
  cannot establish improvement until all named controls are in place for a
  controlled generation-quality comparison.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 5

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_p_skill3_5`

#### Observed response

> No. The evidence is confounded, so it cannot support a claim that the finetune is better.
>
> 1. The tokenizer revision, special tokens, and chat template must be pinned: changing the chat template changes tokenization and loss support, so the SFT-loss comparison is not directly comparable.
>
> 2. Label masking is incorrect: prompt tokens must use the ignore index, with loss computed only over assistant/completion tokens.
>
> 3. If packing was changed, treat it as a sequence-boundary change: recompute attention masks, position ids, and label masks, and prevent attention across packed document boundaries.
>
> 4. Benchmark contamination is possible: audit pretraining and finetuning sources/splits and document whether benchmark examples occur in them.
>
> 5. Generation temperature changed, so hold temperature and every other decoding and evaluator setting constant before comparing generation quality.
>
> 6. Also confirm both runs evaluate the intended checkpoint: resume state, optimizer state, PEFT adapter versus merged weights, correct adapter folding, base-model revision, and quantization compatibility.
>
> After fixing these controls and rerunning comparable evaluations, you can assess whether the finetune improved.

#### Rubric

- PASS — checks tokenizer/chat-template consistency and states that the changed
  template makes SFT losses incomparable.
- PASS — requires the ignore index for prompt tokens so loss is
  assistant/completion-only.
- PASS — connects packing to boundaries and requires recomputed attention
  masks, position ids, and label masks plus cross-document isolation.
- PASS — identifies contamination and requires auditing pretraining/finetuning
  sources and splits.
- PASS — requires fixed temperature, decoding, and evaluator settings for the
  generation-quality comparison.
- PASS — checks intended checkpoint, resume state, merged weights, and
  quantization compatibility.
- PASS — rejects the current confounded evidence and explicitly requires fixing
  the named controls and rerunning comparable evaluations before assessing
  whether the finetune improved.

#### Verdict

PASS — 7/7 blocking groups passed.

### Counter-example repetition 1

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_c_skill3_1`

#### Observed response

> The LLM Research Profile does not apply: this is a tabular XGBoost experiment, not an LLM training or generation evaluation. Review it using tabular controls—data splits/leakage, feature preprocessing, hyperparameter parity, random seeds, validation protocol, and metric consistency—without tokenizer, chat-template, masking, contamination, decoding, or KV-cache checks.

#### Rubric

- PASS — explicitly classifies the tabular XGBoost task as non-LLM work and
  states that the LLM Research Profile does not apply.
- PASS — explicitly avoids tokenizer, chat-template, masking, contamination,
  decoding, and KV-cache checks.
- PASS — gives a concise tabular-ML review without LLM ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 2

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_c_skill3_2`

#### Observed response

> The LLM Research Profile does not apply: this is a tabular XGBoost experiment with no tokenization, chat templates, generation, masking, decoding, or KV-cache concerns.
>
> Review it by checking train/validation/test split integrity, leakage prevention, feature availability at prediction time, cross-validation design, class imbalance handling, hyperparameter tuning isolation, metric choice, baseline comparisons, calibration if probabilities are used, and reproducibility through fixed seeds and documented data/versioning.

#### Rubric

- PASS — explicitly states that the LLM Research Profile does not apply to the
  tabular XGBoost task.
- PASS — explicitly avoids tokenizer, chat-template, masking, decoding, and
  KV-cache concerns and applies no other LLM-specific checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 3

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_c_skill3_3`

#### Observed response

> The LLM Research Profile does not apply: a tabular XGBoost experiment has no tokenizer, chat template, token masking, packing, decoding, or KV-cache concerns.
>
> Review it using tabular ML controls instead: fixed train/validation/test splits, leakage checks, consistent feature preprocessing, tuned hyperparameters selected only on validation data, appropriate metrics, baseline comparison, and test-set evaluation after final model selection.

#### Rubric

- PASS — explicitly states that the LLM Research Profile does not apply to the
  tabular XGBoost task.
- PASS — explicitly avoids tokenizer, chat-template, masking, packing, decoding,
  and KV-cache concerns and applies no other LLM-specific checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 4

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_c_skill3_4`

#### Observed response

> The LLM Research Profile does not apply: this is a tabular XGBoost experiment with no language-model tokenization, training templates, generation, decoding, or KV-cache behavior to assess.
>
> Review it on tabular-ML controls instead:
>
> - Use a leakage-safe train/validation/test split, ideally time- or entity-based when the data-generating process requires it.
> - Fit preprocessing, imputation, encoding, feature selection, and target transformations using training data only.
> - Keep the split, feature set, target definition, evaluation metric, and sample weights fixed across compared runs.
> - Tune XGBoost only against validation/CV data; keep the test set untouched until final evaluation.
> - Check class imbalance handling, missing-value behavior, categorical encoding, and duplicate or near-duplicate rows across splits.
> - Report variation across folds/seeds and compare against a simple baseline.
> - Inspect feature leakage and validate that the chosen metric reflects the decision objective.
>
> A score increase alone does not establish a better model if splits, preprocessing, features, or evaluation conditions changed between experiments.

#### Rubric

- PASS — explicitly states that the LLM Research Profile does not apply to the
  tabular XGBoost task.
- PASS — explicitly avoids language-model tokenization, templates, generation,
  decoding, and KV-cache checks and applies no other LLM-specific checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 5

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_17_implementer/llm_c_skill3_5`

#### Observed response

> The LLM Research Profile does not apply: this is a tabular XGBoost experiment with no tokenization, language-model training, generation, or decoding.
>
> Review it instead for train/validation/test split integrity, leakage, feature availability timing, class imbalance handling, hyperparameter search isolation, metric choice, baseline comparisons, calibration, and performance across relevant segments.

#### Rubric

- PASS — explicitly states that the LLM Research Profile does not apply to the
  tabular XGBoost task.
- PASS — explicitly avoids tokenization, language-model training, generation,
  and decoding checks and applies no other LLM-specific checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Iteration 3 aggregate

- Primary: 7/7, 7/7, 7/7, 7/7, 7/7 = 35/35; 5/5 complete.
- Counter-example: 3/3, 3/3, 3/3, 3/3, 3/3 = 15/15; 5/5 complete.
- Total: 50/50 blocking groups; 10/10 responses complete.
- GREEN confirmed: yes.
- Failed/superseded arms retained: Iteration 1 (11/14 primary; two valid
  failed samples) and Iteration 2 (27/28 primary; four valid samples, including
  one blocking failure).
- Excluded or replaced samples: none.
