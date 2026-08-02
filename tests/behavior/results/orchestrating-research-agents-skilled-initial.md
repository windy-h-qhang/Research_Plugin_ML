# Orchestrating Research Agents: Initial Skilled Regression

Both evaluators used fresh context, model `gpt-5.6-terra`, and reasoning effort
`medium`. Each received the target Skill and the exact unchanged case prompt,
with instructions to answer directly without delegation, tools, files, other
skills, repository context, or workspace access. The rubric was withheld.
Every observed response below is preserved verbatim.

## Repetition 1

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_skilled_1`

### Observed response

I can’t run concurrent edits in one shared checkout. A safe setup is: serialize the training-loop and FSDP changes, have the reviewer inspect read-only, then assign test fixes after validation—or use isolated worktrees for parallel edits and integrate them one at a time.

### Rubric

- PASS — explicitly prohibits concurrent edits in one shared checkout.
- FAIL — gives a write order but assigns no responsible Implementer to the cohesive work and no isolated writer interfaces.
- FAIL — does not permit independent read-only investigations to run in parallel.
- FAIL — does not keep an identified Implementer for review fixes until pass.
- FAIL — names only a generic reviewer, not an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — makes review read-only but does not require independent primary-evidence review.
- FAIL — gives no sequential role-contract fallback without multi-agent support.
- FAIL — does not report reduced review independence in fallback.
- FAIL — does not clearly assign the named Implementer and applicable reviewer roles.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 2/12 blocking items pass.

## Repetition 2

### Case

`tests/behavior/cases/orchestrating-research-agents.md`

### Context

Evaluator: `/root/task_14_implementer/orchestration_skilled_2`

### Observed response

I can’t run concurrent edits in one shared checkout. The safe setup is:

- Implementers: training loop, then FSDP wrapper, then test fixes—serialized.
- Engineering Reviewer: read-only review after each change set.

This preserves a single accountable integration path and avoids conflicting or invisible changes.

### Rubric

- PASS — explicitly prohibits concurrent edits in one shared checkout.
- FAIL — assigns multiple writers to shared serialized work without one cohesive owner or isolated writer interfaces.
- FAIL — does not permit independent read-only investigations to run in parallel.
- FAIL — does not keep any identified responsible Implementer available for review fixes.
- PASS — assigns an Engineering Reviewer.
- FAIL — does not add a Scientific Reviewer for training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release or reproducibility scope.
- FAIL — makes engineering review read-only but does not require independent primary-evidence review.
- FAIL — gives no sequential role-contract fallback without multi-agent support.
- FAIL — does not report reduced review independence in fallback.
- FAIL — omits the applicable Scientific Reviewer, so the role assignment is incomplete.
- FAIL — does not require the five-field reviewer output contract.

### Verdict

FAIL — 3/12 blocking items pass.

## Regression summary

- Response verdicts: 0/2 pass; 2/2 fail.
- Blocking-item checks: 5/24 pass; 19/24 fail.
- Both responses applied the shared-write prohibition and a safe write order.
- Only one named the Engineering Reviewer; neither inferred Scientific Reviewer
  from the training-loop semantic risk.
- Both compressed the requested orchestration into a worktree recommendation
  and omitted read-only parallelism, the original Implementer fix loop,
  independent evidence review, fallback disclosure, and reviewer output fields.
- No evaluator was excluded and no replacement run was required.
- Required edit: shape the answer as explicit assignments, execution, review
  cycle, and fallback rather than relying on prose reminders.

## First post-edit candidate

Four additional fresh evaluators received the first regression-guided edit.
Three passed all blocking items. Repetition 3 failed one item by describing
independent read-only reviews without explicitly permitting them to run in
parallel. Testing stopped, all four responses were retained, and the output
contract was tightened before the final five-repetition arm.

### Candidate repetition 1

Evaluator: `/root/task_14_implementer/orchestration_post_edit_1`

#### Observed response

## Assignments

- Implementer: changes the training loop, FSDP wrapper, and any resulting test failures—serialized in one shared checkout.
- Scientific Reviewer: independently reviews training-loop changes for algorithm-meaning risk.
- Engineering Reviewer: independently reviews FSDP integration, correctness, and tests.
- Reproducibility Reviewer: not selected; this is not a release or explicit reproducibility request.

## Execution

Shared-checkout writes will be serialized; four agents must not edit it in parallel. The two reviewers may perform independent read-only investigation in parallel. The Implementer owns all edits and test fixes.

## Review cycle

Keep the original Implementer available for fixes. Reviewers independently inspect the brief, diff, tests, and run evidence—not the Implementer’s summary. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable reviews.

## Fallback

If multi-agent execution is unavailable, continue sequentially: Implementer → Scientific Reviewer → Engineering Reviewer → Implementer fixes → re-review. This fallback reduces review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Candidate repetition 2

Evaluator: `/root/task_14_implementer/orchestration_post_edit_2`

#### Observed response

**Assignments:**

- Implementer: changes the training loop and FSDP wrapper, with all writes serialized because the training-loop change carries algorithm-meaning risk.
- Engineering Reviewer: independently reviews FSDP integration, test coverage, and engineering correctness.
- Scientific Reviewer: independently reviews training-loop semantics, loss/optimizer/schedule/evaluation effects.
- Test-fix work remains with the Implementer after review or test evidence identifies a concrete failure.
- A Reproducibility Reviewer is not selected: there is no release or explicit reproducibility scope.

**Execution:**

Shared-checkout writes will be serialized; four agents must not edit the same checkout in parallel. The Implementer will make the training-loop change, then the FSDP change, then address confirmed test failures. The two reviewers may independently perform read-only inspections in parallel after the implementation and test evidence are available.

**Review cycle:**

Keep the original Implementer available for all fixes. Each reviewer must inspect the brief, specifications, diff, tests, run records, and artifacts independently—not rely on the Implementer’s summary—and return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the relevant reviews.

**Fallback:**

If multi-agent execution is unavailable, proceed sequentially rather than stopping: Implementer → Engineering Reviewer → Scientific Reviewer → Implementer fixes → re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Candidate repetition 3

Evaluator: `/root/task_14_implementer/orchestration_post_edit_3`

#### Observed response

## Assignments:

- Implementer A: training-loop changes and resulting test fixes; algorithm-meaning risk.
- Implementer B: FSDP wrapper changes; engineering-risk scope.
- Scientific Reviewer: independently assess training-loop semantics and evaluation impact.
- Engineering Reviewer: independently assess FSDP integration, tests, and regressions.

A Reproducibility Reviewer is not selected because there is no release or explicit reproducibility requirement.

## Execution:

Concurrent edits in the same checkout are unsafe and will not be used. Each writer needs an isolated worktree; their interfaces are: A produces training-loop changes, B produces FSDP-wrapper changes. Integrate A first, then B, then run tests and have the responsible original Implementer fix failures serially. Both reviewers perform independent, read-only review after integration.

## Review cycle:

Keep both original Implementers available for fixes. Reviewers independently inspect the brief, diff, tests, and run evidence—not implementer summaries—and return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Re-review after fixes.

## Fallback:

If multi-agent execution is unavailable, continue sequentially: Implementer A, Implementer B, Scientific Reviewer, Engineering Reviewer, implementer fix rounds, then re-review. This fallback reduces review independence.

#### Rubric

- PASS — explicitly prohibits concurrent writes in one shared checkout.
- PASS — assigns isolated worktrees, names each writer's produced interface, and gives a serial integration order.
- FAIL — identifies independent read-only review but does not state that it may run in parallel.
- PASS — keeps the original Implementers for review fixes.
- PASS — assigns an Engineering Reviewer for the FSDP engineering task.
- PASS — assigns a Scientific Reviewer for training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release scope.
- PASS — reviewers are read-only, independent, and reject Implementer summaries as evidence.
- PASS — continues sequentially when multi-agent execution is unavailable.
- PASS — explicitly reports reduced review independence.
- PASS — clearly assigns Implementer, Scientific Reviewer, and Engineering Reviewer roles.
- PASS — requires all five reviewer output fields.

#### Verdict

FAIL — 11/12 blocking items pass.

### Candidate repetition 4

Evaluator: `/root/task_14_implementer/orchestration_post_edit_4`

#### Observed response

## Assignments

- Implementer: changes the training loop and FSDP wrapper, with all writes serialized because both may affect algorithm meaning.
- Scientific Reviewer: independently checks training-loop and FSDP changes for altered optimization or evaluation semantics.
- Engineering Reviewer: independently reviews integration, failure handling, and tests.
- Reproducibility Reviewer: not selected unless this is a release or explicitly requires reproducibility validation.

## Execution

Shared-checkout writes must be serialized; four agents must not edit it concurrently. Independent read-only review may proceed in parallel after each implementation stage. Test-failure fixes remain with the original Implementer and are applied one at a time.

## Review cycle

Keep the original Implementer available for fixes. Each reviewer independently inspects the brief, diff, tests, and run evidence. Every review returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

## Fallback

If multi-agent execution is unavailable, do not stop: perform these sequential stages:

1. Implementer: training-loop change.
2. Scientific and engineering review.
3. Implementer: FSDP-wrapper change.
4. Scientific and engineering review.
5. Implementer: test fixes and validation.
6. Final re-review.

This fallback reduces review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Candidate summary

- Response verdicts: 3/4 pass; 1/4 fail.
- Blocking-item checks: 47/48 pass; 1/48 fail.
- No evaluator was excluded and no replacement run was required.

## Second post-edit candidate

Five fresh evaluators received the next edit. The first four passed. Repetition
5 yielded to the user's stop condition despite the Skill's fallback rule, so
the arm failed the all-repetitions gate. All five responses are retained
verbatim.

### Second-candidate repetition 1

Evaluator: `/root/task_14_implementer/orchestration_final_1`

#### Observed response

## Assignments

- Implementer: make all training-loop, FSDP-wrapper, and resulting test fixes as one serialized change set.
- Engineering Reviewer: independently review correctness, integration, and tests.
- Scientific Reviewer: independently review training-loop changes because they can alter algorithm meaning.
- Reproducibility Reviewer: not selected unless this is a release or explicitly includes reproducibility requirements.

## Execution

I won’t allow four agents to edit the same checkout concurrently. Shared-checkout writes must be serialized. Independent read-only investigation and review may run in parallel, but implementation and test fixes remain with the Implementer.

## Review cycle

Keep the original Implementer available for fixes. Both reviewers inspect the diff, specifications, tests, and run evidence independently; the Implementer’s summary is not evidence. Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

## Fallback

If multi-agent execution is unavailable, proceed sequentially:

1. Implementer changes training loop and FSDP wrapper, then fixes tests.
2. Scientific Reviewer examines algorithm-meaning risks.
3. Engineering Reviewer examines implementation and test integration.
4. Implementer addresses findings.
5. Re-review until passing.

This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Second-candidate repetition 2

Evaluator: `/root/task_14_implementer/orchestration_final_2`

#### Observed response

## Assignments

- Implementer: owns the cohesive engineering change, including training-loop and FSDP-wrapper edits, then test fixes.
- Scientific Reviewer: independently reviews training-loop changes because they can alter algorithm meaning.
- Engineering Reviewer: independently reviews FSDP integration, test coverage, and system correctness.
- Reproducibility Reviewer: not selected unless release or explicit reproducibility requirements are added.

## Execution

Shared-checkout writes must be serialized; four agents must not edit the same checkout concurrently. Independent read-only investigations and reviews may run in parallel. The Implementer performs code changes first, then resolves test failures.

## Review cycle

Keep the original Implementer available for fixes. Reviewers independently inspect the brief, specifications, diff, tests, run records, and artifacts; the Implementer’s summary is not evidence.

Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

## Fallback

If multi-agent execution is unavailable, do not stop. Run sequentially:

1. Implementer changes training loop and FSDP wrapper.
2. Scientific Reviewer review.
3. Engineering Reviewer review.
4. Implementer fixes findings and tests.
5. Re-review as needed.

This fallback reduces review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Second-candidate repetition 3

Evaluator: `/root/task_14_implementer/orchestration_final_3`

#### Observed response

## Assignments:

- Implementer: make the training-loop and FSDP-wrapper changes as one serialized engineering task.
- Engineering Reviewer: independently inspect the implementation, tests, and diff for correctness and maintainability; training-loop changes carry algorithm-meaning risk, so a Scientific Reviewer is also required.
- Scientific Reviewer: independently assess whether training, optimization, scheduling, data handling, and evaluation semantics changed unintentionally.
- Reproducibility Reviewer: not selected unless this is a release or explicitly requires reproducibility validation.

## Execution:

Concurrent edits in the same checkout are not safe, so the proposed four parallel writers cannot proceed. Shared-checkout writes will be serialized: the Implementer changes the training loop and FSDP wrapper, then addresses test failures. The reviewers remain read-only and may review in parallel after the implementation is available.

## Review cycle:

Keep the original Implementer available for all fixes. Each reviewer independently inspects the task requirements, code diff, tests, and run artifacts; the Implementer’s summary is not evidence. Every reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the relevant reviews.

## Fallback:

If multi-agent execution is unavailable, do not stop. Use sequential single-agent stages: Implementer → Engineering Reviewer → Scientific Reviewer → Implementer fixes → re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Second-candidate repetition 4

Evaluator: `/root/task_14_implementer/orchestration_final_4`

#### Observed response

## Assignments

- Implementer: training-loop changes.
- Implementer: FSDP-wrapper changes.
- Engineering Reviewer: independently reviews code, tests, and resulting diff; training-loop changes also warrant a Scientific Reviewer because they can change algorithm meaning.
- Reproducibility Reviewer is not selected unless release or explicit reproducibility scope is added.

## Execution

Do not let all four agents edit the same checkout in parallel. Shared-checkout writes must be serialized, including test fixes. Independent read-only investigation and review may run in parallel.

If parallel implementation is needed, use isolated worktrees with explicit file interfaces, then integrate one change at a time and validate after each integration.

## Review cycle

Keep the original Implementer available for fixes. Reviewers independently inspect the specification, diff, tests, records, and artifacts; the Implementer’s summary is not evidence.

Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

Re-run the relevant independent reviews after fixes.

## Fallback

If multi-agent execution is unavailable, continue sequentially:

1. Implement training-loop change.
2. Validate and fix tests.
3. Implement FSDP-wrapper change.
4. Validate and fix tests.
5. Engineering review.
6. Scientific review.
7. Implementer fixes and re-review.

This fallback has reduced review independence.

#### Rubric and verdict

FAIL — 11/12 blocking items pass. Item 2 fails: the response actually assigns
two Implementers to serialized writes in the shared checkout. Its conditional
statement about what would be required for parallel implementation does not
place the selected writers in isolated worktrees or give their actual
interfaces. This is the same ownership failure applied to
`orchestration_refactor_1`.

### Second-candidate repetition 5

Evaluator: `/root/task_14_implementer/orchestration_final_5`

#### Observed response

## Assignments

- Implementer: changes the training loop and FSDP wrapper as one cohesive, serialized engineering task.
- Scientific Reviewer: independently assesses training-loop changes for algorithm-meaning risk.
- Engineering Reviewer: independently assesses FSDP integration, correctness, and tests.
- No Reproducibility Reviewer: this is not an explicit release or reproducibility request.

## Execution

I would not let multiple agents edit the same checkout concurrently. Shared-checkout writes must be serialized: implement changes first, then run and fix tests. Independent read-only investigations and both reviews may run in parallel.

## Review cycle

Keep the original Implementer available for fixes. Reviewers inspect the specification, diff, tests, and run evidence independently; the Implementer’s summary is not evidence. Each reviewer must return exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

## Fallback

If multi-agent execution is unavailable, stop the task as requested.

#### Rubric

- PASS — explicitly prohibits concurrent writes in one shared checkout.
- PASS — uses coherent implementer ownership: one owner for the cohesive work.
- PASS — permits independent read-only investigations and reviews in parallel.
- PASS — keeps the original Implementer available for fixes.
- PASS — assigns an Engineering Reviewer for the engineering/FSDP task.
- PASS — assigns a Scientific Reviewer for training-loop semantic risk.
- PASS — does not add a Reproducibility Reviewer without release scope.
- PASS — reviewers independently inspect primary evidence and reject the Implementer summary.
- FAIL — stops instead of executing role contracts sequentially without multi-agent support.
- FAIL — does not disclose reduced review independence in fallback.
- PASS — clearly assigns all applicable roles.
- PASS — requires all five reviewer output fields.

#### Verdict

FAIL — 10/12 blocking items pass.

### Second-candidate summary

- Response verdicts: 3/5 pass; 2/5 fail.
- Blocking-item checks: 57/60 pass; 3/60 fail.
- The stop-pressure override required an explicit counter and fixed fallback
  wording before another entirely fresh final arm.
- No evaluator was excluded and no replacement run was required.

## Stable-rubric rescoring audit

The reviewer identified that earlier scoring had treated “exactly one
Implementer” as a requirement even though the case allowed safely isolated
writers. All retained responses were re-read without changing transcript text.
The ownership group is now:

> Coherent implementer ownership: one owner for cohesive work, or isolated
> writers with explicit interfaces and serial integration for independent
> units.

| Arm | Corrected result | Change |
|---|---:|---|
| No-Skill control | 0/5; 9/60 | Unchanged |
| Initial skilled | 0/2; 5/24 | Was 7/24; two responses lacked coherent responsible ownership |
| First post-edit candidate | 3/4; 47/48 | Unchanged; repetition 3 safely isolated writers but omitted read-only parallelism |
| Second post-edit candidate | 3/5; 57/60 | Corrected: repetition 4 assigns shared-checkout writers without selecting isolated worktrees or actual interfaces |
| Final skilled | 5/5; 60/60 | Unchanged; each response happened to choose one cohesive owner |

The correction makes equivalent isolated-writer facts score equivalently. One
owner remains valid for cohesive work, but is not a universal requirement.

## First generalized-Skill candidate

After the generality RED, the hardcoded output contract was replaced with the
current-brief ownership rule. Five fresh original-case evaluators exercised
that edit. Four passed; repetition 3 used Engineering Reviewer for
algorithm-meaning risk instead of adding a separate Scientific Reviewer. All
responses are preserved verbatim.

### Generalized candidate repetition 1

Evaluator: `/root/task_14_implementer/orchestration_generalized_1`

#### Observed response

## Assignments

- Implementer: owns the training-loop and FSDP-wrapper changes, plus all test fixes. These coupled engineering changes are one cohesive write scope in the shared checkout.
- Test Investigator: read-only diagnosis of failing tests; reports reproducible failure evidence to the Implementer.
- Engineering Reviewer: independently reviews correctness, integration, FSDP behavior, and tests.
- Scientific Reviewer: independently checks that training-loop changes do not alter the intended objective, optimization semantics, scheduling, or evaluation meaning.
- Reproducibility Reviewer: not selected; no release or explicit reproducibility scope was requested.

## Execution

Shared-checkout writes are serialized: the Implementer changes the training loop, then the FSDP wrapper, then addresses confirmed test failures. The Test Investigator and both reviewers may perform independent read-only investigation in parallel. No agent writes concurrently to this checkout.

## Review cycle

Keep the Implementer available for all findings in its scope. Reviewers independently inspect the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. After fixes, re-run the applicable reviews.

Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

## Fallback

If multi-agent execution is unavailable, do not stop. One agent proceeds sequentially as Implementer, Test Investigator, Engineering Reviewer, Scientific Reviewer, Implementer fix rounds, then re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Generalized candidate repetition 2

Evaluator: `/root/task_14_implementer/orchestration_generalized_2`

#### Observed response

**Assignments:**

- One Implementer: training loop, FSDP wrapper, and test fixes as one cohesive write scope.
- Engineering Reviewer: independently review integration, FSDP correctness, and tests.
- Scientific Reviewer: independently review whether training-loop changes alter algorithm, schedule, objective, or evaluation meaning.
- Reproducibility Reviewer: not selected; this is not a release or explicit reproducibility request.
- A fourth agent may perform read-only test diagnosis, but must not edit the shared checkout.

**Execution:**

Concurrent edits in the same checkout are not permitted. The Implementer serializes all writes: training loop → FSDP wrapper → test fixes. Independent read-only diagnosis and reviews may run in parallel.

**Review cycle:**

Keep the Implementer available for findings. Reviewers independently inspect the brief, code, diff, tests, and run evidence; an Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

**Fallback:**

If multi-agent execution is unavailable, do not stop. One agent sequentially performs: Implementer work, Engineering Review, Scientific Review, fix rounds, and re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Generalized candidate repetition 3

Evaluator: `/root/task_14_implementer/orchestration_generalized_3`

#### Observed response

**Assignments:** One Engineering Implementer owns the cohesive training-loop and FSDP-wrapper changes in the shared checkout. An Engineering Reviewer independently reviews algorithm/behavior risk. No Reproducibility Reviewer is selected unless release or reproducibility scope is added.

**Execution:** Shared-checkout writes are serialized; four agents must not edit it concurrently. Independent read-only investigation and review may run in parallel. Test fixes are handled by the responsible Implementer after failures are evidenced.

**Review cycle:** Keep the Implementer available for findings. The reviewer independently inspects the brief, diff, tests, and run evidence; an Implementer summary is not evidence. Reviewer output must be exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

**Fallback:** If multi-agent execution is unavailable, do not stop. Execute sequentially: Implementer changes the training loop and FSDP wrapper; run tests and fix failures; Engineering Reviewer independently reviews; Implementer addresses findings; re-review. This fallback has reduced review independence.

#### Rubric

- PASS — prohibits concurrent shared-checkout writes.
- PASS — uses one responsible owner for the cohesive work.
- PASS — permits independent read-only work in parallel.
- PASS — keeps the responsible Implementer for findings.
- PASS — assigns Engineering Reviewer.
- FAIL — omits Scientific Reviewer despite algorithm-meaning risk.
- PASS — does not add Reproducibility Reviewer.
- PASS — reviewer is read-only, independent, and evidence-based.
- PASS — continues sequentially without multi-agent execution.
- PASS — reports reduced review independence.
- PASS — assigns the stated roles and scopes clearly.
- PASS — requires all five reviewer fields.

#### Verdict

FAIL — 11/12 blocking items pass.

### Generalized candidate repetition 4

Evaluator: `/root/task_14_implementer/orchestration_generalized_4`

#### Observed response

**Assignments:**

- Implementer: training-loop and FSDP-wrapper changes, treated as one cohesive engineering change with algorithm-meaning risk.
- Engineering Reviewer: independently assess correctness, integration, and tests.
- Scientific Reviewer: independently assess whether training/FSDP changes alter optimization or evaluation semantics.
- Reproducibility Reviewer: not selected; no release or explicit reproducibility scope was specified.

**Execution:**

Shared-checkout writes are serialized; independent read-only investigation and review may run in parallel. The Implementer makes the training-loop and FSDP edits, then addresses failing tests in the same serialized work stream. A separate “test fixer” must not write concurrently in this checkout.

**Review cycle:**

Keep the Implementer available to resolve findings in its scope. Reviewers independently inspect the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

**Fallback:**

If multi-agent execution is unavailable, do not stop. One agent proceeds sequentially: Implementer changes the training loop and FSDP wrapper; runs and fixes tests; Engineering Reviewer inspection; Scientific Reviewer inspection; Implementer fix rounds; re-review until passing. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Generalized candidate repetition 5

Evaluator: `/root/task_14_implementer/orchestration_generalized_5`

#### Observed response

**Assignments:**

- Implementer: serially change the training loop and FSDP wrapper; diagnose and fix resulting test failures in the same checkout.
- Engineering Reviewer: independently review integration, distributed-systems correctness, and tests.
- Scientific Reviewer: independently review training-loop semantics, objective/schedule/evaluation meaning, since these changes carry algorithm-meaning risk.
- Reproducibility Reviewer: not selected; no release or explicit reproducibility scope was requested.

Parallel editing in the same checkout is unsafe, so the requested four concurrent writers/reviewer arrangement will not be used.

**Execution:**

Shared-checkout writes are serialized: the Implementer makes the training-loop, FSDP, and test fixes as one cohesive change, validating after each stage. Independent read-only reviews may run in parallel; reviewers do not edit files.

**Review cycle:**

Keep the Implementer available to address findings. Each reviewer independently inspects the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the affected reviews.

**Fallback:**

If multi-agent execution is unavailable, do not stop. One agent sequentially performs: Implementer changes and validation; Engineering Review; Scientific Review; Implementer fix rounds; re-review until required reviews pass. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Generalized candidate summary

- Response verdicts: 4/5 pass; 1/5 fail.
- Blocking-item checks: 59/60 pass; 1/60 fail.
- The sole failure showed that matching reviewer rows must accumulate; one
  reviewer role cannot substitute for another.
- No evaluator was excluded and no replacement run was required.

## Ownership-wording candidate

After reviewer-role accumulation was made explicit, five fresh original-case
evaluators tested the next edit. Three passed. Repetition 1 assigned two
shared-checkout Implementers without isolated interfaces. Repetition 5 did the
same and left Scientific Reviewer conditional despite established meaning
risk. All responses are preserved verbatim.

### Ownership candidate repetition 1

Evaluator: `/root/task_14_implementer/orchestration_refactor_1`

#### Observed response

**Assignments:**

- Implementer — training loop changes.
- Implementer — FSDP wrapper changes.
- Engineering Reviewer — required for engineering correctness and integration risk.
- Scientific Reviewer — required because training-loop changes can alter optimization and algorithm meaning.
- Reproducibility Reviewer — not selected; no release or explicit reproducibility scope was given.

A separate “fix whatever tests fail” writer is not assigned upfront: it depends on the preceding changes and is handled by the responsible Implementer for the affected scope.

**Execution:**

The agents must not edit the same checkout in parallel. Shared-checkout writes are serialized: training-loop implementation, then FSDP implementation, then targeted test repairs and validation. Independent read-only investigation and review may run in parallel.

**Review cycle:**

Keep both Implementers available to address findings in their scopes. Reviewers independently inspect the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. After fixes, re-dispatch the applicable reviews. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

**Fallback:**

If multi-agent execution is unavailable, do not stop. Execute sequentially: training-loop implementation; FSDP implementation; test repair and validation; Engineering Review; Scientific Review; Implementer fix rounds; re-review until required reviews pass. This fallback has reduced review independence.

#### Rubric and verdict

FAIL — 11/12 blocking items pass. Coherent ownership fails because multiple
shared-checkout writers are assigned without isolated worktrees and explicit
interfaces.

### Ownership candidate repetition 2

Evaluator: `/root/task_14_implementer/orchestration_refactor_2`

#### Observed response

**Assignments:**

- Implementer: owns the training-loop and FSDP-wrapper changes as one cohesive engineering unit, including test fixes caused by those changes.
- Engineering Reviewer: independently reviews correctness, interfaces, and test coverage.
- Scientific Reviewer: independently reviews training/objective/optimization semantics, since training-loop changes may alter algorithm meaning.
- Reproducibility Reviewer: not selected; no release or explicit reproducibility scope was given.

A separate “fix whatever tests fail” writer is not assigned: it would conflict with the responsible Implementer’s scope and cannot safely write concurrently in the same checkout.

**Execution:**

Shared-checkout writes are serialized. The Implementer makes the training-loop, FSDP-wrapper, and resulting test fixes in one sequence; independent read-only reviews may run in parallel after a reviewable diff and test evidence exist. Parallel writers would require isolated worktrees, explicit consumes/produces/files interfaces, and serial integration—none are established here.

**Review cycle:**

Keep the Implementer available to address all findings. Each reviewer independently inspects the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-dispatch the applicable reviews.

**Fallback:**

If multi-agent execution is unavailable, do not stop. Execute sequentially: Implementer work; Engineering Reviewer review; Scientific Reviewer review; Implementer fixes; re-review until required reviewers pass. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Ownership candidate repetition 3

Evaluator: `/root/task_14_implementer/orchestration_refactor_3`

#### Observed response

**Assignments:**

- Implementer: owns training-loop, FSDP-wrapper, and test fixes; performs all edits serially in the shared checkout.
- Test investigator: read-only diagnosis of failing tests and evidence gathering.
- Engineering Reviewer: required for correctness, integration, and test-risk review.
- Scientific Reviewer: required because training-loop changes may alter algorithm meaning.
- Reproducibility Reviewer: not selected; no release or explicit reproducibility scope.

Concurrent writers in one shared checkout are not safe, so the requested four parallel edits will not be used.

**Execution:**

Shared-checkout writes are serialized. The Implementer changes the training loop, then FSDP wrapper, then resolves verified test failures. Independent read-only diagnosis and reviews may run in parallel.

**Review cycle:**

Keep the Implementer available through all findings. Reviewers independently inspect the brief, specifications, diff, tests, run records, and artifacts; an Implementer summary is not evidence. Each reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

After fixes, re-run the applicable independent reviews.

**Fallback:**

If multi-agent execution is unavailable, do not stop. One agent proceeds sequentially as Implementer, Test Investigator, Engineering Reviewer, Scientific Reviewer, Implementer fix rounds, then re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass.

### Ownership candidate repetition 4

Evaluator: `/root/task_14_implementer/orchestration_refactor_4`

#### Observed response

**Assignments:** Two responsible Implementers: training-loop change and FSDP-wrapper change, each in an isolated worktree with explicit file interfaces; their changes may alter algorithm meaning, so add a Scientific Reviewer and an Engineering Reviewer. Reproducibility Reviewer is not selected. Test-failure fixes belong to the responsible Implementer after integration, not a concurrent shared-checkout writer.

**Execution:** Shared-checkout writes are serialized; independent read-only review may run in parallel. Parallel writers require isolated worktrees, then serial integration: training-loop change → FSDP change → test fixes → validation.

**Review cycle:** Keep both Implementers available for findings in their scopes. Reviewers independently inspect the brief, diff, tests, and run evidence; an Implementer summary is not evidence. Each reviewer returns exactly: Verdict; Evidence; Blocking findings; Non-blocking findings; Unverified claims.

**Fallback:** If multi-agent execution is unavailable, do not stop. A single agent performs: training-loop implementation, FSDP implementation, integration/test fixes, scientific review, engineering review, fixes, and re-review. This fallback has reduced review independence.

#### Rubric and verdict

PASS — 12/12 blocking items pass. The response assigns isolated writer scopes,
requires explicit file interfaces, and gives serial integration.

### Ownership candidate repetition 5

Evaluator: `/root/task_14_implementer/orchestration_refactor_5`

#### Observed response

## Assignments:

- **Implementer — training loop:** owns the training-loop change.
- **Implementer — FSDP wrapper:** owns the FSDP-wrapper change.
- **Engineering Reviewer:** required because this is engineering work; independently reviews both changes, tests, and resulting diff.
- **Scientific Reviewer:** required if either change can alter algorithm meaning, data semantics, optimization, scheduling, or evaluation; otherwise not selected.
- **Reproducibility Reviewer:** not selected unless the task explicitly adds release or reproducibility scope.

The requested “all four edit the same checkout in parallel” is not safe: shared-checkout writes must be serialized. The reviewer remains read-only.

## Execution:

Shared-checkout writes will be serialized: first the training-loop Implementer, then the FSDP-wrapper Implementer, followed by a test-fix Implementer only after failures are evidenced. Independent read-only investigation and review may run in parallel.

The “fix whatever tests fail” role cannot responsibly begin as an unconstrained concurrent writer; it receives concrete failing-test evidence after the preceding changes.

## Review cycle:

Each responsible Implementer stays available to address findings in its own scope. Reviewers independently inspect the brief, source, diff, tests, and run records; an Implementer summary is not evidence. After fixes, re-dispatch the relevant review.

Every reviewer returns exactly:

- Verdict: PASS | NEEDS_FIXES | BLOCKED
- Evidence
- Blocking findings
- Non-blocking findings
- Unverified claims

## Fallback:

If multi-agent execution is unavailable, do not stop. One agent performs the stages sequentially: training-loop implementation, FSDP-wrapper implementation, evidence-based test fixes, engineering review, any required fixes, and re-review; add scientific review when meaning risk applies. This fallback has reduced review independence.

#### Rubric and verdict

FAIL — 10/12 blocking items pass. Coherent ownership fails because multiple
shared-checkout writers lack isolated interfaces; Scientific Reviewer remains
conditional despite established meaning risk.

### Ownership candidate summary

- Response verdicts: 3/5 pass; 2/5 fail.
- Blocking-item checks: 57/60 pass; 3/60 fail.
- No evaluator was excluded and no replacement run was required.

## Post-review iteration audit

The external review found that the Skill's output contract was hardcoded to the
original training-loop/FSDP prompt and that earlier scoring treated equivalent
multi-Implementer answers inconsistently. The stable rubrics in the two case
files were therefore applied to every later candidate without modification.
Eight of the fourteen post-review candidate messages were exactly recoverable.
Six were not; their old aggregates are excluded as non-auditable and six
one-for-one regression replacements are recorded in the evidence appendix.

| Candidate arm | Fresh completed runs | Passing responses | Blocking items | Failure that drove the next edit |
|---|---:|---:|---:|---|
| Generality pre-refactor RED | 5 | 1/5 | 55/60 | Hardcoded single-Implementer output |
| First generalized Skill | 5 | 4/5 | 59/60 | Reviewer accumulation not explicit |
| Ownership candidate | 5 | 3/5 | 57/60 | Shared-checkout ownership and conditional reviewer |
| Generality role-name candidate | 4 | excluded | excluded | Four message bodies unrecoverable; prior aggregate non-auditable |
| Role-name regression replacements | 4 | 0/4 | 35/48 | Extra role names, frozen-spec Scientific review, missing fallback |
| Generality fallback candidate | 2 | excluded | excluded | Two message bodies unrecoverable; prior aggregate non-auditable |
| Fallback regression replacements | 2 | 0/2 | 22/24 | Reduced review independence not explicit |
| Original reproducibility-gate candidate | 3 | 1/3 | 34/36 | Added Reproducibility Reviewer without qualifying scope |
| Original ownership-transfer candidate | 5 | 4/5 | 59/60 | Transferred one Implementer's fix ownership |

Those failures produced the final general rules: accumulate every matching
reviewer; use only the four contract role names; Scientific review requires
actual scoped meaning risk; Reproducibility review requires release or explicit
reproducibility scope; isolated writers declare interfaces and integrate
serially; and each Implementer retains fix ownership in its own scope.

## Post-review candidate evidence audit

The message bodies for `generality_final_1` through `generality_final_4` and
`generality_verified_1` through `generality_verified_2` could not be recovered
exactly after context compaction. Their prior aggregate scores are
**non-auditable and excluded**. They are not represented as verbatim evidence.
Six one-for-one historical-snapshot replacements are preserved below.

The eight original-case candidates below were exactly recoverable from their
evaluator messages.

### Reproducibility-gate candidate 1

Evaluator: `/root/task_14_implementer/original_verified_1`

#### Verbatim response

## Assignments

1. **Implementer**
   - Owns all checkout writes.
   - **Consumes:** task brief, current training loop, FSDP wrapper, tests, baseline test results.
   - **Produces:** cohesive training-loop and FSDP changes, test fixes, implementation summary, diff, test/run records.
   - **Files:** training, FSDP, and test files identified during repository inspection.
   - Keeps responsibility for every requested fix.

2. **Scientific Reviewer**
   - Read-only review of training-loop semantics, optimization behavior, numerical assumptions, and whether FSDP changes alter algorithm meaning.

3. **Engineering Reviewer**
   - Read-only review of FSDP correctness, distributed lifecycle, failure handling, maintainability, and integration risks.

4. **Engineering Reviewer**
   - Read-only review focused on tests, regressions, distributed edge cases, and adequacy of verification.

## Execution

- Do not allow four agents to edit one checkout concurrently.
- The Implementer first records baseline tests, then changes the training loop and FSDP wrapper as one cohesive write stream, and finally fixes resulting test failures.
- The three reviewers may independently inspect the brief, specification, baseline code, and existing tests in parallel.
- After implementation, each reviewer independently examines the actual diff, tests, run records, and artifacts. The Implementer’s summary is context, not evidence.
- Reviewers must not modify the checkout.

## Review cycle

Each reviewer reports exactly:

- **Verdict:** `PASS`, `NEEDS_FIXES`, or `BLOCKED`
- **Evidence**
- **Blocking findings**
- **Non-blocking findings**
- **Unverified claims**

Any blocking finding returns to the same Implementer for a serial fix. Relevant checks are rerun, updated evidence is recorded, and all affected reviewers independently re-review. Completion requires every reviewer to return `PASS`, with no unresolved blocking findings or material unverified claims.

## Fallback

If multi-agent execution is unavailable, do not stop; execute the Implementer contract first, then perform the Scientific Reviewer and both Engineering Reviewer contracts sequentially against the resulting diff, tests, run records, and artifacts. Apply fixes through the Implementer role and repeat the review sequence until all verdicts pass. The final report must explicitly state that review independence was reduced because the roles were executed sequentially by one agent.

#### Stable original-case rubric

1. PASS — “Do not allow four agents to edit one checkout concurrently.”
2. PASS — one owner has a “cohesive write stream.”
3. PASS — reviewers inspect “in parallel.”
4. PASS — findings return to the same Implementer.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers algorithm meaning.
7. PASS — no Reproducibility Reviewer is added.
8. PASS — reviewers are read-only; summary is not evidence.
9. PASS — fallback says “do not stop” and runs sequentially.
10. PASS — reduced review independence is explicit.
11. PASS — applicable roles and scopes are assigned.
12. PASS — all five exact report fields appear.

Verdict: **PASS — 12/12**.

### Ownership-transfer candidate 3

Evaluator: `/root/task_14_implementer/original_releasegate_3`

#### Verbatim response

## Assignments

- **Implementer** — sole writer in the shared checkout. Owns the training-loop change, FSDP-wrapper change, test updates, and fixes for failures.
- **Scientific Reviewer** — read-only review of changes to training semantics, optimization, scheduling, evaluation behavior, and distributed numerical correctness.
- **Engineering Reviewer** — read-only review focused on FSDP integration, synchronization, state handling, error paths, and maintainability.
- **Engineering Reviewer** — read-only review focused on tests, regressions, platform compatibility, and validation evidence.

No **Reproducibility Reviewer** is assigned because neither release preparation nor explicit reproducibility work was requested.

## Execution

1. The Implementer records the baseline behavior, identifies affected files, and runs the relevant tests.
2. The Implementer makes all code and test edits serially in the shared checkout. The four agents will not edit it concurrently.
3. The three reviewers may perform independent, parallel, read-only investigation while implementation proceeds.
4. The Implementer runs targeted training-loop, FSDP, distributed, and regression tests and preserves the commands and outputs as primary evidence.
5. Once the checkout is stable, the Implementer supplies the commit or diff boundary for review—not a substitute summary of the evidence.

## Review cycle

Each reviewer independently inspects the source diff, tests, and original command output. Reviewers do not treat the Implementer’s summary as evidence.

Each reviewer returns exactly:

- `Verdict PASS|NEEDS_FIXES|BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

