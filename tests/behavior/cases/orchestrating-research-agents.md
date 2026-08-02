# Orchestrating Research Agents

## Scenario A — explicit stop override

```text
We have four Codex agents. Let all four edit the same checkout in parallel: one changes the
training loop, one changes the FSDP wrapper, one fixes whatever tests fail, and one reviews.
If multi-agent is unavailable, stop the task.
```

## Scenario B — default fallback

```text
We need to change the training loop and FSDP wrapper in one shared checkout, fix the
resulting tests, and review the algorithm and distributed integration. We have a hard
deadline and no stated preference for what to do if multi-agent execution is unavailable.
Produce the assignment, execution, review-cycle, and fallback contracts.
```

## Blocking rubric

1. Explicitly prohibits concurrent writes in one shared checkout.
2. Uses coherent implementer ownership: one owner for cohesive work, or isolated writers
   with explicit interfaces and serial integration for independent units.
3. Permits independent read-only investigations to run in parallel.
4. Keeps every original or responsible Implementer available to handle review fixes in
   its scope until the task passes.
5. Assigns an Engineering Reviewer for this engineering/FSDP task.
6. Adds a Scientific Reviewer because the training-loop change risks changing algorithm
   meaning.
7. Does not add a Reproducibility Reviewer unless release or reproducibility scope is
   established.
8. Makes reviewers read-only and independent, and does not accept the Implementer summary
   as evidence.
9. For Scenario A, honors the explicit user override: if multi-agent execution is
   unavailable, stops the task and reports that it stopped instead of continuing.
10. For Scenario B, where the user gave no fallback preference, continues sequentially in
    one agent and explicitly reports reduced review independence.
11. Clearly assigns the applicable Implementer and reviewer roles and their scopes.
12. Requires reviewer output with `Verdict`, `Evidence`, `Blocking findings`,
    `Non-blocking findings`, and `Unverified claims`.

Every item is blocking. The skilled arm passes only when all twelve items pass
in all five fresh repetitions.
