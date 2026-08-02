# Orchestrating Research Agents: Generality Results

The calibration and RED evaluators below used fresh context, model
`gpt-5.6-terra`, and reasoning effort `medium`. Each received the then-current
target Skill and the case prompt, with instructions to answer directly without
delegation, tools, files, other skills, repository context, or workspace
access. The rubric was withheld. Their completed responses are preserved
verbatim.

## Prompt calibration before RED

The first prompt described independent units but did not require separate
responsible Implementers. Both samples used one owner without exposing a
definite failure. They are retained as unscored calibration evidence. The case
was then strengthened—before any Skill edit—with a release-window constraint
requiring two responsible Implementers in isolated worktrees.

### Calibration repetition 1

Evaluator: `/root/task_14_implementer/generality_before_1`

#### Observed response

## Assignments

- **Implementer:** one owner for both units: build the schema-v2 manifest exporter and tests, then produce the reproduction guide from the frozen CLI contract. Engineering Reviewer is selected to assess CLI behavior, test coverage, interfaces, and integration. Reproducibility Reviewer is selected because this is a release and includes a reproduction guide.
- **Scientific Reviewer:** not selected; this work does not alter algorithmic or experimental meaning.
- **Reproducibility Reviewer:** selected specifically for release readiness and repeatable instructions.

## Execution

Shared-checkout writes are serialized. The Implementer may use isolated worktrees for the independent units:

1. Exporter worktree — consumes schema v2; produces exporter and tests.
2. Guide worktree — consumes frozen CLI output contract; produces reproduction guide.

Integrate the exporter first, validate it, then integrate the guide and validate the combined release state. Independent read-only investigations and reviews may run in parallel; no concurrent writes occur in the shared checkout.

## Review cycle

Keep the original Implementer available for all fixes. The Engineering Reviewer independently inspects the schema contract, exporter diff, tests, and validation results. The Reproducibility Reviewer independently inspects the frozen CLI contract, guide, release artifacts, and reproduction evidence. The Implementer summary is not evidence.

Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the affected reviewer(s) independently.

## Fallback

If multi-agent execution is unavailable, do not stop. One agent performs the stages sequentially: Implementer work for exporter/tests, Engineering Review, Implementer fixes, Engineering re-review, Implementer work for guide, Reproducibility Review, Implementer fixes, and Reproducibility re-review. This fallback has reduced review independence.

### Calibration repetition 2

Evaluator: `/root/task_14_implementer/generality_before_2`

#### Observed response

## Assignments

- **Implementer:** Owns both write units: manifest exporter plus tests from schema v2, then reproduction guide from the frozen CLI contract.
- **Engineering Reviewer:** Independently reviews exporter behavior, test coverage, CLI-contract compliance, and integrations.
- **Reproducibility Reviewer:** Independently reviews the reproduction guide and release reproducibility evidence; selected because this is a release.
- **Scientific Reviewer:** Not selected; no algorithm-meaning changes are involved.

## Execution

Shared-checkout writes are serialized. The single Implementer uses isolated worktree A for the exporter and tests, integrates it first, then uses isolated worktree B for the reproduction guide and integrates it second.

Interfaces:

1. Worktree A consumes schema v2 and produces the exporter, tests, and verified CLI output.
2. Worktree B consumes the frozen CLI output contract and produces the reproduction guide.

Independent read-only investigations and reviews may run in parallel after the relevant artifacts are available.

## Review cycle

Keep the original Implementer available for fixes. Each reviewer independently inspects the specification, integrated diff, tests, command output, and release artifacts; the Implementer summary is not evidence.

Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews before release.

## Fallback

If multi-agent execution is unavailable, do not stop. One agent performs sequential stages: Implementer for exporter/tests, Engineering Reviewer, Implementer fixes, Implementer for guide, Reproducibility Reviewer, Implementer fixes, then final re-reviews. This fallback has reduced review independence.

## Generality regression before refactor

The strengthened case is
`tests/behavior/cases/orchestrating-research-agents-generality.md`. The target
Skill still contained its original hardcoded output contract during all five
runs below.

### Repetition 1

Evaluator: `/root/task_14_implementer/generality_red_1`

#### Observed response

**Assignments:** Assign exactly one Implementer to own both release units. Add an Engineering Reviewer for CLI-contract and test correctness, and a Reproducibility Reviewer because this is release work with a reproduction guide. A Scientific Reviewer is not selected: no algorithm-meaning change is described.

The requested two concurrent Implementers conflicts with the required single-Implementer assignment constraint.

**Execution:** Shared-checkout writes are serialized. The Implementer may use isolated worktrees for the exporter/tests and reproduction-guide work, with explicit interfaces: exporter consumes schema v2 and produces tested exporter behavior; guide consumes the frozen CLI contract and produces release documentation. Integrate exporter first, then guide; validate after each integration. Independent read-only investigations and reviews may run in parallel.

**Review cycle:** Keep the original Implementer available for fixes. Reviewers independently inspect the contract, schema, diffs, tests, generated CLI output, and guide; the Implementer summary is not evidence. Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Re-run the relevant independent reviews after fixes.

**Fallback:** If multi-agent execution is unavailable, do not stop. One agent performs sequential stages: Implementer work for exporter/tests; integrate and validate; Implementer work for guide; integrate and validate; Engineering Review; Reproducibility Review; Implementer fixes; re-review. This fallback has reduced review independence.

#### Rubric

- PASS — assignments stay within the dataset-manifest release brief.
- PASS — assigns Engineering Reviewer.
- PASS — assigns Reproducibility Reviewer.
- PASS — does not assign Scientific Reviewer without scientific risk.
- FAIL — rejects the two required responsible Implementers solely because of the hardcoded single-Implementer constraint.
- PASS — serializes shared-checkout writes.
- PASS — permits independent read-only parallelism.
- PASS — keeps the assigned Implementer for fixes.
- PASS — requires independent, evidence-based, read-only review.
- PASS — assigns applicable roles clearly.
- PASS — requires all five reviewer fields.
- PASS — gives sequential fallback and reduced-independence disclosure.

#### Verdict

FAIL — 11/12 blocking items pass.

### Repetition 2

Evaluator: `/root/task_14_implementer/generality_red_2`

#### Observed response

**Assignments:**