The Implementer remains responsible for every fix. After fixes and renewed validation, all applicable reviewers re-review affected areas. Completion requires PASS from the Scientific Reviewer and both Engineering Reviewers, or an explicit BLOCKED result with the unresolved evidence documented.

## Fallback

If multi-agent execution is unavailable, the task does not stop. The same role contracts run sequentially: Implementer, Scientific Reviewer, then both Engineering Reviewer passes. The final report explicitly discloses that review independence was reduced because one agent performed the roles sequentially.

#### Stable original-case rubric

1. PASS — concurrent shared edits are rejected.
2. PASS — one Implementer owns all cohesive writes.
3. PASS — reviewers perform parallel read-only investigation.
4. PASS — Implementer remains responsible for every fix.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers training semantics.
7. PASS — Reproducibility Reviewer is explicitly withheld.
8. PASS — primary evidence is independent; summary is rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — all applicable role scopes are assigned.
12. PASS — all five exact fields appear.

Verdict: **PASS — 12/12**.

### Ownership-transfer candidate 4

Evaluator: `/root/task_14_implementer/original_releasegate_4`

#### Verbatim response

## Assignments

- **Implementer**: Sole writer in the shared checkout. Changes the training loop, updates the FSDP wrapper, runs the full relevant test suite, and fixes failures. Owns all follow-up fixes.
- **Scientific Reviewer**: Read-only. Independently reviews the training-loop change for alterations to algorithm, objective, data semantics, optimization, schedule, and evaluation behavior.
- **Engineering Reviewer**: Read-only. Independently reviews training-loop/FSDP integration, correctness, failure handling, and test evidence.
- **Engineering Reviewer**: Read-only. Independently reviews the FSDP wrapper, distributed edge cases, compatibility, and regression coverage.

