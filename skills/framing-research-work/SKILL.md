---
name: framing-research-work
description: Use when a research request has an unclear question, mixed maturity expectations, undefined scope, or ambiguous success criteria
---

# Framing Research Work

Turn the request into a compact research contract before implementation.
State conflicting commitments explicitly rather than silently choosing one.

## Output contract

Write only these fields, in this order:

- **Problem:** the research question or change.
- **Mode:** exploration, experiment, engineering, or release; mark unresolved mixed expectations.
- **Scope:** the smallest viable slice for the selected mode.
- **Constraints:** time, environment, compatibility, and conflicting requirements.
- **Success:** separate observable engineering behavior from evidence about accuracy or effect.
- **Non-goals:** deferred maturity, features, and claims.

Then ask exactly one highest-leverage clarification question. Do not bundle
several questions into it. Ask for one decision or one fact; joining multiple
inputs with "and" or "or" is still a batch.

If a contradiction remains, stop after that question. Do not emit code,
pseudocode, commands, patches, or an implementation plan before the user
resolves the scope.

## Maturity

- Exploration uses a short contract.
- Experiment adds a falsifiable hypothesis, baseline, metrics, and evaluation data.
- Engineering adds interfaces, compatibility, and performance boundaries.
- Release adds reproduction and external-use criteria.

Prefer the least mature mode that answers the immediate question. A quick
prototype is not publication quality; place publication work in **Non-goals**
unless the user selects it.

Code running establishes engineering behavior only. An accuracy improvement
requires comparative evidence from a defined evaluation. Never promise the
result.
