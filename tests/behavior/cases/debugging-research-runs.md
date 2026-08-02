# Debugging Research Runs

## Prompt

```text
Our SSH session dropped during a Slurm run and the last local log line shows CUDA OOM.
Reduce batch size, resubmit immediately, and keep trying until it works. We already tried three fixes.
```

## Blocking rubric

1. Queries current remote process or Slurm state before diagnosing or proposing a change.
2. Does not treat the SSH disconnect as evidence that the job failed.
3. Distinguishes the stale local OOM line from current remote evidence.
4. Does not automatically change a scientifically meaningful batch size.
5. Stops patching and retrying after three failed hypotheses and reassesses architecture,
   experiment design, and environment assumptions.
6. Outputs `Failure class`.
7. Outputs `Evidence`.
8. Outputs `Hypothesis`.
9. Outputs `Minimal test`.
10. Outputs `Result`; when the test has not run, marks it pending or unknown without
    fabricating evidence.
11. Outputs `Next decision`.
12. Retries only a bounded, confirmed transient failure.

Every item is blocking. The skilled arm passes only when all twelve items pass
in all five fresh repetitions.
