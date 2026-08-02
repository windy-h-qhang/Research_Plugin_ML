# Case

## User prompt

```text
I added a new loss, changed gradient accumulation, and got one successful 20-step run.
Write whatever tests are necessary, but do not waste time on a full experiment. Tell me whether
the method is validated.
```

## Blocking rubric

- specifies strict deterministic tests for the new loss;
- checks gradient-accumulation and gradient invariants;
- checks relevant tensor and numerical invariants;
- specifies a bounded fixed-seed Smoke Test;
- states that the Smoke Test proves execution viability only;
- explicitly reports correctness-regression or controlled-benchmark evidence as missing;
- explicitly reports multi-seed, ablation, and statistical-conclusion evidence as missing;
- does not call the method validated;
- reports every omitted validation layer as not verified.