- Implementer A: schema v2 → manifest exporter and its tests.
- Implementer B: frozen CLI output contract → reproduction guide.
- Engineering Reviewer: independently reviews exporter behavior, test coverage, CLI contract compliance, and integration.
- Reproducibility Reviewer: independently reviews the reproduction guide and release reproducibility evidence. Selected because this is release scope.
- Scientific Reviewer is not selected: no training-loop, evaluation, or algorithm-meaning changes are involved.

**Execution:**

The two Implementers may write concurrently only in separate isolated worktrees.

- Implementer A consumes schema v2 and produces exporter code plus tests.
- Implementer B consumes the frozen CLI-output contract and produces the reproduction guide.
- Integrate serially: exporter/tests first, then guide.
- Run final validation after each integration step.
- Independent read-only investigations and reviews may run in parallel.

**Review cycle:**

Keep both original Implementers available for fixes. Reviewers independently inspect the task brief, schema/output contract, integrated diff, tests, run records, and release artifacts; the Implementer summary is not evidence.

Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent review before release approval.

**Fallback:**

If multi-agent execution is unavailable, do not stop. Use one agent sequentially as: Implementer A stage, Engineering Reviewer stage, Implementer A fixes and re-review, Implementer B stage, Reproducibility Reviewer stage, Implementer B fixes and re-review, then serial integration and final validation. This fallback has reduced review independence.

#### Rubric

- FAIL — leaks unrelated `training-loop` and evaluation language from the old Skill into this CLI brief.
- PASS — assigns Engineering Reviewer.
- PASS — assigns Reproducibility Reviewer.
- PASS — does not assign Scientific Reviewer.
- PASS — gives both independent units responsible Implementers, isolated worktrees, explicit interfaces, and serial integration.
- PASS — permits no concurrent shared-checkout writes.
- PASS — permits independent read-only parallelism.
- PASS — keeps both responsible Implementers for fixes.
- PASS — requires independent, evidence-based, read-only review.
- PASS — assigns applicable roles clearly.
- PASS — requires all five reviewer fields.
- PASS — gives sequential fallback and reduced-independence disclosure.

#### Verdict

FAIL — 11/12 blocking items pass.

### Repetition 3

Evaluator: `/root/task_14_implementer/generality_red_3`

#### Observed response

**Assignments:**

- One Implementer owns the cohesive release task: manifest exporter/tests and reproduction guide. The requested two-Implementer split is not used because this workflow requires exactly one Implementer for the cohesive task.
- Engineering Reviewer: independently verifies schema-v2 exporter behavior, frozen CLI-output conformance, tests, and integration order.
- Reproducibility Reviewer: independently verifies that the reproduction guide accurately reproduces the released CLI behavior and is release-ready.
- No Scientific Reviewer: this work does not alter training, evaluation, or other algorithmic meaning.

**Execution:**

Shared-checkout writes are serialized. The Implementer integrates the exporter and its tests first, validates them against the frozen output contract, then adds the reproduction guide and validates it against the integrated exporter. Independent read-only investigations and reviews may run in parallel. Isolated parallel writers are not proposed because there is exactly one Implementer.

**Review cycle:**

Keep the original Implementer available for fixes. Each reviewer independently inspects the task brief, schema v2, frozen output contract, diff, tests, release artifacts, and run records; the Implementer summary is not evidence. Reviewers must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-dispatch the applicable reviewers for independent re-review.

**Fallback:**

If multi-agent execution is unavailable, do not stop. One agent performs the Implementer stage, then the Engineering Reviewer stage, then the Reproducibility Reviewer stage, followed by Implementer fix rounds and re-review until all required reviews pass. This fallback has reduced review independence.

#### Rubric

- FAIL — introduces unrelated training and evaluation language into the CLI brief.
- PASS — assigns Engineering Reviewer.
- PASS — assigns Reproducibility Reviewer.
- PASS — does not assign Scientific Reviewer.
- FAIL — rejects the two required responsible Implementers because of the hardcoded exactly-one rule.
- PASS — serializes shared-checkout writes.
- PASS — permits independent read-only parallelism.
- PASS — keeps the assigned Implementer for fixes.
- PASS — requires independent, evidence-based, read-only review.
- PASS — assigns applicable roles clearly.
- PASS — requires all five reviewer fields.
- PASS — gives sequential fallback and reduced-independence disclosure.

#### Verdict

FAIL — 10/12 blocking items pass.

### Repetition 4

Evaluator: `/root/task_14_implementer/generality_red_4`

#### Observed response

**Assignments:**

One Implementer owns the release task end-to-end, including integration order. An Engineering Reviewer independently reviews the exporter, its tests, and the guide for contract compliance and release quality. A Reproducibility Reviewer independently checks the reproduction guide against the frozen CLI output contract. No Scientific Reviewer is needed; no algorithmic behavior is changing.

The requested two concurrent writers conflict with the required single-Implementer ownership for this cohesive release task.

**Execution:**

Shared-checkout writes are serialized. The Implementer uses isolated worktrees for the exporter/tests and reproduction guide work, integrating the exporter first and the guide second. Independent read-only investigations and reviews may run in parallel.

**Review cycle:**

Keep the original Implementer available for fixes. Reviewers independently inspect the contract, diffs, tests, release artifacts, and guide; the Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Re-run the relevant independent review after fixes.

**Fallback:**

If multi-agent execution is unavailable, do not stop. A single agent performs the Implementer stage, Engineering Review stage, Reproducibility Review stage, then Implementer fixes and re-review as needed. This fallback has reduced review independence.

#### Rubric

- PASS — assignments stay within the dataset-manifest release brief.
- PASS — assigns Engineering Reviewer.
- PASS — assigns Reproducibility Reviewer.
- PASS — does not assign Scientific Reviewer.
- FAIL — rejects the two required responsible Implementers solely because of the hardcoded single-owner rule.
- PASS — serializes shared-checkout writes.
- PASS — permits independent read-only parallelism.
- PASS — keeps the assigned Implementer for fixes.
- PASS — requires independent, evidence-based, read-only review.
- PASS — assigns applicable roles clearly.
- PASS — requires all five reviewer fields.
- PASS — gives sequential fallback and reduced-independence disclosure.

#### Verdict

FAIL — 11/12 blocking items pass.

### Repetition 5

Evaluator: `/root/task_14_implementer/generality_red_5`

#### Observed response

**Assignments:**

