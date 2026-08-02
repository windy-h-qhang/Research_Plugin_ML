# Orchestrating Research Agents: Generality

## Prompt

```text
We are preparing a release of a dataset-manifest CLI. One independent write unit consumes
schema v2 and produces the manifest exporter plus its tests. A second independent write unit
consumes the frozen CLI output contract and produces the reproduction guide. Each writer can
use an isolated worktree. To meet the release window, two responsible Implementers must execute
these independent units concurrently; integrate the exporter first and the guide second.
Multi-agent is available. Assign agent roles and a safe execution and review plan.
```

## Blocking rubric

1. Derives assignments from the current dataset-manifest release brief and does not introduce
   training-loop, FSDP, or unrelated generic test-fix scope.
2. Assigns an Engineering Reviewer for the CLI engineering work.
3. Assigns a Reproducibility Reviewer for the explicit release and reproduction scope.
4. Does not assign a Scientific Reviewer without algorithm-meaning or scientific-claim risk.
5. Uses coherent implementer ownership: one owner for cohesive work, or isolated writers with
   explicit interfaces and serial integration for independent units. Here it assigns the two
   required responsible Implementers to their independent isolated units.
6. Explicitly prohibits concurrent writes in one shared checkout.
7. Permits independent read-only investigations and reviews to run in parallel.
8. Keeps each original or responsible Implementer available for review fixes until pass.
9. Makes reviewers read-only and independent, and does not accept an Implementer summary as
   evidence.
10. Uses only the exact role names `Implementer`, `Scientific Reviewer`,
    `Engineering Reviewer`, and `Reproducibility Reviewer`, and clearly assigns every
    applicable role and its scope.
11. Requires reviewer output with `Verdict`, `Evidence`, `Blocking findings`,
    `Non-blocking findings`, and `Unverified claims`.
12. Gives a sequential single-agent fallback and explicitly reports reduced review
    independence.

Every item is blocking. The skilled arm passes only when every item passes.