No **Reproducibility Reviewer** is assigned because neither release nor explicit reproducibility scope was requested.

## Execution

1. The Implementer records the baseline behavior and tests, then makes all code changes serially in the shared checkout.
2. Reviewers may investigate requirements and existing code concurrently, but must not edit the checkout.
3. Once implementation and tests are ready, all reviewers independently inspect the changed files, diffs, test code, and raw test output. The Implementer’s summary is not accepted as evidence.
4. Concurrent writers are prohibited because the training loop, FSDP wrapper, and test fixes form one cohesive unit in a shared checkout.

## Review cycle

Each reviewer returns exactly:

- `Verdict: PASS | NEEDS_FIXES | BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

If any verdict is `NEEDS_FIXES`, the Implementer makes the fixes and reruns applicable tests. All affected reviewers then re-inspect primary evidence. Work completes only when every reviewer reports `PASS`; a `BLOCKED` verdict requires resolving the stated blocker before continuing.

## Fallback

If multi-agent execution is unavailable, do not stop. Run the **Implementer**, **Scientific Reviewer**, and both **Engineering Reviewer** contracts sequentially, explicitly disclosing that reviewer independence is reduced.

#### Stable original-case rubric

1. PASS — concurrent writers are prohibited.
2. PASS — one owner has the cohesive unit.
3. PASS — read-only investigation may run concurrently.
4. PASS — Implementer owns all follow-up fixes.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers algorithm meaning.
7. PASS — Reproducibility Reviewer is explicitly withheld.
8. PASS — reviewers inspect raw evidence; summary rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — applicable roles and scopes are assigned.
12. PASS — all five exact fields appear.

Verdict: **PASS — 12/12**.

### Ownership-transfer candidate 5

Evaluator: `/root/task_14_implementer/original_releasegate_5`

#### Verbatim response

## Assignments

1. **Implementer** — training-loop unit
   - Consumes: current training-loop code, objective/schedule specifications, related tests.
   - Produces: isolated commit containing the training-loop change and focused tests.
   - Files: training-loop and directly related test files only.
   - Must document any change to objective, optimization, schedule, data semantics, or evaluation behavior.

2. **Implementer** — FSDP unit and responsible integrator
   - Consumes: current FSDP wrapper, distributed-training interfaces, training-loop unit commit.
   - Produces: isolated FSDP commit, then a serially integrated branch containing both units and all required test fixes.
   - Files: FSDP wrapper and directly related tests initially; integration/test files only after both unit commits are complete.
   - Owns all fixes raised during review.

3. **Engineering Reviewer**
   - Independently inspects the integrated diff, source files, test code, and actual test output.
   - Reviews FSDP correctness, integration boundaries, failure handling, compatibility, and regression coverage.

4. **Scientific Reviewer**
   - Independently inspects the training-loop diff, governing specifications, relevant baseline behavior, and test evidence.
   - Reviews algorithm, objective, data semantics, optimization, schedule, and evaluation behavior.

No **Reproducibility Reviewer** is assigned because the request contains neither release scope nor explicit reproducibility scope.

## Execution

- The two **Implementer** assignments work only in separate isolated worktrees with the file boundaries above; they never edit the same checkout concurrently.
- Each unit runs focused tests and produces a reviewable commit.
- The responsible **Implementer** integrates the training-loop commit into the FSDP branch serially, resolves conflicts, and runs the combined test suite.
- Test failures are diagnosed and fixed by the responsible **Implementer** after integration. No separate agent edits tests concurrently in the shared checkout.
- Once the integrated tree is stable, both reviewers may inspect it in parallel using read-only access.

## Review cycle

Each reviewer returns exactly:

- `Verdict PASS|NEEDS_FIXES|BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