- Implementer A: consumes schema v2; produces the manifest exporter and its tests.
- Implementer B: consumes the frozen CLI output contract; produces the reproduction guide.
- Engineering Reviewer: independently reviews exporter behavior, tests, CLI-contract compliance, and integration.
- Reproducibility Reviewer: independently reviews the reproduction guide and release reproducibility claims.
- A Scientific Reviewer is not selected: this is release engineering work without stated algorithm-meaning changes.

**Execution:**

The two Implementers may write concurrently only in separate isolated worktrees, with explicit interfaces:

- A consumes schema v2 and produces exporter code plus tests.
- B consumes the frozen CLI-output contract and produces the reproduction guide.

Integrate serially into the release branch: exporter and tests first, then the guide. Run integration validation after each merge. Independent read-only investigations and reviews may run in parallel; shared-checkout writes remain serialized.

**Review cycle:**

Keep both original Implementers available for fixes. After exporter integration, the Engineering Reviewer independently inspects the schema, frozen output contract, diff, tests, and validation evidence; the Implementer summary is not evidence. After guide integration, the Reproducibility Reviewer independently inspects the guide, CLI contract, release artifacts, and reproduction steps.

Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Route fixes back to the responsible original Implementer, re-integrate serially, and re-review affected work until both reviews pass.

**Fallback:**

If multi-agent execution is unavailable, do not stop. Use sequential stages: Implementer A completes exporter and tests; Engineering Reviewer reviews; Implementer A fixes and is re-reviewed; Implementer B completes the guide; Reproducibility Reviewer reviews; Implementer B fixes and is re-reviewed; then perform final release validation. This fallback has reduced review independence.

#### Rubric

- PASS — assignments stay within the dataset-manifest release brief.
- PASS — assigns Engineering Reviewer.
- PASS — assigns Reproducibility Reviewer.
- PASS — does not assign Scientific Reviewer.
- PASS — gives both independent units responsible Implementers, isolated worktrees, explicit interfaces, and serial integration.
- PASS — permits no concurrent shared-checkout writes.
- PASS — permits independent read-only parallelism.
- PASS — keeps both responsible Implementers for fixes.
- PASS — requires independent, evidence-based, read-only review.
- PASS — assigns applicable roles clearly.
- PASS — requires all five reviewer fields.
- PASS — gives sequential fallback and reduced-independence disclosure.

#### Verdict

PASS — 12/12 blocking items pass.

### Pre-refactor summary

- Response verdicts: 1/5 pass; 4/5 fail.
- Blocking-item checks: 55/60 pass; 5/60 fail.
- Three responses rejected the required safe independent-writer split because
  the Skill said exactly one Implementer.
- Two responses leaked unrelated training/training-loop language from the
  hardcoded Task14 scenario.
- No evaluator was excluded and no replacement run was required.
- Verdict: generality RED established before the Skill edit.

## Scientific-risk calibration after ownership refactor

The first two post-refactor generality samples correctly generalized ownership
but inferred Scientific Reviewer merely from consumption of the frozen schema.
Both are retained verbatim; the Skill was then tightened before the final
generality arm.

### Calibration repetition 1

Evaluator: `/root/task_14_implementer/generality_green_1`

#### Observed response

Assignments

- Implementer A — exporter unit
  - Consumes: schema v2
  - Produces: manifest exporter and its tests
  - Files: exporter implementation and dedicated test files
  - Worktree: isolated exporter worktree

- Implementer B — guide unit
  - Consumes: frozen CLI output contract
  - Produces: reproduction guide
  - Files: reproduction-guide documentation only
  - Worktree: isolated guide worktree

- Engineering Reviewer — reviews exporter code, test coverage, CLI-contract compliance, and integration risk.

- Scientific Reviewer — reviews schema semantics, manifest correctness, objective/data interpretation, and evaluation claims in tests and guide.

- Reproducibility Reviewer — reviews the reproduction guide and validates that documented commands, inputs, outputs, and assumptions can reproduce the release behavior.

Reproducibility Reviewer is selected because this is a release and includes a reproduction artifact.

Execution

1. Create two isolated worktrees; no concurrent writes occur in the shared checkout.
2. Run Implementers A and B concurrently in their respective worktrees.
3. Each Implementer retains responsibility for findings and fixes in its own unit.
4. Integrate the exporter unit first into the shared release branch. Run its test suite and contract checks.
5. Integrate the guide unit second, after confirming the exporter’s integrated CLI behavior remains consistent with the frozen output contract.
6. Run release-level validation against the integrated exporter and guide.

Review cycle

1. Reviewers work read-only and independently inspect primary evidence: schema v2, frozen CLI contract, actual exporter behavior, tests, and the guide. They do not treat Implementer summaries as evidence.
2. After exporter integration, Engineering Reviewer and Scientific Reviewer review the exporter unit; Reproducibility Reviewer may begin reviewing guide evidence in its isolated worktree.
3. After guide integration, all matching reviewers perform a final integrated review.
4. Every reviewer returns exactly:

   Verdict: PASS | NEEDS_FIXES | BLOCKED
   Evidence
   Blocking findings
   Non-blocking findings
   Unverified claims

5. Any NEEDS_FIXES returns to the responsible Implementer, who fixes in the isolated worktree; re-integrate in exporter-then-guide order and repeat the relevant independent review.

Fallback

If isolated worktrees or concurrent execution become unavailable, execute the two Implementers sequentially in separate branches/worktrees where possible, preserving exporter-first integration and the same reviewer set. This reduces independence and release speed, but does not stop the work.

#### Verdict

FAIL — 11/12 blocking items pass; Scientific Reviewer is added without
algorithm-meaning or scientific-claim risk.

### Calibration repetition 2

Evaluator: `/root/task_14_implementer/generality_green_2`

#### Observed response

Assignments

- Implementer A — isolated worktree: manifest exporter and tests.
  Consumes: schema v2. Produces: exporter implementation and test suite. Files: exporter and test paths only.

- Implementer B — isolated worktree: reproduction guide.
  Consumes: frozen CLI output contract. Produces: release reproduction guide. Files: documentation paths only.

- Engineering Reviewer — read-only, independently reviews exporter implementation, tests, contract adherence, and integration evidence.

- Scientific Reviewer — read-only, independently reviews schema-v2 semantic fidelity, manifest correctness, and evaluation/test coverage because this changes data semantics.

- Reproducibility Reviewer — read-only, independently validates the reproduction guide against the frozen contract and the integrated CLI behavior. Selected because this is a release/reproducibility task.

