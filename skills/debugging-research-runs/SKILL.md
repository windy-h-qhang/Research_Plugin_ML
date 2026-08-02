---
name: debugging-research-runs
description: Use when training, evaluation, distributed, GPU, SSH, Slurm, or other research runs fail, hang, diverge, disconnect, time out, exhaust resources, or produce unexpected results
---

# Debugging Research Runs

Investigate before changing or rerunning anything. Preserve the research
question while distinguishing execution failures from unsupported hypotheses.

## Establish current state

For a remote or scheduled run, make the first action a read-only query of the
authoritative current state: reconnect and inspect the process, or query
`squeue` and `sacct` for the job and its steps. If access or the job identifier
is missing, request it and leave the state unknown.

An SSH disconnect proves only transport loss. A timeout proves only that an
observer stopped waiting. Neither diagnoses job failure. Treat local output
captured before a disconnect—including an OOM line—as stale evidence until
current remote process, scheduler, accounting, and remote-log evidence
corroborate it.

## Record one diagnostic cycle

Output exactly these fields before proposing any fix:

- **Failure class:** Choose exactly one; never write `unknown`: `code`, `data/experiment`,
  `numerical/device`, `environment`, `resource/scheduler`,
  `remote connection`, or `unsupported hypothesis`. Classify the evidence
  currently established, not a suspected hidden cause; use `remote connection`
  when transport loss prevents checking run state.
- **Evidence:** Separate observed facts by source and time; put the current
  process or scheduler query first for remote runs.
- **Hypothesis:** State one falsifiable cause supported by the evidence.
- **Minimal test:** Specify the smallest read-only check or one-variable test
  that distinguishes this hypothesis.
- **Result:** Record only observed output. If the test did not run, write
  `pending` or `unknown`; never invent a result.
- **Next decision:** State the conditional action for each possible result.

Test one hypothesis at a time. Reclassify when evidence points to another
layer; a scientifically valid negative result is `unsupported hypothesis`, not
automatically a code failure.

## Bound changes and retries

- Retry only a confirmed transient remote, network, preemption, node, or
  scheduler failure. Set a finite attempt limit before retrying.
- Do not retry code, data/experiment, numerical/device, environment, or
  unsupported-hypothesis failures unchanged.
- Change batch size, sequence length, precision, or device/distributed topology
  automatically only after explicitly establishing that the research question,
  experimental unit, optimization semantics, and intended comparison remain
  unchanged. Otherwise request a scientific decision.
- After three unsuccessful hypotheses or fixes, stop all patching, resubmission,
  and parameter changes. In `Next decision`, explicitly require reassessment of
  (1) architecture, (2) experiment design, (3) environment assumptions, and
  (4) whether the hypothesis is unsupported before another run.