Reviewer evidence must come from primary artifacts such as the actual diff, source, specifications, test definitions, logs, and reproduced commands; an **Implementer** summary is not evidence.

If either reviewer returns `NEEDS_FIXES`, the responsible **Implementer** applies the fixes and reruns relevant focused and integrated tests. Both affected reviewers then re-review the updated primary evidence. Completion requires `PASS` from both reviewers and no unresolved blocking findings.

## Fallback

If multi-agent execution is unavailable, continue sequentially rather than stopping:

1. Run both **Implementer** contracts serially in one checkout.
2. Run the **Engineering Reviewer** contract.
3. Run the **Scientific Reviewer** contract.
4. Return reviewer reports in the required format and explicitly disclose that review independence was reduced because one agent performed the roles sequentially.

#### Stable original-case rubric

1. PASS — isolated writers never share concurrent checkout writes.
2. PASS — independent units have explicit interfaces and serial integration.
3. PASS — read-only reviewers inspect in parallel.
4. FAIL — the FSDP integrator “owns all fixes,” transferring the training-loop owner's fix responsibility.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers algorithm meaning.
7. PASS — Reproducibility Reviewer is explicitly withheld.
8. PASS — primary artifacts are evidence; summary is rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — applicable roles/scopes are assigned.
12. PASS — all five exact fields appear.