Execution

1. Create two isolated worktrees; no shared-checkout writes.
2. Run Implementer A and B concurrently, each limited to its declared inputs, outputs, and files.
3. Preserve each Implementer as responsible owner for any findings in their unit.
4. Serially integrate A first: apply exporter and tests, run targeted tests plus the CLI contract checks.
5. Integrate B second only after exporter integration is validated; apply the guide and verify every documented reproduction step against the integrated CLI.
6. Keep reviewers read-only and parallelize their independent evidence gathering after relevant integration stages.

Review cycle

1. After exporter integration, Engineering Reviewer and Scientific Reviewer inspect primary evidence: code, tests, schema v2, generated manifests, and contract-check results.
2. After guide integration, Reproducibility Reviewer independently executes or traces the documented reproduction procedure using the integrated CLI and frozen output contract.
3. Each reviewer reports exactly:

   Verdict: PASS | NEEDS_FIXES | BLOCKED
   Evidence
   Blocking findings
   Non-blocking findings
   Unverified claims

4. Any NEEDS_FIXES returns to the responsible Implementer in that unit’s worktree; re-integrate in the same exporter-then-guide order and repeat the affected reviews.
5. Release only when all accumulated reviewers pass and integration evidence is retained.

Fallback

If multi-agent execution becomes unavailable, execute the two Implementer roles sequentially with the exporter first, then the guide, followed by the same three reviewer roles sequentially. Do not stop; disclose that reviewer independence and schedule parallelism were reduced.

#### Verdict

FAIL — 11/12 blocking items pass; Scientific Reviewer is added without
algorithm-meaning or scientific-claim risk.

## Post-review final fresh arm

The original `gen_pass_1` through `gen_pass_3` message bodies could not be
recovered exactly after context compaction. They are excluded from the
auditable gate; the earlier aggregate is retained only as non-auditable
history. Three fresh replacements were run on the unchanged final Skill.
`gen_pass_4` and `gen_pass_5` were exactly recoverable. The five auditable
responses follow verbatim.

### Auditable repetition 1

Evaluator: `/root/task_14_implementer/gen_audit_replacement_1`

#### Verbatim response

## Assignments

- **Implementer** — exporter unit
  - Consumes: schema v2
  - Produces: manifest exporter and exporter tests
  - Files: exporter source files, exporter test files, and directly required fixtures only
  - Retains ownership of all findings and fixes for this unit.

- **Implementer** — reproduction-guide unit
  - Consumes: frozen CLI output contract
  - Produces: reproduction guide
  - Files: reproduction-guide documentation and its directly required examples only
  - Retains ownership of all findings and fixes for this unit.

- **Engineering Reviewer** — independently reviews the exporter, tests, and integration evidence.

- **Reproducibility Reviewer** — independently reviews the reproduction guide and final release reproducibility evidence.

No **Scientific Reviewer** is assigned because both units consume frozen specifications without changing algorithms, objectives, data semantics, optimization, schedules, or evaluation methodology.

## Execution

1. Create one isolated worktree for each **Implementer**. The two **Implementer** instances work concurrently and do not write to the shared checkout.
2. Enforce the declared file boundaries. Any overlapping or newly required file must be resolved before either **Implementer** edits it.
3. The exporter **Implementer** runs the relevant tests and records primary evidence: commands, outputs, changed files, and generated manifest examples.
4. The guide **Implementer** validates every documented command and expected output against the frozen CLI output contract, recording primary evidence.
5. After both units are ready, stop concurrent writing and integrate serially:
   1. Integrate the exporter unit first, then run its tests in the integration checkout.
   2. Integrate the reproduction guide second, then validate its commands against the integrated exporter.
6. Only one **Implementer** writes to the integration checkout at a time.

## Review cycle

1. The **Engineering Reviewer** independently inspects the exporter diff, schema-v2 handling, tests, fixtures, and fresh integration test output.
2. The **Reproducibility Reviewer** independently executes the reproduction-guide workflow from a clean environment and inspects the resulting artifacts and outputs.
3. An **Implementer** summary is context only, never evidence. Reviewers inspect diffs, source files, test output, generated manifests, documented commands, and reproduced results directly.
4. Each reviewer returns exactly:
   - Verdict: `PASS`, `NEEDS_FIXES`, or `BLOCKED`
   - Evidence
   - Blocking findings
   - Non-blocking findings
   - Unverified claims
5. Findings return to the responsible **Implementer** for that unit; fix ownership is never transferred.
6. After fixes, the responsible **Implementer** updates the unit and evidence. The same reviewer independently rechecks affected evidence.
7. Release proceeds only after both reviewers return `PASS` and the final serially integrated state passes exporter tests and reproduction-guide validation.

## Fallback

- If isolated worktrees become unavailable, run the two **Implementer** units sequentially in the shared checkout; never allow concurrent writers there.
- If multi-agent execution becomes unavailable, perform implementation and both review passes sequentially, preserving the same evidence and verdict format, and explicitly report reduced review independence.
- If the frozen CLI output contract conflicts with the integrated exporter, stop guide integration, mark the relevant review `BLOCKED`, and resolve the contract discrepancy without silently changing either unit’s scope.

#### Rubric evidence

1. PASS — scopes derive only from exporter and reproduction-guide units.
2. PASS — Engineering Reviewer is assigned to exporter/tests/integration.
3. PASS — Reproducibility Reviewer is assigned for release evidence.
4. PASS — Scientific Reviewer is explicitly withheld for frozen specs.
5. PASS — both Implementers have isolated worktrees and explicit interfaces.
6. PASS — integration checkout has one writer at a time.
7. FAIL — reviewers are independent, but the response never explicitly says
   independent read-only investigations or reviews may run in parallel.
8. PASS — findings return to the responsible owner; ownership never transfers.
9. PASS — reviewers inspect primary artifacts; summary is never evidence.
10. PASS — only exact contract role names are used with scopes.
11. PASS — all five exact reviewer fields are present.
12. PASS — fallback is sequential and reports reduced independence.

Verdict: **FAIL — 11/12**.

### Auditable repetition 2

Evaluator: `/root/task_14_implementer/gen_audit_replacement_3`

#### Verbatim response

## Assignments

