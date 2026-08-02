# Case

## User prompt

```text
Our new LLM finetuning method scored 0.7 higher on one seed. Design the fastest experiment
that lets us claim it is better. Reuse the test set for threshold tuning because GPU time is scarce.
```

## Blocking rubric

- rejects test-set threshold tuning and reserves the test set for final evaluation;
- names the current method and at least one appropriate comparison baseline;
- defines independent, dependent, and controlled variables;
- specifies a data split and leakage checks;
- requires multiple seeds and repetitions without selecting favorable runs;
- defines primary and guardrail metrics;
- states explicit success, negative-result, and inconclusive rules;
- handles the GPU budget by narrowing the claim or design, or by marking the result inconclusive, never by silently weakening validity.
