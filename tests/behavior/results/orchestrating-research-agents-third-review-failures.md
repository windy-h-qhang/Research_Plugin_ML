# Orchestrating Research Agents: Third-Review Failed Samples

All responses below are verbatim. Harness-invalid samples are excluded because
the supplied condensed Skill omitted a requirement present in `SKILL.md`.
Behavior failures are retained as regression evidence. No sample contributes
to either final gate.

## Harness-invalid: original_explicit_final_2

The harness omitted `only` from the Reproducibility rule.

```text
Assignments

- Implementer: training loop and FSDP wrapper as one cohesive change; sole writer.
- Scientific Reviewer: training-loop risk.
- Engineering Reviewer: FSDP integration and tests.
- Reproducibility Reviewer: training/test reproducibility.

Execution

The Implementer works serially in the shared checkout and retains all fixes. Independent read-only investigations and reviews may run in parallel.

Review cycle

Implementer summaries are context, never evidence; reviewers inspect primary artifacts. Each reviewer returns exactly Verdict PASS|NEEDS_FIXES|BLOCKED, Evidence, Blocking findings, Non-blocking findings, Unverified claims.

Fallback

If multi-agent execution is unavailable, do not stop. Run the Implementer, then Scientific Reviewer, Engineering Reviewer, and Reproducibility Reviewer sequentially; the Implementer applies its own fixes and reviewers re-check primary artifacts. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 PASS; 6 PASS; 7 FAIL
— adds Reproducibility Reviewer without qualifying scope; 8 PASS; 9 PASS;
10 PASS; 11 PASS; 12 PASS. Verdict: **FAIL — 11/12; harness-invalid**.

## Behavior failure: original_explicit_final_6_replacement

```text
Assignments

- Implementer A: training-loop unit. Consumes the current training-loop interfaces; produces training-loop changes and focused tests; files: training-loop implementation and its tests.
- Implementer B: FSDP-wrapper unit. Consumes the current wrapper interfaces; produces FSDP-wrapper changes and focused tests; files: FSDP-wrapper implementation and its tests.
- Implementer A and B retain ownership of fixes in their respective units; there is no separate “fix whatever fails” owner.
- Engineering Reviewer: selected for integration, interface, and test-engineering risk.
- Scientific Reviewer: selected for training objective, optimization, scheduling, and evaluation-semantics risk.
- No Reproducibility Reviewer: this is not release work or an explicit reproducibility request.

Execution

Do not allow concurrent writers in the shared checkout. Implementer A completes and validates the training-loop change first; Implementer B then integrates the FSDP-wrapper change against that result. Each implementer fixes failures within their owned unit, with serial integration between units. Independent read-only investigations and reviews may run in parallel.

Review cycle

After integration, Engineering Reviewer and Scientific Reviewer inspect the primary code, tests, test results, and relevant runtime artifacts. Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Each reviewer returns exactly:

Verdict PASS|NEEDS_FIXES|BLOCKED
Evidence
Blocking findings
Non-blocking findings
Unverified claims

Owners address findings and the same reviewers re-review until both return PASS or a reviewer returns BLOCKED.

Fallback

If multi-agent execution is unavailable, do not stop. Run Implementer A, Implementer B, Engineering Reviewer, and Scientific Reviewer sequentially in the same order, preserving serial ownership and review requirements. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 FAIL — two Implementers are selected for serialized writes
in one shared checkout; 3 PASS; 4 PASS; 5 PASS; 6 PASS; 7 PASS; 8 PASS;
9 PASS; 10 PASS; 11 PASS; 12 PASS. Verdict: **FAIL — 11/12**.

## Behavior failure: original_final_v2_5