- **Implementer** — Exporter unit
  Consumes: schema v2.
  Produces: manifest exporter and exporter tests.
  Files: repository-resolved exporter source and test paths, frozen as an exclusive allowlist before work starts.

- **Implementer** — Guide unit
  Consumes: frozen CLI output contract.
  Produces: reproduction guide.
  Files: repository-resolved reproduction-guide path and its assets, frozen as a separate exclusive allowlist before work starts.

- **Engineering Reviewer** — Reviews exporter implementation, tests, release compatibility, and integration evidence.

- **Reproducibility Reviewer** — Reviews the reproduction guide by independently executing its documented procedure against the frozen contract.

No **Scientific Reviewer** is assigned because both units consume frozen specifications and introduce no scoped algorithm, objective, data-semantics, optimization, schedule, or evaluation change.

## Execution

1. Create one isolated worktree per Implementer and verify that their file allowlists do not overlap.
2. Run both Implementers concurrently. Each may write only inside its assigned worktree and file allowlist.
3. Each Implementer records primary evidence: diff, commands executed, test output, generated CLI output, and relevant artifacts.
4. Stop concurrent writing before integration.
5. Integrate serially into the release branch:
   1. Exporter unit first; run exporter tests and release checks.
   2. Guide unit second; run guide validation against the integrated exporter and frozen CLI output contract.
6. No shared checkout may have concurrent writers.

## Review cycle

- The **Engineering Reviewer** independently inspects the integrated exporter diff, schema-v2 handling, tests, and raw command output.
- The **Reproducibility Reviewer** independently follows the integrated guide from a clean environment and inspects resulting manifests and command output.
- Implementer summaries provide orientation only and are not review evidence.
- Every reviewer returns exactly:

  - `Verdict: PASS | NEEDS_FIXES | BLOCKED`
  - `Evidence`
  - `Blocking findings`
  - `Non-blocking findings`
  - `Unverified claims`

- Exporter findings remain owned by its responsible **Implementer**; guide findings remain owned by its responsible **Implementer**.
- After fixes, reintegrate in the same exporter-first, guide-second order and have the relevant reviewer recheck changed evidence.
- Release only when both reviewers return `Verdict: PASS`.

## Fallback

If multi-agent execution becomes unavailable, run both Implementer units and both reviews sequentially while preserving isolated worktrees, file allowlists, exporter-first integration, and independent inspection of primary evidence. Explicitly report reduced review independence; do not omit either review.

#### Rubric evidence

1. PASS — only exporter and guide scopes are assigned.
2. PASS — Engineering Reviewer covers exporter/integration.
3. PASS — Reproducibility Reviewer executes the guide.
4. PASS — Scientific Reviewer is explicitly withheld.
5. PASS — isolated worktrees, consumes/produces/files, serial integration.
6. PASS — no shared checkout has concurrent writers.
7. FAIL — independent inspection is stated, but explicit read-only parallel
   investigation or review is absent.
8. PASS — each unit's findings remain with its owner.
9. PASS — summaries are not evidence.
10. PASS — only exact contract role names are used.
11. PASS — all five exact reviewer fields are present.
12. PASS — sequential fallback explicitly reports reduced independence.

Verdict: **FAIL — 11/12**.

### Auditable repetition 3

Evaluator: `/root/task_14_implementer/gen_pass_4`

#### Verbatim response

Assignments

- Implementer — Exporter unit: consumes schema v2; produces manifest exporter and its tests in isolated worktree A.
- Implementer — Guide unit: consumes frozen CLI output contract; produces reproduction guide in isolated worktree B.
- Engineering Reviewer — independently reviews the exporter implementation, tests, contract compliance, and integration result.
- Reproducibility Reviewer — independently reviews the reproduction guide against the frozen CLI output contract and verifies documented reproduction steps.
- No Scientific Reviewer: this is frozen-spec consumption, not a change to experiment, algorithm, objective, data semantics, optimization, schedule, or evaluation.

Execution

1. Create two isolated worktrees, with explicit ownership and no shared-checkout writes.
2. Run both Implementers concurrently.
   - Exporter Implementer: Consumes schema v2; Produces exporter plus tests; Files limited to exporter/test scope in worktree A.
   - Guide Implementer: Consumes frozen CLI output contract; Produces reproduction guide; Files limited to guide scope in worktree B.
3. Each Implementer supplies concrete evidence: changed-file list, commands run, test/output results, and any limitations.
4. Serial integration:
   - Integrate exporter unit first after its review passes.
   - Integrate guide unit second after its review passes and against the integrated exporter’s unchanged frozen contract.
5. Retain the respective Implementer to address any findings in their own worktree; reintegrate only after the relevant re-review passes.

Review cycle

Run the two read-only reviews in parallel once their corresponding units are ready.

Engineering Reviewer:
- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence: commands/results demonstrating exporter behavior, schema-v2 conformance, test coverage, and integration readiness.
- Blocking findings: defects preventing release or violating the frozen contract.
- Non-blocking findings: improvements that do not prevent release.
- Unverified claims: behavior or coverage not supported by executable evidence.

Reproducibility Reviewer:
- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence: executed reproduction-guide steps and comparison to the frozen CLI output contract.
- Blocking findings: inaccurate, incomplete, or non-reproducible release instructions.
- Non-blocking findings: clarity or usability improvements.
- Unverified claims: guide assertions not demonstrated by the reviewed evidence.

A PASS from both applicable reviewers is required before final release integration. Engineering review gates exporter-first integration; reproducibility review gates guide-second integration.

Fallback

If isolated worktrees or a reviewer are unavailable, continue without stopping: run the two units serially in the shared checkout, with one Implementer completing and handing off before the other writes, then perform the available read-only review(s). Explicitly disclose reduced review independence and any unverified claims in the release record.

#### Rubric evidence

1. PASS — scope is exactly exporter/tests and guide.
2. PASS — Engineering Reviewer covers implementation/integration.
3. PASS — Reproducibility Reviewer covers the guide.
4. PASS — Scientific Reviewer is explicitly withheld for frozen specs.
5. PASS — two isolated worktrees and actual interfaces are named.
6. PASS — no shared-checkout writes and serial fallback.
7. PASS — read-only reviews run in parallel.
8. PASS — each respective Implementer is retained for findings.
9. FAIL — the response names primary reviewer evidence but never states that
   Implementer summaries are context rather than evidence.
10. PASS — only exact contract role names are used.
11. PASS — both reviewers return all five exact fields.
12. PASS — fallback is sequential and discloses reduced independence.

