# Applying LLM Research Profile — Baseline Results

Five fresh evaluators answered each prompt without the Skill. The evaluators
received one prompt, no rubric or expected answer, and no access to tools,
files, the workspace, browsing, or delegation. All responses are verbatim.

## Primary repetition 1

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_p_ctrl_1`

### Observed response

> No. The loss improvement is confounded: prompt tokens are being scored, benchmark contamination is possible, and decoding temperature changed.
>
> Use a held-out, decontaminated evaluation set; score only assistant/completion tokens; keep the prompt format, model version, decoding parameters, and evaluation protocol identical; and report uncertainty across multiple runs. Only then can you attribute an improvement to the finetune.

### Rubric

- FAIL — requires the same prompt format, but does not check the tokenizer/chat
  template or state that changing the chat template invalidates SFT-loss
  comparability.
- PASS — requires scoring only assistant/completion tokens rather than prompt
  tokens.
- FAIL — does not connect packing to sequence boundaries or require recomputed
  attention masks, position ids, and label masks.
- PASS — identifies contamination and requires a decontaminated evaluation set.
- PASS — identifies changed temperature as a confound and requires identical
  decoding parameters.
- FAIL — does not check resume state, merged weights, or quantization.
- PASS — rejects the confounded loss as evidence and requires a held-out,
  decontaminated, identically configured evaluation before attributing an
  improvement to the finetune.

### Verdict

FAIL — 4/7 blocking groups passed.

## Primary repetition 2

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_p_ctrl_2`

### Observed response

> No. The lower SFT loss is not sufficient evidence that the finetune is better.
>
> It may reflect template/packing changes, loss on prompt tokens, memorized benchmark examples, or generation-temperature differences rather than improved task capability. Compare under identical evaluation settings using held-out, contamination-checked data; report task metrics and uncertainty, and keep decoding parameters fixed (or evaluate across a defined range).

### Rubric

- FAIL — mentions template changes as a confound, but does not check tokenizer
  consistency or explicitly establish that the changed chat template makes the
  losses incomparable.
- FAIL — notes loss on prompt tokens, but does not require label masking that
  excludes them so loss is completion-only.
- FAIL — names packing changes, but does not connect them to sequence boundaries
  or recomputed attention masks, position ids, and label masks.
- PASS — identifies memorized benchmark examples as contamination and requires a
  contamination-checked held-out set.
- PASS — identifies generation-temperature differences as a confound and
  requires fixed decoding parameters.
- FAIL — does not check resume state, merged weights, or quantization.
- PASS — says lower SFT loss is insufficient and requires identical evaluation
  settings, held-out contamination-checked data, and task metrics before a
  quality claim.

### Verdict

FAIL — 3/7 blocking groups passed.

## Primary repetition 3

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_p_ctrl_3`

### Observed response

> No. The lower SFT loss is encouraging, but it is not sufficient evidence that the finetune is better.
>
> Because labels include prompt tokens, loss may improve from fitting prompt format rather than response quality. Benchmark contamination and changed generation temperature also make benchmark comparisons unreliable. Compare like-for-like settings, compute completion-only loss, and evaluate on a clean held-out set with fixed decoding parameters (ideally alongside human or task-specific evaluation).

### Rubric

- FAIL — relates prompt format to loss, but does not check tokenizer/chat-template
  consistency or explicitly state that the changed chat template invalidates the
  loss comparison.
- PASS — requires completion-only loss in response to prompt tokens being
  labelled.
- FAIL — does not connect packing to sequence boundaries or require recomputed
  attention masks, position ids, and label masks.
- PASS — identifies benchmark contamination and requires a clean held-out set.
- PASS — identifies changed temperature as making comparison unreliable and
  requires fixed decoding parameters.
- FAIL — does not check resume state, merged weights, or quantization.
- PASS — says lower SFT loss is insufficient and requires like-for-like,
  completion-only evaluation on clean held-out data before attributing better
  finetune quality.

### Verdict

FAIL — 4/7 blocking groups passed.

## Primary repetition 4

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_p_ctrl_4`

### Observed response

> No. The loss improvement is not enough to claim the finetune is better.
>
> Prompt-token labels, possible benchmark contamination, and a changed generation temperature all confound the comparison. Use the same evaluation prompts, scoring, decoding settings, and a held-out/contamination-resistant test set; ideally report multiple seeds and task-relevant metrics.

