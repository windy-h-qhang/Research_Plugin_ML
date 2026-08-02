---
name: orchestrating-research-agents
description: Use when research work can benefit from implementer and reviewer roles, independent investigations, or multi-agent execution
---

# Orchestrating Research Agents

Assign roles by mode and risk before dispatch:

Honor explicit safe user execution strategies, including stopping when
multi-agent is unavailable. Platform and shared-checkout safety remain binding.

| Mode or risk | Assignment |
|---|---|
| Exploration | One Implementer by default |
| Complex experiment | Implementer + Scientific Reviewer |
| Engineering | Implementer + Engineering Reviewer |
| Engineering that can change algorithm meaning | Add Scientific Reviewer |
| Release or explicit reproducibility scope | Add Reproducibility Reviewer |

Apply every matching row; reviewers accumulate.
Release engineering matches both Engineering and Release rows.
Use only `Implementer`, `Scientific Reviewer`, `Engineering Reviewer`, and
`Reproducibility Reviewer` as role names.

Add Scientific Reviewer only for complex experiments or explicit scope affecting
an algorithm, objective, data semantics, optimization, schedule, or evaluation.
Do not infer risk merely because engineering consumes a frozen specification.

Select Reproducibility Reviewer only for release or explicit reproducibility
scope.

## Safe execution

Never allow concurrent writers in one shared checkout. Serialize writes there.
Parallel writers require separate worktrees, explicit `Consumes`, `Produces`,
and file interfaces, then one-at-a-time integration and validation.

Parallelize only independent read-only investigation and review in shared state.
Reviewers inspect primary briefs, diffs, tests, run records, and artifacts;
Implementer summaries are not evidence.

Keep each responsible Implementer for findings until all reviews pass.
Never transfer one Implementer's fix ownership to another.
Close completed reviewers when possible; re-dispatch after fixes.

## Role contracts

Read and use the selected contracts:

- `implementer-prompt.md`
- `scientific-reviewer-prompt.md`
- `engineering-reviewer-prompt.md`
- `reproducibility-reviewer-prompt.md`

Every reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

If multi-agent is unavailable, obey an explicit user stop or safe fallback.
Without a preference, one agent
executes the selected role contracts sequentially: Implementer, each applicable
reviewer, Implementer fix rounds, and re-review. Report reduced review
independence.

## Orchestration output

Return these four sections for every assignment:

1. **Assignments:** Derive scopes from the brief. Give cohesive shared-checkout
   work exactly one Implementer. Use separate Implementers only for independent
   isolated units; label each writer's `Consumes`, `Produces`, and `Files`, then
   state integration order. Assign every matching reviewer now and state whether
   Reproducibility Reviewer is selected.
2. **Execution:** State: “Independent read-only investigations and reviews may
   run in parallel.” State: “Concurrent writes in one shared checkout are
   prohibited.” Name isolated writers'
   interfaces and serial integration order.
3. **Review cycle:** State: “Each responsible Implementer remains available to
   fix findings until reviews pass; fix ownership never transfers.” State:
   “Implementer summaries are context, never evidence; reviewers
   inspect primary artifacts.” Require the exact five-field reviewer output.
4. **Fallback:** State whether an explicit user stop/fallback instruction is
   being honored. With no preference, give the sequential single-agent stages
   and end with “This fallback has reduced review independence.”