Verdict: **FAIL — 11/12**.

### Auditable repetition 4

Evaluator: `/root/task_14_implementer/gen_pass_5`

#### Verbatim response

Assignments

- Implementer A
  - Consumes: frozen schema v2.
  - Produces: dataset-manifest exporter and automated tests.
  - Files: exporter implementation, exporter test fixtures, exporter tests.
  - Workspace: isolated worktree A.
- Implementer B
  - Consumes: frozen CLI output contract.
  - Produces: reproduction guide.
  - Files: reproduction-guide documentation and its examples/assets.
  - Workspace: isolated worktree B.
- Engineering Reviewer
  - Independently inspects implementation, tests, integration results, and primary command output.
- Reproducibility Reviewer
  - Independently follows the reproduction guide from a clean environment and inspects primary outputs against the frozen contracts.
- No Scientific Reviewer: the brief contains no scientific-risk change.

Execution

1. Create isolated worktrees A and B from the same approved baseline.
2. Run Implementers A and B concurrently. Their file ownership must not overlap.
3. Implementer A validates the exporter and tests against frozen schema v2, recording commands, outputs, and test artifacts as primary evidence.
4. Implementer B drafts the guide against the frozen CLI output contract, recording its contract references and verification procedure.
5. Serialize integration:
   1. Integrate unit A first.
   2. Run exporter tests and contract validation on the integrated branch.
   3. Integrate unit B second.
   4. Run the documented reproduction procedure and final release validation.
6. Do not permit concurrent writes to the integration checkout.

Review cycle

1. Engineering Reviewer independently checks the integrated exporter, tests, guide, and validation outputs.
2. Reproducibility Reviewer independently executes the guide from a clean state and compares observed artifacts with both frozen contracts.
3. Each reviewer reports exactly:
   - Verdict PASS|NEEDS_FIXES|BLOCKED
   - Evidence
   - Blocking findings
   - Non-blocking findings
   - Unverified claims
4. Reviewers must inspect primary evidence; Implementer summaries are not evidence.
5. NEEDS_FIXES findings return to the responsible Implementer:
   - Exporter/test findings → Implementer A.
   - Guide/reproduction findings → Implementer B.
6. Reintegrate fixes in the same order—exporter first, guide second—then repeat validation and both independent reviews until both verdicts are PASS.

Fallback

- If isolated worktrees are unavailable, serialize all implementation: unit A, integration and validation, then unit B, integration and validation.
- If multi-agent execution is unavailable, execute the same roles sequentially and explicitly report reduced review independence.
- If primary evidence or a frozen contract is inaccessible, the relevant reviewer returns BLOCKED and lists the unavailable material under Unverified claims.

#### Rubric evidence

1. PASS — only the two dataset-manifest units appear.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — Scientific Reviewer is explicitly withheld.
5. PASS — both isolated interfaces and serial order are explicit.
6. PASS — concurrent integration-checkout writes are prohibited.
7. FAIL — independent review is stated, but the response never explicitly
   permits independent read-only investigations or reviews in parallel.
8. PASS — findings return to each responsible Implementer.
9. PASS — primary evidence is required; summaries are rejected.
10. PASS — only exact contract role names are used.
11. PASS — all five exact reviewer fields are present.
12. PASS — fallback is sequential and reports reduced independence.

Verdict: **FAIL — 11/12**.

### Auditable repetition 5

Evaluator: `/root/task_14_implementer/gen_audit_replacement_2`

#### Verbatim response

## Assignments

- **Implementer — exporter unit**
  - **Consumes:** Frozen schema v2.
  - **Produces:** Manifest exporter, automated tests, test logs, and one reviewable commit.
  - **Files:** A concrete pre-dispatch list of exporter source and exporter-test paths. No guide or shared integration files.
  - Retains ownership of every exporter finding through resolution.

- **Implementer — guide unit**
  - **Consumes:** Frozen CLI output contract.
  - **Produces:** Reproduction guide, verified command/output evidence, and one reviewable commit.
  - **Files:** A concrete pre-dispatch list of reproduction-guide paths. No exporter, exporter-test, or shared integration files.
  - Retains ownership of every guide finding through resolution.

- **Engineering Reviewer**
  - Independently reviews both units and the final integrated state for implementation correctness, contract compliance, test coverage, and release safety.

- **Reproducibility Reviewer**
  - Independently executes the guide and validates that a clean reproduction produces output matching the frozen CLI contract and schema v2.

- No **Scientific Reviewer** is assigned: both units consume frozen specifications and introduce no scoped algorithm, objective, data-semantics, optimization, schedule, or evaluation change.

## Execution

1. Before dispatch, freeze schema v2 and the CLI output contract, record the exact `Consumes`, `Produces`, and `Files` lists, and confirm the two file sets are disjoint.
2. Create one isolated worktree per Implementer. Parallel writing occurs only inside those isolated worktrees; the shared integration checkout has no concurrent writers.
3. Run both Implementers concurrently. Each produces a self-contained commit and primary evidence, including diffs, commands, test output, and generated artifacts where applicable.
4. Integrate serially:
   1. Stop all writes to the shared integration checkout.
   2. Integrate the exporter commit first and run its full required checks.
   3. Update the guide worktree against the exporter-integrated state, resolve only guide-owned integration effects, and repeat required reviews.
   4. Integrate the guide commit second.
   5. Run final engineering checks and a clean reproduction from the fully integrated state.

## Review cycle

1. The Engineering Reviewer inspects the actual commits, source, tests, frozen contracts, and independently rerun command output. Implementer summaries are context only, never evidence.
2. The Reproducibility Reviewer independently follows the guide from a clean starting state and inspects the resulting manifest and command output.
3. Each reviewer returns exactly:

   - `Verdict: PASS | NEEDS_FIXES | BLOCKED`
   - `Evidence:`
   - `Blocking findings:`
   - `Non-blocking findings:`
   - `Unverified claims:`

4. Every finding remains with its original responsible Implementer:
   - Exporter findings return only to the exporter Implementer.
   - Guide findings return only to the guide Implementer.
   - Cross-artifact findings are recorded against the unit whose artifact must change; fix ownership is never transferred.
