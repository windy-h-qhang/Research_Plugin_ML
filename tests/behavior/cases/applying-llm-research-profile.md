# Case

## Primary prompt

```text
After changing the chat template and packing, SFT loss improved. Labels include prompt tokens, the benchmark examples may appear in pretraining data, and generation temperature changed. Can we claim the finetune is better?
```

## Primary blocking rubric

- checks tokenizer/chat template consistency and warns that changing the chat template invalidates loss comparison;
- verifies label masking excludes prompt tokens so loss is computed only on the completion;
- detects that packing changes sequence boundaries and requires recomputed attention masks, position ids, and label masks;
- identifies benchmark contamination in pretraining/finetuning data as a confound;
- notes that a generation temperature change invalidates a quality comparison and requires holding decoding settings constant;
- checks checkpoint compatibility (resume state, merged weights, quantization);
- limits the claim: lower SFT loss alone does not show that the finetune is
  better; after correcting template, packing, and masking, removing
  contamination, and fixing decoding/evaluator settings, requires a controlled
  quality evaluation before concluding improvement.

## Counter-example prompt

```text
Review a tabular XGBoost experiment that does not use tokenization or generation.
```

## Counter-example blocking rubric

- recognises that a tabular XGBoost task is not LLM work and the LLM Research Profile does not apply;
- does not apply LLM-specific checks (tokenizer, chat template, label masking, contamination, decoding settings, KV-cache);
- avoids irrelevant LLM ceremony for a non-language-model task.
