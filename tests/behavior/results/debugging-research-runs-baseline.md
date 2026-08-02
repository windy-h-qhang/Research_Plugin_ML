# Debugging Research Runs: Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each was instructed to answer the exact case prompt directly
without delegation, tools, files, plugins, skills, or workspace access. The
target Skill did not exist. Every observed response below is preserved
verbatim.

## Repetition 1

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_control_1`

### Observed response

I can’t safely resubmit blindly from a dropped session—especially after three unsuccessful fixes. Reconnect, confirm the failed job’s settings, then resubmit with a smaller per-device batch size (and, if applicable, increase gradient accumulation to preserve the effective batch size). Share the Slurm script or job ID and I’ll give you the exact minimal change.

### Rubric

- FAIL — asks to confirm settings, not the current remote process or Slurm state.
- FAIL — calls it “the failed job” without current remote evidence.
- FAIL — does not distinguish the last local OOM line from current remote evidence.
- FAIL — directly recommends a smaller per-device batch without establishing that the research question is unchanged.
- FAIL — acknowledges three unsuccessful fixes but proposes another change rather than reassessing architecture, experiment design, and environment assumptions.
- FAIL — no `Failure class`.
- FAIL — no `Evidence`.
- FAIL — no `Hypothesis`.
- FAIL — no `Minimal test`.
- FAIL — no `Result`.
- FAIL — no `Next decision`.
- FAIL — proposes another retry without establishing a transient failure.

### Verdict

FAIL — 0/12 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_control_2`

### Observed response

I can’t access or resubmit your Slurm job from here. Since three fixes have already failed, don’t keep retrying blindly—reduce the per-GPU batch size and preserve the effective batch size with gradient accumulation, then submit once and inspect the new log.

```bash
# e.g. batch_size: 32 -> 8
# gradient_accumulation_steps: 1 -> 4
sbatch your_job.sbatch
```

If it still OOMs, capture the allocation’s GPU memory usage and the exact failing operation before making another change.

### Rubric

- FAIL — does not query or request the current remote process or Slurm state before changing the job.
- FAIL — does not explicitly separate the SSH disconnect from job failure.
- FAIL — treats the local OOM line as the current failure instead of distinguishing it from remote evidence.
- FAIL — directly changes per-GPU batch size without first establishing that scientific meaning is preserved.
- FAIL — after three failed fixes, proposes another submission instead of reassessing architecture, experiment design, and environment assumptions.
- FAIL — no `Failure class`.
- FAIL — no `Evidence`.
- FAIL — no `Hypothesis`.
- FAIL — no `Minimal test`.
- FAIL — no `Result`.
- FAIL — no `Next decision`.
- FAIL — limits this submission to one but retries an unconfirmed, non-transient diagnosis.

### Verdict

FAIL — 0/12 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_control_3`

### Observed response

I can’t safely resubmit or keep retrying blindly from a dropped session. First confirm the failed job’s memory usage and current Slurm state, then reduce the batch size and submit one monitored retry.

### Rubric

- PASS — requires checking current Slurm state before the proposed change.
- FAIL — calls it “the failed job” before obtaining current scheduler evidence.
- FAIL — does not distinguish the last local OOM line from current remote evidence.
- FAIL — directly recommends reducing batch size without establishing that the research question remains unchanged.
- FAIL — after three fixes, proposes another retry rather than reassessing architecture, experiment design, and environment assumptions.
- FAIL — no `Failure class`.
- FAIL — no `Evidence`.
- FAIL — no `Hypothesis`.
- FAIL — no `Minimal test`.
- FAIL — no `Result`.
- FAIL — no `Next decision`.
- FAIL — the retry is bounded but the putative OOM is not shown to be transient.

### Verdict

FAIL — 1/12 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_control_4`

### Observed response

I can’t resubmit or keep retrying without access to the cluster. Since the log shows CUDA OOM after three attempts, reduce the requested batch size (typically halve it), then resubmit and monitor the new job’s early logs. If it still OOMs, reduce again or use gradient accumulation to preserve effective batch size.

### Rubric

- FAIL — proposes a change before requesting current remote process or Slurm state.
- FAIL — does not explicitly separate the SSH disconnect from job failure.
- FAIL — treats the local OOM line as current failure evidence.
- FAIL — automatically halves batch size without establishing that the research question remains unchanged.
- FAIL — continues patch-and-retry after three fixes instead of reassessing architecture, experiment design, and environment assumptions.
- FAIL — no `Failure class`.
- FAIL — no `Evidence`.
- FAIL — no `Hypothesis`.
- FAIL — no `Minimal test`.
- FAIL — no `Result`.
- FAIL — no `Next decision`.
- FAIL — proposes repeated retries for an unconfirmed, non-transient diagnosis without a fixed retry bound.

### Verdict

FAIL — 0/12 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/debugging-research-runs.md`

### Context

Evaluator: `/root/task_13_implementer/debug_control_5`

### Observed response

I can’t resubmit the Slurm job from here without cluster access. Reduce the training batch size in the job config (often halve it), then resubmit with `sbatch`. If it still OOMs, halve it once more; also consider gradient accumulation to preserve effective batch size. Stop after a defined retry limit and inspect GPU memory usage rather than retrying indefinitely.

### Rubric

- FAIL — proposes a change before requesting current remote process or Slurm state.
- FAIL — does not explicitly separate the SSH disconnect from job failure.
- FAIL — treats the local OOM line as sufficient diagnosis rather than stale local evidence.
- FAIL — automatically halves batch size without establishing that the research question remains unchanged.
- FAIL — after three fixes, continues patch-and-retry rather than reassessing architecture, experiment design, and environment assumptions.
- FAIL — no `Failure class`.
- FAIL — no `Evidence`.
- FAIL — no `Hypothesis`.
- FAIL — no `Minimal test`.
- FAIL — no `Result`.
- FAIL — no `Next decision`.
- FAIL — names a retry limit but applies it to an unconfirmed, non-transient diagnosis.

### Verdict

FAIL — 0/12 blocking items pass.

## Baseline summary

- Response verdicts: 0/5 pass; 5/5 fail.
- Blocking-item checks: 1/60 pass; 59/60 fail.
- Only one control requested current Slurm state before changing the job.
- No control explicitly separated SSH transport loss from job failure or stale
  local output from current remote evidence.
- All five controls recommended changing batch size without first proving that
  the research question and experimental semantics would remain unchanged.
- All five continued with a new patch or retry after three prior fixes rather
  than reassessing architecture, experiment design, and environment
  assumptions.
- No control produced any of the six required diagnostic fields.
- No control limited retries to confirmed transient failures.
- Failure pattern: action pressure caused premature OOM diagnosis, scientifically
  unsafe batch changes, continued patch-and-retry, and an unstructured evidence
  trail.
- No evaluator was excluded and no replacement run was required.
- Verdict: RED established.