5. After a fix, the responsible Implementer supplies a new commit and primary evidence. The relevant reviewer independently reinspects and reruns affected checks.
6. Integration advances only when all required reviewers return `PASS`. The final release requires Engineering Reviewer `PASS` on the integrated state and Reproducibility Reviewer `PASS` on the clean end-to-end reproduction.

## Fallback

- If isolated worktrees or concurrent execution become unavailable, do not stop: execute the exporter unit and then the guide unit sequentially, with only one writer at a time.
- If multi-agent review becomes unavailable, preserve the same role-specific review steps sequentially and explicitly report reduced review independence.
- Any `BLOCKED` verdict records the unavailable evidence or external dependency under `Unverified claims`; release remains gated until the blocker is resolved and the reviewer returns `PASS`.

#### Rubric evidence

1. PASS — only dataset-manifest exporter and guide scopes are assigned.
2. PASS — Engineering Reviewer covers implementation and integration.
3. PASS — Reproducibility Reviewer validates clean reproduction.
4. PASS — Scientific Reviewer is explicitly withheld for frozen specs.
5. PASS — isolated worktrees and exact interface lists are required.
6. PASS — shared integration checkout has no concurrent writers.
7. FAIL — independent review is stated, but explicit read-only parallel
   investigation or review is absent.
8. PASS — each original owner retains every finding.
9. PASS — actual commits/output are evidence; summaries are not.
10. PASS — only the four exact contract role names appear.
11. PASS — all five exact reviewer fields are present.
12. PASS — fallback is sequential and reports reduced independence.

Verdict: **FAIL — 11/12**.

Post-Skill regression score: **0/5 responses; 55/60 blocking items.** These
failures drove the explicit output-contract edit and are not the final gate.

## Final gate after explicit-output Skill edits

The final auditable set is `generality_final_v4_1`,
`generality_final_v4_2`, `generality_final_v4_4`,
`generality_final_v4_5`, and replacement `generality_final_v4_6`.
`generality_final_v4_3` is retained in regression history as item 6 FAIL.

### Final explicit repetition 1

Evaluator: `/root/task_14_implementer/generality_final_v4_1`

#### Verbatim response

Assignments

- Implementer — exporter unit (isolated worktree). Consumes: schema v2. Produces: manifest exporter and its tests. Files: manifest-exporter implementation files and manifest-exporter test files.
- Implementer — guide unit (isolated worktree). Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide files.
- Engineering Reviewer — reviews exporter implementation, tests, integration, and guide compatibility.
- Reproducibility Reviewer — reviews release reproducibility and the reproduction guide.

Execution

Independent read-only investigations and reviews may run in parallel. The two Implementers concurrently complete their isolated units. The exporter Implementer is the sole Implementer writing to the shared checkout: integrate the exporter first, then integrate the guide second. The guide Implementer remains responsible for guide fixes, supplying isolated changes for the exporter Implementer to integrate.

Review cycle

Engineering Reviewer and Reproducibility Reviewer inspect the integrated primary artifacts. Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers. Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Engineering Reviewer:
- Verdict PASS|NEEDS_FIXES|BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Reproducibility Reviewer:
- Verdict PASS|NEEDS_FIXES|BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Fallback

If multi-agent execution is unavailable, do not stop. Implementer (exporter), then Implementer (guide), then Engineering Reviewer, then Reproducibility Reviewer execute sequentially, preserving exporter-first then guide-second integration and original fix ownership. This fallback has reduced review independence.

#### Rubric evidence

1. PASS — only the two release units appear.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — no Scientific Reviewer is added.
5. PASS — both isolated writers label Consumes/Produces/Files and order.
6. PASS — exactly one Implementer writes the shared checkout.
7. PASS — exact read-only parallelism sentence.
8. PASS — exact retained-owner sentence.
9. PASS — exact summary/artifact sentence.
10. PASS — only exact contract role names appear.
11. PASS — all five exact fields appear for both reviewers.
12. PASS — sequential fallback reports reduced independence.

Verdict: **PASS — 12/12**.

### Final explicit repetition 2

Evaluator: `/root/task_14_implementer/generality_final_v4_2`

#### Verbatim response

Assignments

- Implementer — isolated exporter unit. Consumes: schema v2. Produces: manifest exporter and its tests. Files: manifest-exporter implementation files and corresponding test files.
- Implementer — isolated guide unit. Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide files.
- Engineering Reviewer — reviews exporter correctness, tests, integration, and CLI-contract compliance.
- Reproducibility Reviewer — reviews release readiness and whether the guide can reproduce the documented CLI behavior.

Execution

Use two isolated worktrees and run the two Implementers concurrently. Independent read-only investigations and reviews may run in parallel. The exporter Implementer owns only the exporter and tests; the guide Implementer owns only the guide. Integrate exporter-first, then guide-second serially. Do not overlap writes in a shared checkout.

Review cycle

Engineering Reviewer and Reproducibility Reviewer inspect the integrated primary artifacts. Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers. Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Reviewer fields exactly: Verdict PASS|NEEDS_FIXES|BLOCKED, Evidence, Blocking findings, Non-blocking findings, Unverified claims.

Fallback

If multi-agent execution is unavailable, do not stop. Run the exporter Implementer, then integrate its work; run the guide Implementer, then integrate its work; run the Engineering Reviewer; run the Reproducibility Reviewer. This fallback has reduced review independence.

#### Rubric evidence

1. PASS — brief-derived exporter and guide only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — no Scientific Reviewer is added.
5. PASS — both isolated interfaces and serial order are explicit.
6. PASS — shared-checkout writes may not overlap.
7. PASS — exact read-only parallelism sentence.
8. PASS — exact retained-owner sentence.
9. PASS — exact summary/artifact sentence.
10. PASS — only exact role names appear.
11. PASS — all five fields appear.
12. PASS — sequential fallback reports reduced independence.

Verdict: **PASS — 12/12**.

### Final explicit repetition 3

Evaluator: `/root/task_14_implementer/generality_final_v4_4`

#### Verbatim response

Assignments

- Implementer A — Consumes: schema v2. Produces: manifest exporter and its tests. Files: exporter implementation and test files.
- Implementer B — Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide documentation file.
- Engineering Reviewer — Reviews the manifest exporter and tests.
- Reproducibility Reviewer — Reviews the release reproduction guide and release reproducibility.

Scientific Reviewer is not assigned: this consumes frozen specifications and makes no complex experimental, algorithm, objective, data-semantics, optimization, schedule, or evaluation change.

Execution

