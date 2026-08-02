# Fresh-context Skill behavior protocol

Use this protocol to determine whether a Skill changes agent behavior. Build
the harness and cases first; do not run behavior agents as part of creating
this protocol.

1. Create the case file before the Skill.
2. Run the prompt in at least five fresh subagents without access to the target Skill.
3. Save every response verbatim and score every rubric item; manually inspect all matches.
4. Create the minimal Skill that addresses observed failures.
5. Run the identical prompt in at least five new fresh subagents instructed to read the target Skill first.
6. Save every response verbatim and score the same rubric; compare variance with the no-guidance control.
7. A discipline Skill requires at least three combined pressures; a Profile requires recognition, application, and counter-example coverage.
8. The post-Skill arm must pass every blocking rubric item in all five repetitions before commit.

## Result files

Store one result file per case/Skill arm in `tests/behavior/results/`. Each
fresh repetition must have one complete response section. Use the same rubric
in both the control and skilled arms, and give every repetition a unique
evaluator/repetition identity.

Each response section must contain:

```text
Case and Context (or a documented arm-level equivalent)
Observed response (or a documented equivalent)
Rubric
Verdict
```

`Verbatim response` and `Rubric evidence` are acceptable documented
equivalents. Retain the observed response verbatim. Score each rubric item
manually, record the resulting verdict, and inspect every apparent rubric match
rather than relying on a keyword count. Keep failed, superseded, or excluded
evidence visible with its status and replacement reason; never delete it to
make the final arm appear cleaner.