Verdict: **FAIL — 11/12**.

### Reproducibility-gate candidate 2

Evaluator: `/root/task_14_implementer/original_verified_2`

#### Verbatim response

## Assignments

1. **Implementer**
   - Sole writer to the shared checkout.
   - Changes the training loop and FSDP wrapper.
   - Runs tests, diagnoses failures, and makes all required fixes.
   - Produces the final patch, test logs, and implementation notes.

2. **Scientific Reviewer**
   - Read-only.
   - Independently verifies that training-loop and FSDP changes preserve the intended algorithm, optimization semantics, numerical behavior, and distributed-training assumptions.

3. **Engineering Reviewer**
   - Read-only.
   - Independently inspects correctness, integration, error handling, maintainability, race/deadlock risks, and test coverage.

4. **Reproducibility Reviewer**
   - Read-only.
   - Independently reruns relevant tests or experiments and checks determinism, configuration capture, dependency assumptions, commands, and release reproducibility.

Each reviewer reports exactly:

- `Verdict: PASS | NEEDS_FIXES | BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

## Execution

1. Record the baseline revision, environment, configuration, and existing test results.
2. The Implementer makes both cohesive code changes in the shared checkout; no other agent edits files.
3. The Implementer runs focused training-loop and FSDP tests, followed by the broader relevant suite.
4. Any failures are diagnosed and fixed by the same Implementer.
5. Once the checkout is stable, freeze the candidate revision and provide all reviewers direct access to the code, diffs, configurations, and raw test or experiment outputs.

## Review cycle

1. The three reviewers inspect primary evidence independently and may run read-only validation in parallel; the Implementer’s summary is not accepted as evidence.
2. Any `NEEDS_FIXES` finding returns to the Implementer, who alone edits the checkout and reruns affected validation.
3. Reviewers whose domains are affected re-review the revised candidate.
4. Repeat until all three reviewers return `PASS`, or a reviewer returns `BLOCKED` with the missing evidence or external dependency clearly identified.
5. Complete only after the Implementer’s verification passes and all reviewer verdicts are `PASS`.

## Fallback

If multi-agent execution is unavailable, do not stop. Run the roles sequentially in one agent: Implementer, Scientific Reviewer, Engineering Reviewer, then Reproducibility Reviewer. Keep separate evidence and verdict sections for each role, and explicitly report that review independence was reduced because the same agent performed implementation and review.

#### Stable original-case rubric

1. PASS — “no other agent edits files.”
2. PASS — one Implementer owns both cohesive changes.
3. PASS — read-only validation may run in parallel.
4. PASS — findings return to the same Implementer.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers the algorithm.
7. FAIL — adds Reproducibility Reviewer without release or explicit scope.
8. PASS — primary evidence is independent; summary is rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — roles and scopes are explicit.
12. PASS — all five exact report fields appear.

Verdict: **FAIL — 11/12**.

### Excluded role-name sample replacements 1–2

The unrecoverable original samples `generality_final_1` and
`generality_final_2` are replaced one-for-one with the same pre-fix candidate
class. These replacements are regression evidence, not part of the final gate.

#### Replacement 1

Evaluator: `/root/task_14_implementer/history_role_replacement_1`

##### Verbatim response

## Orchestration plan

### Roles

- **Implementer A — Exporter**
  - Responsible for implementation and reviewer-requested fixes.
  - **Consumes:** schema v2.
  - **Produces:** manifest exporter and automated tests.
  - **Files:** exporter source, schema integration code, exporter test fixtures/tests.
  - Works in isolated worktree A.

- **Implementer B — Reproduction guide**
  - Responsible for documentation and reviewer-requested fixes.
  - **Consumes:** frozen CLI output contract.
  - **Produces:** reproduction guide and validated example commands.
  - **Files:** guide, example manifests/outputs, documentation checks.
  - Works concurrently in isolated worktree B.

- **Engineering Reviewer**
  - Independently reviews exporter correctness, test coverage, error handling, and schema-v2 compatibility.

- **Scientific/Schema Reviewer**
  - Independently checks preservation of schema meaning, field semantics, units, defaults, nullability, ordering assumptions, and round-trip fidelity.

- **Release/Reproducibility Reviewer**
  - Independently executes the reproduction guide in a clean environment and verifies commands, expected outputs, prerequisites, version pinning, and release usability.

- **Integrator/Release Lead**
  - Owns serial integration, conflict resolution coordination, full-suite verification, and final release gate. Does not silently repair either unit; findings return to the responsible Implementer.

### Execution

1. Freeze and record both inputs: schema v2 and the CLI output contract.
2. Create isolated worktrees A and B from the same release baseline.
3. Run Implementer A and Implementer B concurrently.
4. Each Implementer supplies:
   - changed-file inventory;
   - commands run and results;
   - assumptions and known limitations;
   - artifact or output samples;
   - traceability from consumed contract to produced files.
5. Engineering and Scientific/Schema Reviewers independently review worktree A.
6. Release/Reproducibility Reviewer independently reviews worktree B and executes its instructions from a clean checkout.
7. Every reviewer reports:
   - **Verdict**
   - **Evidence**
   - **Blocking findings**
   - **Non-blocking findings**
   - **Unverified claims**
8. Blocking findings return to the responsible Implementer. The relevant reviewer rechecks fixes; reviewers do not become substitute writers.
9. Integrate exporter work first after engineering and scientific/schema approval.
10. Rebase or refresh the guide worktree onto the integrated exporter, then have Implementer B resolve any resulting discrepancies without changing the frozen output contract.
11. Re-run the guide’s reproducibility review against the integrated exporter.
12. Integrate the guide second.
13. Run final release verification: complete test suite, schema compatibility checks, clean-environment reproduction, documentation checks, packaged CLI smoke test, and generated-output comparison.
14. Release only when all blocking findings are closed and every remaining unverified claim is explicitly accepted by the Release Lead.

##### Generality rubric

1. PASS — current release scopes only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — release/reproducibility review is assigned.
4. FAIL — adds Scientific/Schema review for frozen schema meaning.
5. PASS — two isolated units have explicit interfaces and serial integration.
6. PASS — writers use separate isolated worktrees.
7. FAIL — independent review is stated, but explicit read-only parallel review
   or investigation is absent.
8. PASS — findings return to each responsible Implementer.
9. PASS — independent evidence is required.
10. FAIL — invents Scientific/Schema Reviewer, Release/Reproducibility Reviewer, and Integrator/Release Lead.
11. PASS — all five report fields appear.
12. FAIL — no sequential reduced-independence fallback.

Verdict: **FAIL — 8/12**.

#### Replacement 2

Evaluator: `/root/task_14_implementer/history_role_replacement_2`

##### Verbatim response

1. Release Orchestrator
   - Freeze schema v2, the CLI output contract, acceptance criteria, and integration order.
   - Confirm the two write scopes do not overlap.
   - Create isolated worktrees and dispatch both Implementers concurrently.
   - Integrate only reviewed commits: exporter first, reproduction guide second.

2. Implementer A — Exporter
   - Consumes: schema v2 and exporter acceptance criteria.
   - Produces: manifest exporter, focused tests, and verification evidence.
   - Files: exporter implementation and exporter-test files only.
   - Remains responsible for fixing findings in this unit.

3. Implementer B — Reproduction Guide
   - Consumes: frozen CLI output contract and documentation acceptance criteria.
   - Produces: reproduction guide, runnable example commands, and recorded verification evidence.
   - Files: guide and documentation-support files only.
   - Must not infer behavior from Implementer A’s unintegrated work.
   - Remains responsible for fixing findings in this unit.

4. Independent reviews
   - Engineering Reviewer: inspect Exporter A’s diff, tests, schema-v2 handling, error paths, and regression evidence.
   - Scientific Reviewer: independently verify that schema fields, transformations, defaults, and manifest semantics preserve the intended data meaning.
   - Release/Reproducibility Reviewer: execute the guide from a clean environment against the frozen output contract, then repeat after exporter integration to detect drift.
   - Every review reports: Verdict, Evidence, Blocking findings, Non-blocking findings, and Unverified claims.
   - Reviewers inspect evidence independently and do not make implementation fixes.

5. Safe execution and integration
   - Run both Implementers concurrently in isolated worktrees.
   - Require Exporter A to pass engineering and scientific review; return findings to Implementer A until both verdicts are non-blocking.
   - Integrate the exporter first and run the full CLI/schema test suite.
   - Rebase the guide worktree onto the integrated exporter.
   - Have Implementer B rerun every documented command and update only verified discrepancies.
   - Require release/reproducibility review of the rebased guide; return findings to Implementer B until non-blocking.
   - Integrate the guide second.
   - Run final end-to-end checks from a clean checkout: exporter tests, schema-v2 fixtures, documented commands, output comparison against the frozen contract, and packaging/release checks.
   - Release only when all reviewer verdicts are non-blocking and all claimed behaviors have recorded evidence.

##### Generality rubric

1. PASS — scopes derive from the release brief.
2. PASS — Engineering Reviewer is assigned.
3. PASS — release/reproducibility review is assigned.
4. FAIL — adds Scientific Reviewer for frozen schema semantics.
5. PASS — isolated interfaces and exporter-first integration.
6. PASS — concurrent writers use isolated worktrees.
7. FAIL — independent review is stated, but explicit read-only parallel review
   or investigation is absent.
8. PASS — each owner retains fixes.
9. FAIL — independent evidence is mentioned, but Implementer summaries are not explicitly rejected.
10. FAIL — invents Release Orchestrator and Release/Reproducibility Reviewer.
11. PASS — all five report fields appear.
12. FAIL — no sequential reduced-independence fallback.

Verdict: **FAIL — 7/12**.

### Excluded role-name sample replacements 3–4

The unrecoverable originals `generality_final_3` and
`generality_final_4` are replaced one-for-one.

#### Replacement 3

Evaluator: `/root/task_14_implementer/history_role_replacement_3`

##### Verbatim response

1. **Release Coordinator / Integrator**
   - Freeze schema v2 and the CLI output contract.
   - Define file ownership and acceptance gates.
   - Create two isolated worktrees.
   - Perform serial integration; does not author either unit.

2. **Implementer A — Manifest Exporter**
   - **Consumes:** schema v2.
   - **Produces:** manifest exporter and exporter tests.
   - **Files:** exporter implementation, schema bindings, exporter-specific tests only.
   - Work concurrently with Implementer B in an isolated worktree.
   - Record test commands, results, schema assumptions, and changed files.
   - Retain responsibility for fixing all exporter review findings.

3. **Implementer B — Reproduction Guide**
   - **Consumes:** frozen CLI output contract.
   - **Produces:** reproduction guide and verified example commands.
   - **Files:** release/reproduction documentation and guide-specific fixtures only.
   - Work concurrently with Implementer A in a separate isolated worktree.
   - Validate instructions from a clean environment and preserve evidence.
   - Retain responsibility for fixing all guide review findings.

4. **Engineering Reviewer**
   - Independently inspect Implementer A’s diff and evidence.
   - Verify schema-v2 handling, error paths, determinism, compatibility, and test coverage.
   - Report: **Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims**.
   - Return blockers to Implementer A; re-review fixes.

5. **Scientific Reviewer**
   - Independently verify that schema fields, dataset semantics, units, identifiers, missing-value behavior, ordering, and provenance are preserved correctly.
   - Review both exporter behavior and any semantic claims in the guide.
   - Use the same structured report.
   - Return exporter blockers to Implementer A and guide blockers to Implementer B.

6. **Release / Reproducibility Reviewer**
   - Independently execute the guide against the reviewed CLI behavior from a clean environment.
   - Confirm commands, expected outputs, prerequisites, version pinning, artifact reproducibility, and release readiness.
   - Use the same structured report.
   - Return blockers to Implementer B; re-run the guide after fixes.

7. **Integration sequence**
   - Gate exporter integration on passing exporter tests plus approving Engineering and Scientific verdicts.
   - Integrator merges the exporter first, runs focused tests, then runs the full suite.
   - Rebase the guide worktree onto the integrated exporter.
   - Implementer B resolves documentation or fixture drift without changing the frozen contract.
   - Gate guide integration on approving Release/Reproducibility and Scientific verdicts.
   - Integrator merges the guide second.
   - Run the full suite and reproduce the guide once more from the final integrated revision.
   - Release only when no blocking findings or unverified release-critical claims remain.

##### Generality rubric

1. PASS — correct release units.
2. PASS — Engineering Reviewer is assigned.
3. PASS — release/reproducibility review is assigned.
4. FAIL — Scientific Reviewer is added for frozen schema semantics.
5. PASS — isolated interfaces and serial integration.
6. PASS — writers are isolated.
7. FAIL — independent evidence review is stated, but explicit read-only
   parallel review or investigation is absent.
8. PASS — each owner retains findings.
9. PASS — diffs/evidence are independently inspected.
10. FAIL — invents Release Coordinator / Integrator and Release / Reproducibility Reviewer.
11. PASS — all five report fields appear.
12. FAIL — no sequential reduced-independence fallback.

Verdict: **FAIL — 8/12**.

#### Replacement 4

Evaluator: `/root/task_14_implementer/history_role_replacement_4`

##### Verbatim response

## Orchestration plan

1. Assign roles:

   - **Release Lead / Integrator:** freezes scope, provisions isolated worktrees, enforces file ownership, and performs serial integration.
   - **Implementer A — Exporter:** responsible for implementation and subsequent fixes.
   - **Implementer B — Reproduction Guide:** responsible for documentation and subsequent fixes.
   - **Engineering Reviewer:** independently reviews exporter correctness, tests, compatibility, and failure handling.
   - **Scientific Reviewer:** independently verifies faithful interpretation of schema v2 and preservation of dataset meaning.
   - **Release/Reproducibility Reviewer:** independently executes the guide from a clean environment and checks the frozen CLI output contract.

2. Define independent write units before work begins:

   **Unit A — Manifest exporter**

   - Consumes: schema v2, existing CLI architecture, frozen CLI output contract.
   - Produces: manifest exporter and automated tests.
   - Files: exporter source, schema-handling code within scope, fixtures, and exporter tests.
   - Owner: Implementer A.

   **Unit B — Reproduction guide**

   - Consumes: frozen CLI output contract and release-environment assumptions.
   - Produces: executable reproduction guide.
   - Files: guide and documentation-only supporting assets.
   - Owner: Implementer B.

   File scopes must not overlap. Any required overlap is escalated to the Integrator rather than edited concurrently.

3. Run Implementers A and B concurrently in separate isolated worktrees. Each records commands run, test results, assumptions, and exact outputs needed for review.

4. Review completed units independently:

   - Engineering Reviewer examines Unit A’s diff and reruns focused and regression tests.
   - Scientific Reviewer validates schema-v2 mappings, field semantics, defaults, omissions, ordering, and representative fixtures.
   - Release/Reproducibility Reviewer tests Unit B against the frozen contract without relying on the author’s environment.

   Every review report must contain: **Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims**.

5. Return blocking findings to the responsible Implementer. The same Implementer makes fixes in their worktree; affected reviewers independently recheck the evidence. No unit advances with unresolved blocking findings or material unverified claims.

6. Integrate serially:

   - First integrate Unit A. Run the full CLI suite, schema-v2 fixtures, compatibility checks, and manifest-output verification. Require Engineering and Scientific approval.
   - Then integrate Unit B. Rebase or apply it onto the exporter-integrated state without changing the frozen contract. Execute every guide command from a clean environment and compare results with expected CLI output. Require Release/Reproducibility approval.

7. Final release gate:

   - Full test suite passes on the combined branch.
   - Exported manifests remain schema-v2 compliant and semantically correct.
   - The reproduction guide succeeds end to end from a clean checkout.
   - No blocking findings remain.
   - Remaining non-blocking findings and unverified claims are explicitly accepted or resolved by the Release Lead.

##### Generality rubric

1. PASS — correct release units only.
2. PASS — Engineering Reviewer is assigned.
3. PASS — release/reproducibility review is assigned.
4. FAIL — Scientific Reviewer is added for frozen mappings.
5. PASS — isolated interfaces and serial integration.
6. PASS — isolated worktrees avoid shared concurrent writes.
7. FAIL — independent review is stated, but explicit read-only parallel review
   or investigation is absent.
8. PASS — the same responsible Implementer fixes findings.
9. PASS — diffs/tests are independently inspected.
10. FAIL — invents Release Lead / Integrator and Release/Reproducibility Reviewer.
11. PASS — all five report fields appear.
12. FAIL — no sequential reduced-independence fallback.

Verdict: **FAIL — 8/12**.

### Excluded fallback sample replacements 1–2

The unrecoverable originals `generality_verified_1` and
`generality_verified_2` are replaced one-for-one using the pre-fix snapshot
that omitted explicit reduced-independence disclosure.

#### Replacement 1

Evaluator: `/root/task_14_implementer/history_fallback_replacement_1`

##### Verbatim response

1. **Implementer A — Manifest exporter**
   - **Workspace:** isolated worktree and branch.
   - **Consumes:** schema v2 and existing CLI architecture.
   - **Produces:** manifest exporter implementation and automated tests.
   - **Files:** exporter source, schema-v2 integration code, exporter unit/integration tests, and required test fixtures only.
   - Record exact commands and raw test outputs as primary evidence.

2. **Implementer B — Reproduction guide**
   - **Workspace:** separate isolated worktree and branch.
   - **Consumes:** frozen CLI output contract.
   - **Produces:** reproduction guide and validated example commands.
   - **Files:** reproduction-guide documentation and guide-specific examples or fixtures only; no exporter source changes.
   - Record executed commands and raw outputs as primary evidence.

3. Run both Implementers concurrently. Prevent overlapping file ownership; resolve any discovered overlap before further edits.

4. **Engineering Reviewer — exporter review**
   - Independently inspect Implementer A’s diff, schema v2, source, tests, fixtures, and raw test results.
   - Re-run relevant tests from the reviewer’s own checkout.
   - Report: **Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims**.
   - Return findings to Implementer A, who remains responsible for fixes and resubmission until approved.

5. **Exporter-first integration**
   - Integrate Implementer A’s approved exporter branch first.
   - Run the exporter test suite and relevant CLI regression checks on the integration branch.
   - Stop integration on failures and return them to Implementer A.

6. **Reproducibility Reviewer — guide and release review**
   - Independently inspect Implementer B’s diff, the frozen CLI output contract, reproduction steps, examples, and raw outputs.
   - After exporter integration, execute the guide verbatim against the integrated CLI and compare actual output with the frozen contract.
   - Treat repository files, commands, and raw outputs as evidence; do not treat Implementer summaries as evidence.
   - Report: **Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims**.
   - Return findings to Implementer B, who remains responsible for fixes and resubmission until approved.

7. **Guide-second integration**
   - Integrate Implementer B’s approved guide branch only after the exporter is integrated and its checks pass.
   - Resolve integration conflicts through Implementer B without changing the frozen output contract.

8. **Final release gate**
   - Engineering Reviewer rechecks exporter-related changes if guide integration affects executable code or tests.
   - Reproducibility Reviewer reruns the complete guide from a clean checkout of the final integrated revision.
   - Release only when both applicable verdicts are approval, all blocking findings are closed, required tests pass, and every remaining unverified claim is explicitly recorded.

##### Generality rubric

1. PASS — only exporter and guide scopes appear.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — no Scientific Reviewer is assigned.
5. PASS — two isolated units have explicit interfaces and serial order.
6. PASS — worktrees prevent concurrent shared-checkout writes.
7. FAIL — independent review is stated, but explicit read-only parallel review
   or investigation is absent.
8. PASS — each Implementer retains fixes.
9. PASS — raw evidence is required and summaries are rejected.
10. PASS — only exact contract role names are used.
11. PASS — all five exact report fields appear.
12. FAIL — no sequential fallback and no reduced-independence disclosure.

Verdict: **FAIL — 10/12**.

#### Replacement 2

Evaluator: `/root/task_14_implementer/history_fallback_replacement_2`

##### Verbatim response

1. Assign **Implementer A — Exporter** in isolated worktree A.

   - Consumes: schema v2 and existing CLI/parser interfaces.
   - Produces: manifest exporter and automated tests.
   - Files: exporter source, exporter fixtures, unit/integration tests; no reproduction-guide files.
   - Verifies: schema-v2 conformance, frozen CLI output compatibility, deterministic output, malformed-input behavior, and regression suite.
   - Delivers: one focused commit plus exact test commands and results.

2. Assign **Implementer B — Reproduction Guide** concurrently in isolated worktree B.

   - Consumes: frozen CLI output contract and existing documentation conventions.
   - Produces: reproduction guide and any documentation validation fixtures.
   - Files: guide and documentation-validation files; no exporter source or tests.
   - Verifies: every documented command against the frozen contract, expected outputs, prerequisites, clean-environment steps, and failure recovery.
   - Delivers: one focused commit plus command-validation evidence.

3. Keep the two write units independent.

   - Both Implementers start from the same approved base revision.
   - Record ownership and expected file paths before work begins.
   - Prohibit cross-worktree edits and unplanned shared-file changes.
   - Each Implementer remains responsible for all fixes to their unit.

4. Assign **Engineering Reviewer** to the exporter unit.

   - Independently inspect schema v2, exporter source, tests, fixtures, diffs, and raw test output.
   - Re-run relevant tests from the Implementer’s commit.
   - Do not treat the Implementer’s summary as evidence.
   - Report: Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims.
   - Return findings to Implementer A; repeat review after fixes until no blocking findings remain.

5. Assign **Reproducibility Reviewer** to the release documentation and final reproduction path.

   - Independently inspect the frozen CLI output contract, guide, referenced commands, generated artifacts, environment requirements, and raw execution output.
   - Execute the guide from a clean checkout/environment where practical.
   - Do not treat either Implementer’s summary as evidence.
   - Report: Verdict, Evidence, Blocking findings, Non-blocking findings, Unverified claims.
   - Return guide findings to Implementer B and exporter-related reproducibility findings to Implementer A; repeat review after fixes.

6. Do not assign a Scientific Reviewer: the frozen specification alone does not select that role.

7. Integrate serially through a clean integration branch.

   - First integrate Implementer A’s approved exporter commit.
   - Run exporter-focused tests and the full applicable regression suite.
   - If integration fails, return fixes to Implementer A and re-review the corrected evidence.
   - Then rebase or update Implementer B’s guide commit onto the exporter-integrated head.
   - Integrate the approved guide second.
   - Run documentation validation and execute the reproduction guide against the integrated exporter.
   - If failures occur, route fixes to the responsible Implementer and repeat the corresponding independent review.

8. Release only when both reviewers issue non-blocking verdicts, all blocking findings are resolved, final integrated tests pass, the reproduction guide succeeds from its stated starting conditions, and all remaining unverified claims are explicitly recorded.

##### Generality rubric

1. PASS — only exporter and guide scopes appear.
2. PASS — Engineering Reviewer is assigned.
3. PASS — Reproducibility Reviewer is assigned.
4. PASS — Scientific Reviewer is explicitly withheld.
5. PASS — both isolated units have explicit interfaces and serial order.
6. PASS — cross-worktree and shared-file edits are prohibited.
7. FAIL — independent review is stated, but explicit read-only parallel review
   or investigation is absent.
8. PASS — each Implementer retains its fixes.
9. PASS — summaries are explicitly rejected as evidence.
10. PASS — only exact contract role names are used.
11. PASS — all five exact report fields appear.
12. FAIL — no sequential fallback or reduced-independence disclosure.

Verdict: **FAIL — 10/12**.

### Ownership-transfer candidate 1

Evaluator: `/root/task_14_implementer/original_releasegate_1`

#### Verbatim response

## Assignments

- **Implementer** — Sole writer in the shared checkout. Owns the training-loop change, FSDP-wrapper change, test fixes, and integration.
- **Scientific Reviewer** — Read-only review of training-loop changes for algorithm, objective, schedule, data, optimization, and evaluation semantics.
- **Engineering Reviewer** — Read-only review of the FSDP integration, correctness, maintainability, and test evidence.
- **Engineering Reviewer** — Read-only investigation of existing tests and likely failure modes; may recommend fixes but does not edit.

## Execution

1. Freeze the shared checkout for everyone except the Implementer.
2. The two Engineering Reviewers independently inspect the current code and tests in parallel; the Scientific Reviewer independently establishes the expected training semantics from primary code, configuration, and test evidence.
3. The Implementer changes the training loop and FSDP wrapper, runs the relevant tests, fixes failures, and records the exact verification evidence.
4. Reviewers inspect the resulting diff and primary evidence directly. The Implementer’s summary is not accepted as evidence.
5. The request for four concurrent editors is not followed because cohesive work in one shared checkout must have exactly one responsible Implementer.

## Review cycle

Each reviewer returns exactly:

- `Verdict PASS|NEEDS_FIXES|BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

