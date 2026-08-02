# Repository Instructions

## Scope and compatibility

- This repository is an independent Research Engineering Agent plugin. Codex is
  the primary host; the repository also provides a Claude Code compatibility
  layer.
- It targets PyTorch-first research and engineering across machine learning,
  large language models, and AI infrastructure.
- Do not modify, replace, or depend on Superpowers. Keep Skills independent and
  avoid name or behavior conflicts with other plugins.

## Working approach

- Follow explicit user instructions over any automatic classification of work as
  exploration, experiment, engineering, or release.
- Before changing files, inspect the Git state and the relevant existing files.
  Build on the current implementation; do not recreate completed work from
  scratch.
- If `.local-history/` exists, treat it only as a local, Git-ignored historical
  reference. Never stage, commit, push, or publish it; current repository files
  and the user's latest instructions take precedence over its contents.
- Keep repository content suitable for public distribution. Do not add personal
  paths, user or host identifiers, credentials, tokens, SSH aliases, or private
  environment details.

## Validation and resource safety

- Static checks, unit tests, and bounded CPU validation are in scope unless the
  user says otherwise.
- Obtain explicit user authorization, or follow an explicitly provided budget,
  before downloading large models or datasets, running long training, using
  multiple GPUs or nodes, submitting Slurm jobs, using paid cloud resources, or
  overwriting or deleting remote data.
- Keep code verification, experiment execution, and evidence for scientific
  conclusions separate. A single smoke test is not evidence for a scientific,
  quality, throughput, or performance conclusion.

## Git and release boundaries

- Do not push, merge, publish, submit to a Marketplace, or rewrite Git history
  without an explicit user instruction.
- Completion reports must name the current validation commands and results, and
  list relevant platforms or real environments that remain unverified.
- Do not claim end-to-end validation for Windows, Claude Code, GPU, SSH, Slurm,
  cloud GPU, or a public Marketplace unless it was actually performed and its
  evidence is available for the current change.
