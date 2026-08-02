---
name: using-research-workflows
description: Use when starting machine learning, LLM, or AI infrastructure research work, before planning, editing, running, or claiming results
---

# Using Research Workflows

First output this complete eight-line block. Never omit a line. Repeat only when
classification changes. Choose one Mode; list all matching Profiles/Environments.

- Mode: exploration/experiment/engineering/release
- Profiles: ML/LLM/AI Infra
- Environment: local/SSH/Slurm/cloud GPU
- Cost gate: auto-approved/user budget/approval required
- Reason: concrete task→Mode; each domain→its Profile; each explicit environment→itself; resource/cost + "no declared budget or authorization"→approval required
- Agent policy: single/reviewed/multi-role
- Override: user may override classification/workflow mode; platform safety remains binding
- Next Skill: copy the selected route below exactly

Priority: user instruction, project rules, automatic classification, Skill defaults.
Mixed LLM systems select LLM + AI Infra.
Load every matching Profile Skill. Use the user's language for responses and
research records.
Agent policy: explicit user Agent policy overrides; otherwise exploration=single;
experiment=reviewed; engineering=reviewed; release=multi-role; high-risk
cross-domain/multi-environment=multi-role.
Routes: exploration=framing-research-work;
experiment=framing-research-work→designing-research-experiments;
engineering=framing-research-work→planning-research-changes;
release=framing-research-work→verifying-research-evidence.
Engineering completes both before modification.

Never infer permission for paid resources, scheduler jobs, large downloads,
multi-GPU/multi-node work, or overruns. Without budget, auto-run only ≤10-minute
CPU or available-local-GPU work; ask if uncertain.

Initialize `.research/` minimally. Isolate engineering/release in Git worktrees
unless rules choose otherwise. Claim completed evidence only; future work proves
nothing.
