---
name: applying-llm-research-profile
description: Use when work involves language-model tokenization, pretraining, finetuning, alignment, generation, evaluation, checkpoints, PEFT, or LLM inference
---

# Applying the LLM Research Profile

Use this Profile only when the research question depends on language-model
tokenization, training, generation, evaluation, checkpoints, or inference.
For tabular XGBoost or other non-LLM work, state that the LLM Research Profile
does not apply and review it without tokenizer, template, masking,
contamination, decoding, or KV-cache ceremony.

## Comparison contract

For an LLM loss or quality comparison, answer with one explicit finding per
applicable group below. Preserve each cause-to-control relationship; do not
compress named controls into a generic statement that they are "controlled."
Treat multi-part groups as indivisible: the packing finding must name all three
recomputed masks/ids, and the checkpoint finding must name resume state, merged
weights, and quantization compatibility.

1. Pin the tokenizer revision, special tokens, and chat template. Changing the
   tokenizer or chat template changes the token sequence and loss support, so
   SFT losses across those settings are not comparable.
2. Verify label masking assigns the ignore index to prompt tokens so loss is
   computed only on assistant or completion tokens.
3. Treat packing and truncation as sequence-boundary changes. Recompute
   attention masks, position ids, and label masks, and prevent packed examples
   from attending across document boundaries.
4. Audit whether benchmark examples appear in pretraining or finetuning data.
   Contamination confounds evaluation; document data sources and splits.
5. Hold temperature and all other decoding and evaluator settings constant. A
   temperature change invalidates a direct generation-quality comparison.
6. Verify that the evaluated checkpoint is the intended training state. Check
   resume state, optimizer state, PEFT adapter versus merged weights, correct
   adapter folding, base-model revision, and quantization compatibility.
7. State the claim limit: confounded loss or evaluation evidence cannot show
   that the finetune is better.

When relevant, also check Accelerate, DeepSpeed/FSDP, PEFT/TRL, long-context
position handling, quantization, and KV-cache compatibility. Load another
Profile only for a separate relevant question; an LLM quality task alone does
not require the AI Infra Profile.
