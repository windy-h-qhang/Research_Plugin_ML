# Planning Research Changes: Baseline Results

All five evaluators used fresh context, model `gpt-5.6-terra`, and reasoning
effort `medium`. Each was instructed to answer the exact case prompt directly
without delegation, tools, files, or workspace access. The target Skill did not
exist. Every observed response below is preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/planning-research-changes.md`

### Context

Evaluator: `/root/task_11_implementer/planning_control_1`

### Observed response

Run all tasks in parallel from the same checkout, with exclusive file ownership to avoid conflicts:

| Time | Agent | Task |
|---|---|---|
| 0–2 min | Kernel | Scaffold the Triton attention kernel API and test stub. |
| 0–2 min | FSDP | Add the FSDP integration entry point and configuration wiring. |
| 0–2 min | Ablation A | Configure baseline-vs-no-attention ablation. |
| 0–2 min | Ablation B | Configure sequence-length ablation. |
| 0–2 min | Ablation C | Configure precision/block-size ablation. |
| 0–2 min | Figure | Create the paper-figure template, labels, and result-loading script. |
| 0–2 min | Coordinator | Define shared interfaces, assign non-overlapping files, and record commands/results. |

At minute 2, synchronize and run one integration pass. If any task needs code changes in a shared file, have the coordinator make that change to prevent checkout collisions.

### Rubric

- FAIL — follows the arbitrary two-minute slicing request instead of rejecting it in favor of independently verifiable units.
- FAIL — names the requested areas but reduces them to scaffolds and configuration fragments rather than coherent units that can receive independent reviewer verdicts.
- FAIL — no task explicitly declares `Consumes`.
- FAIL — no task explicitly declares `Produces`.
- FAIL — no task explicitly declares `Files`.
- FAIL — no task explicitly declares `Validation`.
- FAIL — no task explicitly declares `Budget`.
- FAIL — no task explicitly declares `Environment`.
- FAIL — no task explicitly declares `Evidence`.
- FAIL — still directs parallel writes in one shared checkout; reserving some shared-file changes for one coordinator does not serialize all shared-worktree writes.
- FAIL — permits parallel writes in one checkout based only on file ownership; it neither requires isolated worktrees with explicit interfaces nor limits same-checkout parallelism to read-only investigation.

### Verdict

FAIL — 0/11 blocking groups pass.

## Repetition 2

### Case

`tests/behavior/cases/planning-research-changes.md`

### Context

Evaluator: `/root/task_11_implementer/planning_control_2`

### Observed response

I’d avoid assigning fixed two-minute estimates or having multiple agents edit one checkout concurrently—both make the work less reliable. A safe parallel plan is:

1. Kernel track: implement and benchmark the Triton attention kernel.
2. Integration track: add FSDP support and a minimal distributed-training smoke test.
3. Experiment track: define and run the three ablations with shared logging conventions.
4. Figure track: prepare plotting code and the paper figure from the experiment outputs.
5. Validation track: compare kernel correctness/performance, verify FSDP behavior, and reproduce figure data.

Use separate worktrees or clearly non-overlapping files for the implementation tracks; merge after each track passes its checks. The figure work should start with a template, then finalize once ablation results land.

### Rubric

- PASS — professionally rejects fixed two-minute estimates as unreliable.
- FAIL — separates broad tracks but combines all three model ablations and validation into aggregate tracks instead of independently reviewable coherent units.
- FAIL — no task explicitly declares `Consumes`.
- FAIL — no task explicitly declares `Produces`.
- FAIL — no task explicitly declares `Files`.
- FAIL — no task explicitly declares `Validation`.
- FAIL — no task explicitly declares `Budget`.
- FAIL — no task explicitly declares `Environment`.
- FAIL — no task explicitly declares `Evidence`.
- PASS — rejects concurrent editing of one checkout and describes merges after track checks.
- FAIL — permits parallel writes in “clearly non-overlapping files” without requiring isolated worktrees and explicit interfaces.

### Verdict

FAIL — 2/11 blocking groups pass.

## Repetition 3

### Case

`tests/behavior/cases/planning-research-changes.md`

### Context

Evaluator: `/root/task_11_implementer/planning_control_3`

### Observed response

1. 0–2 min — Kernel agent: scaffold Triton attention kernel API and correctness test.
2. 0–2 min — FSDP agent: add integration wrapper and minimal distributed smoke test.
3. 0–2 min — Ablation agent A: configure baseline/no-attention variant.
4. 0–2 min — Ablation agent B: configure attention-design variant.
5. 0–2 min — Ablation agent C: configure FSDP/training-settings variant.
6. 0–2 min — Figure agent: draft the paper figure template and expected data schema.

All agents work concurrently in the same checkout, with exclusive file ownership to prevent conflicts: kernel code/tests, FSDP code/tests, each ablation config, and figure assets/script respectively.

7. 0–2 min — Joint checkpoint: run the smoke tests, reconcile interfaces, and collect ablation outputs into the figure template.

### Rubric

- FAIL — follows the arbitrary two-minute slicing request instead of rejecting it.
- FAIL — assigns requested areas to fragments and a two-minute checkpoint rather than coherent units with independent reviewer verdicts.
- FAIL — no task explicitly declares `Consumes`.
- FAIL — no task explicitly declares `Produces`.
- FAIL — no task explicitly declares `Files`.
- FAIL — no task explicitly declares `Validation`.
- FAIL — no task explicitly declares `Budget`.
- FAIL — no task explicitly declares `Environment`.
- FAIL — no task explicitly declares `Evidence`.
- FAIL — directs all agents to write concurrently in the shared checkout.
- FAIL — permits same-checkout parallel writes based only on file ownership and does not limit parallelism to read-only investigation or isolated worktrees with explicit interfaces.

### Verdict

FAIL — 0/11 blocking groups pass.

## Repetition 4

### Case

`tests/behavior/cases/planning-research-changes.md`

### Context

Evaluator: `/root/task_11_implementer/planning_control_4`

### Observed response

I’d use a shared checkout only for read-only work; kernel, FSDP, and ablation changes should land through separate branches/worktrees to avoid collisions.

- 2 min — Define the Triton attention kernel interface, supported shapes/dtypes, and correctness tests.
- 2 min — Scaffold the kernel implementation and benchmark harness.
- 2 min — Map the FSDP integration points, sharding policy, and checkpoint behavior.
- 2 min — Add FSDP configuration plumbing and a minimal distributed smoke test.
- 2 min — Specify three ablations: baseline, kernel-only, and FSDP-only (plus combined run if budget permits).
- 2 min — Prepare reproducible configs, seeds, metrics, and logging for all ablations.
- 2 min — Design the paper figure: axes, error bars, labels, and the comparison it must support.
- 2 min — Create the plotting script/template fed by experiment logs.

Then merge the scaffolding and run longer correctness, performance, and training jobs separately—those cannot realistically be completed in two minutes.

### Rubric

- FAIL — recognizes that substantive work exceeds two minutes but still structures every task as an arbitrary two-minute slice rather than an independently verifiable unit.
- FAIL — fragments implementation and combines the three ablations instead of defining coherent units with independent reviewer verdicts.
- FAIL — no task explicitly declares `Consumes`.
- FAIL — no task explicitly declares `Produces`.
- FAIL — no task explicitly declares `Files`.
- FAIL — no task explicitly declares `Validation`.
- FAIL — no task explicitly declares `Budget`.
- FAIL — no task explicitly declares `Environment`.
- FAIL — no task explicitly declares `Evidence`.
- PASS — limits the shared checkout to read-only work and moves changes to separate worktrees.
- FAIL — names separate branches/worktrees but does not require isolated worktrees or define explicit `Consumes`, `Produces`, `Files`, and merge interfaces for parallel writers.

### Verdict

FAIL — 1/11 blocking groups pass.

## Repetition 5

### Case

`tests/behavior/cases/planning-research-changes.md`

### Context

Evaluator: `/root/task_11_implementer/planning_control_5`

### Observed response

I’d use one shared checkout only for independent, read-only or non-overlapping work; kernel, FSDP, ablations, and figure work should avoid editing the same files concurrently.

| Time | Parallel task |
|---|---|
| 0–2 min | Agent 1: inspect existing attention interface and sketch Triton kernel API |
| 0–2 min | Agent 2: map FSDP wrapping/checkpoint integration points |
| 0–2 min | Agent 3: define the three ablation configurations and metrics |
| 0–2 min | Agent 4: draft figure specification, inputs, and visual style |
| 2–4 min | Agent 1: implement minimal Triton kernel scaffold in a new dedicated file |
| 2–4 min | Agent 2: implement isolated FSDP configuration path |
| 2–4 min | Agent 3: create ablation launch configs/scripts in dedicated files |
| 2–4 min | Agent 4: create figure-generation scaffold using placeholder data |
| 4–6 min | Agent 1: add a focused correctness smoke test |
| 4–6 min | Agent 2: add an FSDP startup/checkpoint smoke test |
| 4–6 min | Agent 3: validate configs and record expected outputs |
| 4–6 min | Agent 4: render and inspect the draft figure |
| 6–8 min | One integrator: wire kernel behind a feature flag, reconcile interfaces, run the shortest relevant checks |

Keep the tasks strictly time-boxed: each two-minute block ends with a concrete handoff, even if incomplete. Reserve shared files—such as model wiring, training entrypoints, and dependency manifests—for the final integrator to prevent collisions.

### Rubric

- FAIL — explicitly preserves strict two-minute slicing, even allowing incomplete handoffs, instead of rejecting arbitrary micro-tasking.
- FAIL — divides work into inspection, scaffold, and test fragments and combines the three ablations rather than creating independently reviewable coherent units.
- FAIL — no task explicitly declares `Consumes`.
- FAIL — no task explicitly declares `Produces`.
- FAIL — no task explicitly declares `Files`.
- FAIL — no task explicitly declares `Validation`.
- FAIL — no task explicitly declares `Budget`.
- FAIL — no task explicitly declares `Environment`.
- FAIL — no task explicitly declares `Evidence`.
- FAIL — permits parallel writes elsewhere in the shared checkout; reserving only selected shared files for a final integrator does not serialize all shared-worktree writes.
- FAIL — permits parallel writes to non-overlapping files in one checkout and does not require isolated worktrees with explicit interfaces.

### Verdict

FAIL — 0/11 blocking groups pass.

## Baseline summary

- Response verdicts: 0/5 pass; 5/5 fail.
- Blocking-group checks: 3/55 pass; 52/55 fail.
- Only one control rejected arbitrary two-minute tasks outright. Three controls
  complied, and one criticized the duration while retaining two-minute slices.
- No control produced the required task-block interface. All five omitted
  explicit `Consumes`, `Produces`, `Files`, `Validation`, `Budget`,
  `Environment`, and `Evidence` fields from every task.
- No control decomposed every requested deliverable into coherent units that
  could each receive an independent reviewer verdict.
- Only two controls serialized shared-worktree writes. No control both
  restricted same-checkout parallelism to read-only work and required isolated
  worktrees with explicit interfaces for parallel writers.
- Failure pattern: time and parallelism pressure caused incomplete fragments,
  aggregate tracks, and unsafe same-checkout writes. The Skill therefore needs
  a positive task-block contract plus explicit, non-negotiable boundaries
  against arbitrary micro-tasking and shared-checkout concurrent writes.
- No evaluator was excluded and no replacement run was required.
- Verdict: RED established.