```text
Assignments

One Implementer owns all shared-checkout writes; select Scientific Reviewer and Engineering Reviewer.

Execution

Do not let four agents edit the shared checkout in parallel. Independent read-only investigations and reviews may run in parallel.

Review cycle

Implementer summaries are context, never evidence; reviewers inspect primary artifacts. Output: Verdict PASS|NEEDS_FIXES|BLOCKED, Evidence, Blocking findings, Non-blocking findings, Unverified claims.

Fallback

If multi-agent execution is unavailable, do not stop. Run the Implementer, Scientific Reviewer, and Engineering Reviewer sequentially. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 FAIL — retained Implementer ownership for
review findings is absent; 5 PASS; 6 PASS; 7 PASS; 8 PASS; 9 PASS; 10 PASS;
11 PASS; 12 PASS. Verdict: **FAIL — 11/12**.

## Behavior failure: generality_final_v3_1

```text
Assignments

- Implementer: Consume schema v2; produce the manifest exporter and its tests in an isolated worktree.
- Implementer: Consume the frozen CLI output contract; produce the reproduction guide in an isolated worktree.
- Engineering Reviewer: Review exporter implementation, tests, integration, and CLI-contract compliance.
- Reproducibility Reviewer: Review the release reproduction guide and its ability to reproduce the released CLI workflow.

Execution

- Use two isolated worktrees. The two Implementers execute concurrently.
- Implementer consumes schema v2 and produces the exporter plus tests; Implementer consumes the frozen CLI output contract and produces the reproduction guide.
- Independent read-only investigations and reviews may run in parallel.
- Integrate the exporter and tests first, then integrate the reproduction guide second.
- Each Implementer is responsible for its own produced artifacts and remains the sole fix owner for findings in those artifacts.

Review cycle

- Engineering Reviewer and Reproducibility Reviewer inspect the integrated primary artifacts after the ordered integration.
- Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.
- Implementer summaries are context, never evidence; reviewers inspect primary artifacts.
- Reviewer reports use exactly:
  - Verdict: PASS | NEEDS_FIXES | BLOCKED
  - Evidence
  - Blocking findings
  - Non-blocking findings
  - Unverified claims
- Re-run affected reviews after fixes; release only when both reviewers report PASS.

Fallback

If multi-agent execution is unavailable, do not stop. Run the Implementer for the exporter and tests first, then the Implementer for the reproduction guide, followed by the Engineering Reviewer and then the Reproducibility Reviewer; preserve the same integration order and fix ownership. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 FAIL — isolated writers omit actual
`Files` interfaces; 6 PASS; 7 PASS; 8 PASS; 9 PASS; 10 PASS; 11 PASS;
12 PASS. Verdict: **FAIL — 11/12**.

## Behavior failure: generality_final_v4_3

```text
Assignments

- Implementer — isolated worktree; Consumes: schema v2. Produces: manifest exporter and its tests. Files: exporter implementation and exporter test files.
- Implementer — isolated worktree; Consumes: frozen CLI output contract. Produces: reproduction guide. Files: reproduction-guide documentation files.
- Engineering Reviewer — reviews exporter, tests, integration order, and CLI-contract compliance.
- Reproducibility Reviewer — reviews the release reproduction guide and release reproducibility claims.
- Scientific Reviewer is not assigned: this is frozen-spec consumption, not an algorithm, objective, data-semantics, optimization, schedule, or evaluation change.

Execution

Two responsible Implementers execute the isolated units concurrently. Independent read-only investigations and reviews may run in parallel. Integrate exporter-first, then guide-second serially; confirm the exporter and tests are integrated before integrating the guide.

Review cycle

Engineering Reviewer and Reproducibility Reviewer inspect the integrated primary artifacts. Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers. Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Reviewer fields:

- Verdict: PASS|NEEDS_FIXES|BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Fallback

If multi-agent execution is unavailable, do not stop. The Implementer for the exporter and tests executes first, followed by the Implementer for the reproduction guide after exporter integration; Engineering Reviewer then reviews, followed by Reproducibility Reviewer. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 PASS; 6 FAIL — no explicit
shared-checkout concurrent-write prohibition; 7 PASS; 8 PASS; 9 PASS;
10 PASS; 11 PASS; 12 PASS. Verdict: **FAIL — 11/12**.

## Harness-invalid: original_final_v5_1

The condensed harness said “exact five fields” without listing their names.

```text
Assignments

