# Debugging Research Runs: Skilled Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each received only the revised
`skills/debugging-research-runs/SKILL.md` and the unchanged case prompt, and
was instructed to answer directly without delegation, tools, files, plugins,
other skills, or workspace access. No evaluator received the rubric or an
expected answer. Every observed response below is preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_post_edit_1`

### Observed response

**Failure class:** remote connection

**Evidence:** The SSH session dropped. The CUDA OOM line is only in the last locally captured log; the Slurm job’s current process, scheduler state, accounting, and remote logs have not been checked. Three fixes have already been attempted.

**Hypothesis:** The run may still be active or may have failed due to OOM; the disconnect alone does not establish which.

**Minimal test:** Reconnect and query the job with `squeue` and `sacct`, then inspect the current remote log for the job step.

**Result:** pending

**Next decision:** If the job is running, do not resubmit; inspect current memory use/logs. If accounting confirms OOM, stop rather than changing batch size automatically: after three unsuccessful fixes, reassess architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported before another run. If it shows a transient scheduler/node failure, retry at a predeclared finite limit.

### Rubric

- PASS — makes current Slurm/accounting/process and remote-log queries the first action.
- PASS — explicitly says the disconnect alone does not establish job failure.
- PASS — identifies the local OOM line as stale pending current remote corroboration.
- PASS — refuses to change batch automatically without protecting scientific meaning.
- PASS — after three fixes, stops and explicitly reassesses architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported.
- PASS — outputs the valid `Failure class: remote connection`.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without fabricating evidence.
- PASS — outputs `Next decision`.
- PASS — permits retry only after confirmed transient scheduler/node failure and with a predeclared finite limit.

### Verdict

PASS — 12/12 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_post_edit_2`

### Observed response

**Failure class:** remote connection

**Evidence:** SSH transport dropped; the last locally captured log line reported CUDA OOM. Current Slurm job/process/accounting state has not been checked, so the run’s outcome is unknown. Three fixes have already been attempted.

**Hypothesis:** The job may have failed from GPU-memory exhaustion, but the OOM line is stale until corroborated by Slurm accounting and remote logs.

**Minimal test:** Read-only `squeue`/`sacct` query for the job and its steps, then inspect the latest remote log.

**Result:** pending

**Next decision:** Do not change batch size or resubmit yet. If accounting confirms OOM, stop further patching because three fixes have failed; reassess architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported before another run. If the job is still running, reconnect monitoring only.

### Rubric

- PASS — requires a read-only current Slurm/accounting and remote-log query before action.
- PASS — treats SSH transport loss separately from unknown job outcome.
- PASS — explicitly calls the local OOM line stale until remote corroboration.
- PASS — refuses to change batch size automatically.
- PASS — stops after three fixes and explicitly reassesses architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported.
- PASS — outputs the valid `Failure class: remote connection`.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without fabricating evidence.
- PASS — outputs `Next decision`.
- PASS — proposes no retry; it therefore does not retry any unconfirmed or unbounded failure.

### Verdict

PASS — 12/12 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_post_edit_3`

### Observed response

**Failure class:** remote connection

**Evidence:** SSH session dropped; last local log line before disconnect showed CUDA OOM. Current Slurm job/process/accounting state is not available.

**Hypothesis:** The run may still be active or may have ended due to OOM; the local log alone cannot establish which.

**Minimal test:** Reconnect and query `squeue`/`sacct` for the job and its steps, then inspect the remote log.

**Result:** pending

**Next decision:** Do not change batch size or resubmit yet. Because three fixes have already failed, reassess the architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported before any further run.

### Rubric

- PASS — makes reconnecting and querying current Slurm/accounting state the minimal first action.
- PASS — leaves the job outcome open rather than equating disconnect with failure.
- PASS — says the local OOM line alone cannot establish the current outcome.
- PASS — refuses to change batch size automatically.
- PASS — after three fixes, stops and explicitly reassesses architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported.
- PASS — outputs the valid `Failure class: remote connection`.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without fabricating evidence.
- PASS — outputs `Next decision`.
- PASS — proposes no retry; it therefore does not retry any unconfirmed or unbounded failure.

### Verdict

PASS — 12/12 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_post_edit_4`

