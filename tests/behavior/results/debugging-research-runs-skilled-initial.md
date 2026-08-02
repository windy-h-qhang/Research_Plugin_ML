# Debugging Research Runs: Initial Skilled Regression

These fresh evaluators used model `gpt-5.6-terra` with reasoning effort
`medium`. Each received only the initial Skill and the unchanged case prompt,
and was instructed to answer directly without delegation, tools, files,
plugins, other skills, or workspace access. No evaluator received the rubric
or an expected answer. Both responses are preserved verbatim. They are
regression evidence and are not part of the final post-edit acceptance arm.

## Initial repetition 1

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_skilled_1`

### Observed response

**Failure class:** unknown

**Evidence:** Current Slurm/process state: unknown — SSH disconnected and no job ID or scheduler query is available. Last local log before disconnect: CUDA OOM; this is stale until corroborated remotely. Three prior fixes were already attempted.

**Hypothesis:** The run exceeded GPU memory, but the job may also have completed, been preempted, or still be running.

**Minimal test:** Reconnect and run a read-only `squeue`/`sacct` query for the job, then inspect the remote log for OOM confirmation.

**Result:** pending

**Next decision:** If accounting confirms CUDA OOM, do not change batch size or resubmit without confirming that it preserves the experiment’s intended comparison; request that scientific decision. If it shows a transient scheduler/node/network failure, retry at most a pre-set finite number of times. Since three fixes have already failed, stop further patching and retries pending reassessment.

### Rubric

- PASS — makes the current remote process or scheduler query the first diagnostic action.
- PASS — says only the SSH transport was lost and leaves job state unknown.
- PASS — labels the local OOM line stale pending remote corroboration.
- PASS — refuses to change batch automatically without preserving experimental meaning.
- FAIL — stops after three fixes but says only “pending reassessment”; it does not explicitly reassess architecture, experiment design, and environment assumptions.
- FAIL — outputs `Failure class` but uses `unknown`, which is outside the required classification set.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without inventing evidence.
- PASS — outputs `Next decision`.
- PASS — permits only a finite retry after confirmed transient scheduler, node, or network failure.

### Verdict

FAIL — 10/12 blocking items pass.

## Initial repetition 2

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_skilled_2`

### Observed response

**Failure class:** unknown

**Evidence:** Last local log before the SSH disconnect reported CUDA OOM; current Slurm job/process/accounting state is unknown. SSH loss does not establish that the run failed.

**Hypothesis:** The active run was terminated by GPU memory exhaustion.

**Minimal test:** Read-only query of the job’s current Slurm state and accounting (`squeue`/`sacct`), plus the latest remote log.

**Result:** pending

**Next decision:** If accounting confirms CUDA OOM, do not retry unchanged; assess whether reducing batch size preserves the experiment’s intended comparison, and request that scientific decision if it does not. If the job is still running, reconnect and observe. If it was a transient scheduler/node failure, retry with a pre-set finite limit.

Because three fixes have already failed, stop patching, resubmitting, and parameter changes until the run state and failure cause are reassessed.

### Rubric

- PASS — makes a read-only Slurm and remote-log query the minimal first test.
- PASS — explicitly says SSH loss does not establish job failure.
- PASS — separates the last local OOM line from unknown current remote state.
- PASS — does not change batch automatically and protects the intended comparison.
- FAIL — stops further changes but does not explicitly reassess architecture, experiment design, and environment assumptions.
- FAIL — outputs `Failure class` but uses `unknown`, which is outside the required classification set.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without inventing evidence.
- PASS — outputs `Next decision`.
- PASS — permits only a finite retry after confirmed transient scheduler or node failure.

### Verdict

FAIL — 10/12 blocking items pass.

## Regression summary

- Response verdicts: 0/2 pass.
- Blocking-item checks: 20/24 pass.
- Both responses used a non-enumerated failure class when the current run state
  was unknown.
- Both stopped further attempts but compressed the required architectural,
  experimental, and environmental reassessment into a generic phrase.
- The revision must define classification under uncertainty and make the
  three-part reassessment an explicit output requirement.
