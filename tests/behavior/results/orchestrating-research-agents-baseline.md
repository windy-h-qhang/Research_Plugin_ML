# Orchestrating Research Agents: Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each was instructed to answer the exact case prompt directly
without delegation, tools, files, plugins, skills, or workspace access. The
target Skill did not exist. Every observed response below is preserved
verbatim.

## Repetition 1

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_control_1`

### Observed response

I can coordinate four agents, but not safely have all of them edit the same checkout at once. Use isolated worktrees for the training loop and FSDP changes; reserve the other agents for test fixes and review after those changes land.

### Rubric

- PASS — explicitly rejects all four agents editing the same checkout concurrently.
- FAIL — suggests isolated worktrees but defines no explicit interfaces or serial integration order.
- FAIL — does not identify independent read-only work that may run in parallel.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — does not assign an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for the training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — does not require reviewers to be read-only, independent, or evidence-based.
- FAIL — gives no sequential single-agent fallback when multi-agent is unavailable.
- FAIL — does not report reduced review independence in fallback.
- FAIL — does not clearly assign the named Implementer and reviewer roles.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 2/12 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_control_2`

### Observed response

I’ll run all four roles in parallel against the same checkout: training loop, FSDP wrapper, test fixes, and review. Changes will be coordinated by file ownership to avoid overwriting each other.

### Rubric

- FAIL — accepts concurrent writes in one shared checkout.
- FAIL — relies on file ownership rather than serial writes or isolated writers with explicit interfaces and serial integration.
- FAIL — parallelizes writing rather than limiting parallelism to independent read-only work.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — does not assign an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for the training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — the generic reviewer is neither declared read-only and independent nor required to inspect primary evidence.
- FAIL — gives no sequential single-agent fallback when multi-agent is unavailable.
- FAIL — does not report reduced review independence in fallback.
- FAIL — describes activities rather than clearly assigning the named role contracts.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 1/12 blocking items pass.

## Repetition 3

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_control_3`

### Observed response

I can’t safely have four agents edit the same checkout concurrently; their changes and test fixes can overwrite each other. Multi-agent work is available, but it needs isolated workspaces. If the same checkout is mandatory, I’ll stop here.

### Rubric

- PASS — explicitly rejects concurrent editing in one shared checkout.
- FAIL — mentions isolated workspaces but gives no explicit interfaces or serial integration order.
- FAIL — does not identify independent read-only work that may run in parallel.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — does not assign an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for the training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — does not require reviewers to be read-only, independent, or evidence-based.
- FAIL — stopping is the opposite of the required sequential single-agent fallback.
- FAIL — does not report reduced review independence in fallback.
- FAIL — does not clearly assign the named Implementer and reviewer roles.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 2/12 blocking items pass.

## Repetition 4

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_control_4`

### Observed response

I can’t safely have multiple agents edit the same checkout in parallel; their changes can overwrite or conflict unpredictably. Use separate worktrees/checkouts for the training loop, FSDP wrapper, test fixes, and review, then integrate the reviewed changes.

### Rubric

- PASS — explicitly rejects concurrent editing in one shared checkout.
- FAIL — separates workspaces but defines neither explicit interfaces nor a serial integration order.
- FAIL — does not identify independent read-only work that may run in parallel.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — does not assign an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for the training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — does not make the generic review read-only, independent, or based on primary evidence.
- FAIL — gives no sequential single-agent fallback when multi-agent is unavailable.
- FAIL — does not report reduced review independence in fallback.
- FAIL — does not clearly assign the named Implementer and reviewer roles.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 2/12 blocking items pass.

## Repetition 5

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_control_5`

### Observed response

I can’t safely have four agents edit the same checkout concurrently; their changes could overwrite or conflict. Use isolated worktrees for the training loop, FSDP wrapper, tests, and review, then merge the validated changes.

### Rubric

- PASS — explicitly rejects concurrent editing in one shared checkout.
- FAIL — separates workspaces but defines neither explicit interfaces nor a serial integration order.
- FAIL — does not identify independent read-only work that may run in parallel.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — does not assign an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for the training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — does not make the generic review read-only, independent, or based on primary evidence.
- FAIL — gives no sequential single-agent fallback when multi-agent is unavailable.
- FAIL — does not report reduced review independence in fallback.
- FAIL — does not clearly assign the named Implementer and reviewer roles.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 2/12 blocking items pass.

## Baseline summary

- Response verdicts: 0/5 pass; 5/5 fail.
- Blocking-item checks: 9/60 pass; 51/60 fail.
- Four controls rejected concurrent shared-checkout writes; one explicitly
  accepted them and relied on file ownership.
- No control defined explicit writer interfaces plus serial integration or
  limited parallelism to independent read-only investigations.
- No control assigned the required Engineering Reviewer and Scientific
  Reviewer for this engineering task with training-loop semantic risk.
- No control kept an Implementer for review fixes, defined independent
  evidence-based review, or required the five-field reviewer verdict.
- No control provided the sequential single-agent fallback or disclosed its
  reduced review independence.
- No control added a Reproducibility Reviewer without release scope.
- Failure pattern: generic worktree safety appeared without the mode/risk role
  selection, review lifecycle, fallback, and output contracts needed for
  research orchestration.
- No evaluator was excluded and no replacement run was required.
- Verdict: RED established.
