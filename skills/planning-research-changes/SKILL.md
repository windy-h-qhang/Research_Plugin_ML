---
name: planning-research-changes
description: Use when approved research or AI infrastructure work needs decomposition into independently verifiable implementation and experiment tasks
---

# Planning Research Changes

## Core rule

Make each task the smallest coherent unit worth an independent reviewer
verdict, never an arbitrary time slice. User instructions set outcomes and
constraints; professionally refuse a requested decomposition or concurrency
method that would destroy verifiability, and provide the closest safe plan.

## Build the plan

Separate algorithm implementation, systems integration, each formal
experiment or ablation, and reporting whenever one can be accepted or rejected
without the others. Do not group independently interpretable ablations.
Order tasks by their artifact dependencies.

Write every task as this complete block; use a concrete value or explicit
`TBD`, never omit a field:

- **Task:** Coherent outcome and reviewer verdict.
- **Consumes:** Approved specifications, interfaces, code, data, and upstream artifacts.
- **Produces:** Reviewable code, configuration, results, or report artifact.
- **Files:** Exclusive file/module boundaries and shared files touched.
- **Validation:** Acceptance checks, commands or measurements, and pass criteria.
- **Budget:** Time, CPU/GPU, node, storage, download, scheduler, and paid-resource limits.
- **Environment:** Local, SSH, Slurm, or cloud execution target plus checkout/worktree isolation.
- **Evidence:** Durable test output, benchmark, run record, logs, result table, or rendered artifact proving the verdict.

Validation proves the task's own outcome. A scaffold or elapsed time is not
completion evidence. Mark unapproved or unaffordable validation as blocked,
not silently complete.

For SSH targets, use the existing project sync mechanism. If none exists,
propose and confirm a method before any remote overwrite; record the exact
remote repository path and allowed operations without exposing credentials.

## Concurrency boundary

- Serialize every write in a shared checkout. Non-overlapping files do not
  make concurrent shared-worktree writes safe.
- Parallelize independent read-only investigation.
- Parallelize writes only in isolated worktrees when `Consumes`, `Produces`,
  `Files`, and merge/integration order define explicit interfaces.
- Keep downstream experiments and figures blocked on the exact upstream
  artifacts they consume.

## Example task

- **Task:** Validate Triton kernel correctness independently of FSDP.
- **Consumes:** Locked attention semantics and reference implementation.
- **Produces:** Kernel plus correctness tests.
- **Files:** `kernels/attention.py`, `tests/test_attention.py`.
- **Validation:** Compare supported shapes/dtypes to the reference within declared tolerances; all cases pass.
- **Budget:** CPU tests plus one local-GPU smoke run under ten minutes.
- **Environment:** Isolated worktree; one available local GPU.
- **Evidence:** Test transcript, tolerance table, and environment fingerprint.

## Common mistakes

| Pressure | Required response |
|---|---|
| “Make every task two minutes” | Reject arbitrary slicing; put estimates in `Budget`. |
| “All agents in one checkout” | Serialize writes; parallelize read-only work. |
| “Files do not overlap” | Still isolate parallel writers and define interfaces. |
| “One experiment task” | Split independently interpretable ablations. |

## Red flags

Stop and revise if a task is merely “scaffold,” lacks any required field,
combines separable verdicts, treats a smoke test as research evidence, or
allows concurrent writers in one checkout.