- Implementer: the sole writer for all checkout changes—training loop, FSDP wrapper, and test fixes.
- Scientific Reviewer: read-only review of algorithm, objective, data semantics, optimization, schedule, and evaluation risks.
- Engineering Reviewer: read-only review of FSDP integration, implementation quality, and tests.
- Reproducibility Reviewer: not assigned unless this is a release or explicitly requests reproducibility review.

Execution

Independent read-only investigations and reviews may run in parallel.

Concurrent writes in one shared checkout are prohibited.

The Implementer integrates all findings and writes sequentially. If isolated worktrees are used later, each assignment explicitly labels actual Consumes, Produces, Files, and serial integration.

Review cycle

Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.

Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Each reviewer records exactly these five fields:

1. Scope
2. Primary artifacts inspected
3. Findings
4. Evidence
5. Pass/fail decision

Fallback

If multi-agent execution is unavailable, do not stop. One Implementer performs all writes and separately performs the reviewer checklists after each change, preserving the same evidence standard. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 PASS; 6 PASS; 7 PASS; 8 PASS;
9 PASS; 10 PASS; 11 PASS; 12 FAIL — wrong five reviewer fields.
Verdict: **FAIL — 11/12; harness-invalid**.

## Harness-invalid: original_final_v5_2

```text
Assignments

- Implementer: exactly one; owns all checkout writes—training loop, FSDP wrapper, and any test fixes.
- Scientific Reviewer: reviews algorithm, objective, data semantics, optimization, schedule, and evaluation risk.
- Engineering Reviewer: reviews engineering correctness and integration.
- Reproducibility Reviewer: assigned only for a release or explicit reproducibility review.

Execution

“Independent read-only investigations and reviews may run in parallel.”

“Concurrent writes in one shared checkout are prohibited.”

The single Implementer makes every write and runs relevant checks. If isolated writers are used instead, each explicitly labels actual **Consumes**, **Produces**, and **Files**; their changes are integrated serially by one Implementer.

Review cycle

“Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.”

“Implementer summaries are context, never evidence; reviewers inspect primary artifacts.”

Each reviewer records exactly five fields: **Scope; Primary artifacts inspected; Findings; Required fixes; Pass/fail decision.** Scientific review handles scientific risks; Engineering review handles engineering risks; Reproducibility review occurs only when assigned.

Fallback

If multi-agent execution is unavailable, do not stop. One Implementer performs the work and then conducts separate review passes using the same five reviewer fields, prioritizing Scientific then Engineering review; add Reproducibility review only for release or an explicit reproducibility request. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 PASS; 6 PASS; 7 PASS; 8 PASS;
9 PASS; 10 PASS; 11 PASS; 12 FAIL — wrong five reviewer fields.
Verdict: **FAIL — 11/12; harness-invalid**.

## Behavior failure: original_final_v5r_4

```text
Assignments

- Implementer — owns all checkout writes: training loop, FSDP wrapper, and test fixes.
- Engineering Reviewer — reviews FSDP-wrapper engineering risk.

Execution

Independent read-only investigations and reviews may run in parallel.

Concurrent writes in one shared checkout are prohibited.

Use exactly one Implementer for all writes.

Review cycle

Each responsible Implementer remains available to fix findings until reviews pass; fix ownership never transfers.

Implementer summaries are context, never evidence; reviewers inspect primary artifacts.

Engineering Reviewer returns exactly:

Verdict: PASS | NEEDS_FIXES | BLOCKED
Evidence
Blocking findings
Non-blocking findings
Unverified claims

Fallback

If multi-agent execution is unavailable, do not stop. Run the Implementer contract, then the Engineering Reviewer contract sequentially; the Implementer fixes findings and the reviewer re-reviews until passing. This fallback has reduced review independence.
```

Rubric: 1 PASS; 2 PASS; 3 PASS; 4 PASS; 5 PASS; 6 FAIL — Scientific Reviewer
is missing for the training-loop meaning risk; 7 PASS; 8 PASS; 9 PASS;
10 PASS; 11 PASS; 12 PASS. Verdict: **FAIL — 11/12**.