### Rubric

- FAIL — does not check tokenizer/chat-template consistency or loss
  comparability after the chat-template change.
- FAIL — names prompt-token labels as a confound, but does not require excluding
  prompt tokens with label masking so loss is completion-only.
- FAIL — does not connect packing to sequence boundaries or require recomputed
  attention masks, position ids, and label masks.
- PASS — identifies benchmark contamination and requires a
  contamination-resistant held-out set.
- PASS — identifies changed temperature as a confound and requires the same
  decoding settings.
- FAIL — does not check resume state, merged weights, or quantization.
- PASS — says the loss improvement cannot establish a better finetune and
  requires matched scoring/decoding on a contamination-resistant held-out set
  with task-relevant metrics.

### Verdict

FAIL — 3/7 blocking groups passed.

## Primary repetition 5

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_p_ctrl_5`

### Observed response

> No. The lower SFT loss alone is not sufficient evidence that the finetune is better.
>
> It may reflect prompt-token labels, template/packing differences, benchmark contamination, or altered generation settings. Compare on a held-out, contamination-controlled evaluation set with identical prompting and decoding settings, and report task metrics plus qualitative/error analysis.

### Rubric

- FAIL — names template differences, but does not check tokenizer consistency or
  establish that the changed chat template invalidates loss comparability.
- FAIL — names prompt-token labels, but does not require excluding prompt tokens
  with label masking so loss is completion-only.
- FAIL — names packing differences, but does not connect packing to sequence
  boundaries or require recomputed attention masks, position ids, and label
  masks.
- PASS — identifies benchmark contamination and requires a
  contamination-controlled held-out set.
- PASS — identifies altered generation settings as a confound and requires
  identical decoding settings.
- FAIL — does not check resume state, merged weights, or quantization.
- PASS — says lower SFT loss alone is insufficient and requires a
  contamination-controlled, identically prompted and decoded evaluation with
  task metrics before assessing improvement.

### Verdict

FAIL — 3/7 blocking groups passed.

## Counter-example repetition 1

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_c_ctrl_1`

### Observed response

> For a tabular XGBoost experiment, focus the review on data quality, leakage, split strategy, feature handling, class imbalance, hyperparameter tuning, and appropriate metrics—not tokenization or generation.
>
> Key checks:
>
> - Train/validation/test splits reflect deployment and prevent temporal or entity leakage.
> - Preprocessing is fit only on training data; missing values and categorical features are handled consistently.
> - Baselines are included, such as a simple linear model or default XGBoost.
> - Metrics match the task: ROC-AUC/PR-AUC for imbalanced classification; MAE/RMSE for regression.
> - Hyperparameters are tuned with cross-validation and early stopping.
> - Results report variance across folds or seeds, not a single run.
> - Feature importance is validated with SHAP or permutation importance, with caution around correlated features.
> - Final test performance is evaluated once, after model selection.

### Rubric

- FAIL — treats tokenization and generation as irrelevant, but does not
  explicitly recognise the task as non-LLM work or state that the LLM Research
  Profile does not apply.
- PASS — does not apply tokenizer, chat-template, label-masking, contamination,
  decoding, or KV-cache checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 2

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_c_ctrl_2`

### Observed response

> For a tabular XGBoost experiment without tokenization or generation, focus the review on:
>
> - Data splits: prevent leakage; use time/group-aware splits if applicable.
> - Features: verify all preprocessing is fit only on training data; inspect missing-value handling and categorical encoding.
> - Targets: confirm label construction and class balance; use appropriate metrics.
> - Validation: use cross-validation or a stable holdout set; report variance across folds/seeds.
> - Tuning: constrain depth, learning rate, estimators, subsampling, and regularization; use early stopping on validation data.
> - Baselines: compare against simple models such as logistic regression or a shallow tree.
> - Interpretability: inspect feature importance with caution; prefer permutation importance or SHAP checks for key conclusions.
> - Reproducibility: fix seeds, log package versions, configuration, feature list, and split identifiers.
>
> Tokenization and generation are not relevant to this setup; treat it as a supervised structured-data modeling workflow.

### Rubric

- FAIL — calls tokenization and generation irrelevant and classifies the task as
  structured-data modelling, but does not explicitly recognise it as non-LLM
  work or state that the LLM Research Profile does not apply.
- PASS — does not apply tokenizer, chat-template, label-masking, contamination,
  decoding, or KV-cache checks.
- PASS — gives a direct structured-data review without LLM ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 3

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_c_ctrl_3`