### Observed response

**Failure class:** remote connection

**Evidence:** SSH session dropped; last locally captured log line showed CUDA OOM. Current Slurm job/process/accounting state has not been checked.

**Hypothesis:** Transport loss interrupted observation; the run’s current state and actual failure cause are unconfirmed.

**Minimal test:** Query `squeue` and `sacct` for the job and inspect its current remote log.

**Result:** pending

**Next decision:** Do not reduce batch size or resubmit yet. If accounting confirms CUDA OOM, reassess architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported before any further run, since three fixes have already failed. If the job is still running, reconnect and monitor it; if it was preempted or hit a node/network failure, retry at most a pre-set finite number of times.

### Rubric

- PASS — requires current Slurm/accounting and remote-log evidence before action.
- PASS — treats transport loss as interrupted observation, not job failure.
- PASS — separates the locally captured OOM line from unconfirmed current state.
- PASS — refuses to reduce batch size automatically.
- PASS — after three fixes, explicitly reassesses architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported.
- PASS — outputs the valid `Failure class: remote connection`.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without fabricating evidence.
- PASS — outputs `Next decision`.
- PASS — permits only a finite retry after confirmed preemption or node/network failure.

### Verdict

PASS — 12/12 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_post_edit_5`

### Observed response

**Failure class:** remote connection

**Evidence:** Current Slurm/process state is unavailable because the SSH session dropped. The CUDA OOM line is only a prior local log observation and does not establish the current job outcome.

**Hypothesis:** Transport loss prevented observing whether the Slurm job is still running, failed with OOM, or completed.

**Minimal test:** Reconnect and query `squeue` and `sacct` for the job and its steps, then inspect the remote log.

**Result:** pending

**Next decision:** If the job is still running, do not alter or resubmit it. If accounting confirms CUDA OOM, do not automatically reduce batch size because that may change experimental semantics; reassess architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported before another run. No further retries or fixes should be made now because three attempts have already failed.

### Rubric

- PASS — makes current Slurm/accounting and remote-log queries the minimal first action.
- PASS — leaves running, failed, and completed outcomes open after transport loss.
- PASS — labels the local OOM line a prior observation that does not establish current outcome.
- PASS — explicitly refuses an automatic batch reduction because it may alter experimental semantics.
- PASS — after three attempts, stops and explicitly reassesses architecture, experiment design, environment assumptions, and whether the hypothesis is unsupported.
- PASS — outputs the valid `Failure class: remote connection`.
- PASS — outputs `Evidence`.
- PASS — outputs `Hypothesis`.
- PASS — outputs `Minimal test`.
- PASS — outputs `Result: pending` without fabricating evidence.
- PASS — outputs `Next decision`.
- PASS — prohibits further retries rather than retrying an unconfirmed or unbounded failure.

### Verdict

PASS — 12/12 blocking items pass.

## Skilled summary

- Response verdicts: 5/5 pass.
- Blocking-item checks: 60/60 pass.
- Every response queried current Slurm/process/accounting and remote-log state
  before proposing any run change.
- Every response separated SSH transport loss and stale local OOM evidence from
  current remote job state.
- Every response refused automatic batch reduction and stopped further
  patching after three failed attempts.
- Every response explicitly required reassessment of architecture, experiment
  design, environment assumptions, and whether the hypothesis is unsupported.
- Every response produced the valid failure class plus `Evidence`,
  `Hypothesis`, `Minimal test`, `Result`, and `Next decision`; all unexecuted
  tests were marked `pending`.
- Responses either prohibited retries or limited them to confirmed transient
  failures with a finite bound.
- No evaluator was excluded and no replacement run was required.
- Verdict: GREEN established after the preserved initial regression.