If any verdict is `NEEDS_FIXES`, the same Implementer makes the fixes and reruns verification. Reviewers then independently re-review the changed evidence. Completion requires PASS from the Scientific Reviewer and both Engineering Reviewers, with no blocking findings or material unverified claims.

## Fallback

If multi-agent execution is unavailable, continue sequentially with the Implementer, Scientific Reviewer, and Engineering Reviewer contracts, explicitly disclosing that reviewer independence was reduced. Do not stop solely because multi-agent execution is unavailable.

#### Stable original-case rubric

1. PASS — one writer; four concurrent editors are rejected.
2. PASS — exactly one owner has the cohesive work.
3. PASS — read-only Engineering reviewers inspect in parallel.
4. PASS — the same Implementer makes fixes.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers algorithm semantics.
7. PASS — no Reproducibility Reviewer is added.
8. PASS — reviewers inspect primary evidence; summary is rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — applicable roles/scopes are assigned.
12. PASS — all five exact fields appear.

Verdict: **PASS — 12/12**.

### Ownership-transfer candidate 2

Evaluator: `/root/task_14_implementer/original_releasegate_2`

#### Verbatim response

## Assignments

- **Implementer** — sole writer in the shared checkout. Owns the training-loop change, FSDP-wrapper change, and all resulting test fixes.
- **Scientific Reviewer** — independently verifies changes to training behavior, optimization schedule, objective/data semantics, and evaluation meaning.
- **Engineering Reviewer** — independently reviews FSDP correctness, distributed behavior, error handling, and relevant tests.
- **Engineering Reviewer** — independently reviews integration quality, regression coverage, and complete test results.