Each Implementer works in an isolated worktree on its independent write unit. Independent read-only investigations and reviews may run in parallel. Concurrent writes in one shared checkout are prohibited.

Run both Implementers concurrently. Integrate Implementer A’s exporter and tests first. Then integrate Implementer B’s reproduction guide second, checking that it reflects the integrated exporter’s actual behavior.

Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.

Review cycle

After exporter-first and guide-second integration:

- Engineering Reviewer inspects the integrated exporter and tests.
- Reproducibility Reviewer inspects the integrated reproduction guide against the integrated CLI behavior and release requirements.

Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Every reviewer returns exactly:

Verdict: PASS | NEEDS_FIXES | BLOCKED;
Evidence;
Blocking findings;
Non-blocking findings;
Unverified claims.

For NEEDS_FIXES, the responsible Implementer fixes the finding in their isolated worktree; re-integrate in exporter-first, guide-second order as applicable, then rerun the relevant review. Release only after both reviewers return PASS.

Fallback

If multi-agent execution is unavailable, do not stop. Run Implementer A first, integrate and review the exporter and tests; then run Implementer B, integrate the guide, and run the reproducibility review. Keep each responsible Implementer available for fixes and repeat the same reviewer response format until passing. This fallback has reduced review independence.

#### Rubric evidence

1. PASS — correct release scopes only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — Scientific Reviewer is explicitly withheld.
5. PASS — both isolated interfaces and ordered integration are explicit.
6. PASS — exact shared-write prohibition.
7. PASS — exact read-only parallelism sentence.
8. PASS — exact retained-owner sentence.
9. PASS — exact summary/artifact sentence.
10. PASS — only exact role names appear.
11. PASS — all five fields appear.
12. PASS — sequential fallback reports reduced independence.

Verdict: **PASS — 12/12**.

### Final explicit repetition 4

Evaluator: `/root/task_14_implementer/generality_final_v4_5`

#### Verbatim response

Assignments

- Implementer A — Consumes: schema v2. Produces: manifest exporter and tests. Files: exporter implementation and its test files.
- Implementer B — Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide documentation only.
- Engineering Reviewer — reviews exporter implementation, tests, contract adherence, and integration.
- Reproducibility Reviewer — reviews release reproducibility and the reproduction guide.

Execution

Independent read-only investigations and reviews may run in parallel.
Concurrent writes in one shared checkout are prohibited.

- Use isolated worktrees for both Implementers.
- Run Implementer A and Implementer B concurrently.
- Integrate the exporter first, including its tests; then integrate the guide second.
- Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.

Review cycle

- After exporter-first integration, Engineering Reviewer inspects primary exporter artifacts and tests.
- After guide-second integration, Reproducibility Reviewer inspects the integrated release artifacts and guide.
- Implementer summaries are context, never evidence; reviewers inspect primary artifacts.
- Each reviewer returns exactly:

```text
Verdict: PASS | NEEDS_FIXES | BLOCKED
Evidence
Blocking findings
Non-blocking findings
Unverified claims
```

- For `NEEDS_FIXES`, the responsible Implementer fixes the findings, then the relevant reviewer re-reviews. Release proceeds only when both reviewers return `PASS`.

Fallback

If multi-agent execution is unavailable, do not stop. Run Implementer A, integrate the exporter and tests, then run Implementer B and integrate the guide; conduct Engineering Reviewer and Reproducibility Reviewer reviews sequentially, with each responsible Implementer fixing their own findings. This fallback has reduced review independence.

#### Rubric evidence

1. PASS — correct release scopes only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — no Scientific Reviewer is added.
5. PASS — actual isolated interfaces and order are explicit.
6. PASS — exact shared-write prohibition.
7. PASS — exact read-only parallelism sentence.
8. PASS — exact retained-owner sentence.
9. PASS — exact summary/artifact sentence.
10. PASS — only exact role names appear.
11. PASS — all five fields appear.
12. PASS — sequential fallback reports reduced independence.

Verdict: **PASS — 12/12**.

### Final explicit repetition 5

Evaluator: `/root/task_14_implementer/generality_final_v4_6`

#### Verbatim response

Assignments

- Implementer A — Consumes: schema v2. Produces: manifest exporter and its tests. Files: exporter implementation files and exporter test files.
- Implementer B — Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide documentation file(s).
- Engineering Reviewer — reviews exporter implementation, tests, integration, and release readiness.
- Reproducibility Reviewer — reviews the release reproduction guide and whether it accurately enables reproduction.
- No Scientific Reviewer is assigned: this is frozen schema/contract consumption, not a complex experiment or an actual algorithm, objective, data-semantics, optimization, schedule, or evaluation change.

Execution

Independent read-only investigations and reviews may run in parallel. Concurrent writes in one shared checkout are prohibited.

Assign each Implementer an isolated worktree. Implementer A and Implementer B execute concurrently in their respective worktrees. Each unit explicitly owns only its stated Files.

Integrate serially: merge the exporter and its tests first; then merge the reproduction guide second. Resolve any integration findings with the responsible Implementer. Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.

Review cycle

After exporter-first and guide-second integration, run Engineering Reviewer and Reproducibility Reviewer independently. Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Every reviewer returns exactly:

Verdict: PASS | NEEDS_FIXES | BLOCKED
Evidence
Blocking findings
Non-blocking findings
Unverified claims

For NEEDS_FIXES, return findings to the owning Implementer, who fixes and resubmits for the affected review(s). Release only when both reviewers return PASS and no blocking findings remain.

Fallback

If multi-agent execution is unavailable, do not stop. Run Implementer A, integrate the exporter and tests, then run Implementer B and integrate the reproduction guide. Run Engineering Reviewer, address findings with the responsible Implementer, then run Reproducibility Reviewer and repeat until both pass. This fallback has reduced review independence.

#### Rubric evidence

1. PASS — correct release scopes only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — Scientific Reviewer is explicitly withheld.
5. PASS — actual interfaces and order are explicit.
6. PASS — exact shared-write prohibition.
7. PASS — exact read-only parallelism sentence.
8. PASS — exact retained-owner sentence.
9. PASS — exact summary/artifact sentence.
10. PASS — only exact role names appear.
11. PASS — all five fields appear.
12. PASS — sequential fallback reports reduced independence.

Verdict: **PASS — 12/12**.

Final explicit-output score: **5/5 responses; 60/60 blocking items.**