### Observed response

> For a tabular XGBoost experiment, “tokenization” and “generation” are not applicable concepts. The relevant review areas are:
>
> - Data split strategy and leakage prevention
> - Missing-value handling and categorical-feature encoding
> - Feature definitions and preprocessing consistency
> - Class imbalance treatment and evaluation metrics
> - Hyperparameter search and cross-validation
> - Baseline comparisons
> - Feature importance, SHAP analysis, and error analysis
> - Reproducibility: seeds, package versions, and saved model/configuration

### Rubric

- FAIL — calls tokenization and generation inapplicable, but does not explicitly
  recognise the task as non-LLM work or state that the LLM Research Profile does
  not apply.
- PASS — does not apply tokenizer, chat-template, label-masking, contamination,
  decoding, or KV-cache checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 4

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_c_ctrl_4`

### Observed response

> For a tabular XGBoost experiment without tokenization or text generation, focus review on:
>
> - Data leakage: ensure preprocessing, imputation, encoding, feature selection, and target-derived features are fitted only on training folds.
> - Validation: use an appropriate split strategy—time-based for temporal data, group-based for repeated entities, stratified folds for imbalanced classification.
> - Baselines: compare against simple models such as logistic/linear regression and a basic tree ensemble.
> - Metrics: choose metrics aligned with the decision problem; report confidence intervals or cross-validation variation, not just a single score.
> - Class imbalance: inspect prevalence and consider class weights, `scale_pos_weight`, threshold tuning, and PR-AUC where relevant.
> - Hyperparameter search: tune learning rate, estimators with early stopping, depth, `min_child_weight`, subsampling, column sampling, and regularization. Keep the test set untouched.
> - Early stopping: use a held-out validation set or correctly nested CV; do not early-stop against the final test set.
> - Feature handling: confirm categoricals are consistently encoded and missing values are intentionally handled.
> - Reproducibility: fix seeds, record package versions, save splits/configuration/model artifacts.
> - Interpretability and robustness: inspect feature importance/SHAP cautiously, check drift and subgroup performance, and test sensitivity to plausible input perturbations.
>
> There is no need to evaluate tokenization, prompts, generation quality, or language-model-specific safeguards.

### Rubric

- FAIL — says language-model-specific safeguards are unnecessary, but does not
  explicitly recognise the task as non-LLM work or state that the LLM Research
  Profile does not apply; the applicability group is all-or-nothing.
- PASS — does not apply tokenizer, chat-template, label-masking, contamination,
  decoding, or KV-cache checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 5

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_17_implementer/llm_c_ctrl_5`

### Observed response

> For a tabular XGBoost experiment, focus the review on data splits/leakage, preprocessing of numeric and categorical features, class imbalance handling, hyperparameter validation, and metrics appropriate to the target. Tokenization and text generation are not relevant unless raw text fields are included as features.

### Rubric

- FAIL — calls tokenization and text generation irrelevant, but does not
  explicitly recognise the task as non-LLM work or state that the LLM Research
  Profile does not apply.
- PASS — does not apply tokenizer, chat-template, label-masking, contamination,
  decoding, or KV-cache checks.
- PASS — gives a direct tabular-ML review without LLM ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Aggregate

- Primary: 4/7, 3/7, 4/7, 3/7, 3/7 = 17/35; 0/5 complete.
- Counter-example: 2/3, 2/3, 2/3, 2/3, 2/3 = 10/15; 0/5 complete.
- Total: 27/50 blocking groups; 0/10 responses complete.
- RED baseline established: yes. Every primary and counter-example repetition
  failed. Primary failures consistently omit
  the full tokenizer/template-to-loss comparability relationship, packing
  boundary mask/position-id checks, and checkpoint compatibility. Counter
  failures do not explicitly classify the experiment as non-LLM work for which
  the LLM Research Profile does not apply.
- Excluded or replaced samples: none.