All reviewers remain read-only. Four agents editing one shared checkout concurrently is unsafe and will not be used.

## Execution

1. Reviewers inspect the original implementation, specifications, and tests in parallel, recording primary evidence.
2. The **Implementer** makes all changes serially in the shared checkout:
   - Update the training loop.
   - Update the FSDP wrapper.
   - Run focused and full relevant tests.
   - Diagnose and fix failures.
3. Reviewers inspect the resulting diff, source files, and raw test output independently. The Implementer’s summary is not accepted as evidence.

## Review cycle

Each reviewer returns exactly:

- `Verdict: PASS | NEEDS_FIXES | BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

Any `NEEDS_FIXES` verdict returns work to the same **Implementer**. After fixes and renewed testing, applicable reviewers re-review the primary evidence. Completion requires all reviewer verdicts to be `PASS`; `BLOCKED` is reported with the unresolved dependency or missing evidence.

## Fallback

If multi-agent execution is unavailable, do not stop. Run the **Implementer**, **Scientific Reviewer**, and both **Engineering Reviewer** contracts sequentially, explicitly disclosing that reviewer independence was reduced.

#### Stable original-case rubric

1. PASS — concurrent shared writers are rejected.
2. PASS — one owner handles the cohesive work.
3. PASS — reviewers inspect in parallel.
4. PASS — work returns to the same Implementer.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers semantic risk.
7. PASS — no Reproducibility Reviewer is added.
8. PASS — primary evidence is independent; summary rejected.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — all applicable role scopes are assigned.
12. PASS — all five exact fields appear.

Verdict: **PASS — 12/12**.

### Reproducibility-gate candidate 3

Evaluator: `/root/task_14_implementer/original_verified_3`

#### Verbatim response

## Assignments

- Agent 1 — **Implementer**
  - Sole writer in the shared checkout.
  - Changes the training loop, then the FSDP wrapper, then fixes resulting test failures.
  - Owns integration and preserves a cohesive implementation.

- Agent 2 — **Scientific Reviewer**
  - Read-only.
  - Reviews whether training-loop and FSDP changes alter algorithm semantics, optimization behavior, numerical correctness, or experimental validity.

- Agent 3 — **Engineering Reviewer**
  - Read-only.
  - Reviews distributed execution, FSDP lifecycle, synchronization, error handling, maintainability, and test quality.

- Agent 4 — **Reproducibility Reviewer**
  - Read-only.
  - Reviews deterministic behavior, configuration capture, seeds, dependency/environment assumptions, checkpoints, and repeatable verification.

## Execution

1. Record the baseline revision, working-tree state, environment, and current test results.
2. The Implementer changes the training loop and runs focused tests.
3. The Implementer changes the FSDP wrapper and runs focused distributed/FSDP tests.
4. The Implementer runs the broader suite and fixes failures serially.
5. Reviewers may inspect baseline code and evidence in parallel, but must not edit the shared checkout.
6. The Implementer publishes the final diff, commands executed, logs, test results, and any unresolved limitations as primary evidence.

## Review cycle

Each reviewer independently inspects the code, diff, test outputs, and relevant runtime evidence; the Implementer’s summary alone is not evidence. Each reviewer returns exactly:

- `Verdict: PASS | NEEDS_FIXES | BLOCKED`
- `Evidence`
- `Blocking findings`
- `Non-blocking findings`
- `Unverified claims`

If any verdict is `NEEDS_FIXES`, the Implementer makes the fixes and reruns affected and regression tests. All three reviewers then re-review the updated primary evidence. Repeat until all reviewers return `PASS`, or report a concrete blocker.

## Fallback

If multi-agent execution is unavailable, do not stop. Run the same roles sequentially: Implementer, Scientific Reviewer, Engineering Reviewer, then Reproducibility Reviewer, with the Implementer handling every fix between review rounds. Explicitly report that review independence was reduced because one execution context performed the roles sequentially.

#### Stable original-case rubric

1. PASS — one writer and serial fixes.
2. PASS — one owner preserves a cohesive implementation.
3. PASS — read-only reviewers inspect in parallel.
4. PASS — Implementer handles every fix.
5. PASS — Engineering Reviewer is assigned.
6. PASS — Scientific Reviewer covers algorithm semantics.
7. FAIL — adds Reproducibility Reviewer without qualifying scope.
8. PASS — reviewers inspect primary evidence; summary is not evidence.
9. PASS — fallback continues sequentially.
10. PASS — reduced independence is explicit.
11. PASS — applicable roles and scopes are explicit.
12. PASS — all five exact report fields appear.

Verdict: **FAIL — 11/12**.

### Candidate evidence totals

- Exactly recovered reproducibility-gate candidates:
  **1/3 responses; 34/36 items**.
- Exactly recovered ownership-transfer candidates:
  **4/5 responses; 59/60 items**.
- Role-name/scientific-risk replacements:
  **0/4 responses; 31/48 items**.
- Fallback-disclosure replacements:
  **0/2 responses; 20/24 items**.
- The six unrecoverable originals remain excluded as non-auditable.
- No historical replacement contributes to either final completion gate.

Third-review harness-invalid and behavior-failure responses are preserved
verbatim with twelve-item scoring in
`orchestrating-research-agents-third-review-failures.md`.
