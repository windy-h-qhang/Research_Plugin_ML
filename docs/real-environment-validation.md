# Real-environment validation boundaries and next steps

> Language: English | [简体中文](real-environment-validation.zh-CN.md)

Last updated: 2026-08-03

## Current conclusion

`research-engineering` 0.1.0 has completed plugin-structure checks, Skill
routing, helper scripts, behavior evidence, packaging rules, and safety checks,
and is ready for controlled trial use. A local Codex Marketplace entry was
observed as installed and enabled on macOS.

The accurate status is: **offline build and automated validation are complete,
as is one macOS local Codex installation-state check; end-to-end validation is
not complete for a public Marketplace, Claude Marketplace, Windows, real GPU,
SSH, Slurm, or cloud GPU.** This does not mean the plugin is incomplete, but it
does mean compatibility across all host and infrastructure combinations must
not be claimed.

## Validated scope

- Eight shared core Skills and three composable research Profiles.
- Automatic exploration, experiment, engineering, and release classification,
  with explicit user instructions taking priority.
- PyTorch-first ML, LLM, and AI Infra workflows.
- `.research/` initialization, environment capture, run records, Slurm
  inspection, and evidence summaries.
- Layered deterministic tests, bounded smoke tests, regression evidence, and
  scientific-conclusion evidence.
- SSH read-only-first behavior, remote-path and synchronization discovery, and
  approval gates for high-risk actions.
- 127 offline automated tests, 11 Skill checks, plugin validation, behavior
  evaluation, and independent reviews.
- Git-export and ZIP exclusion rules.
- The macOS local Codex entry's installed/enabled state.

The Claude compatibility Manifest has passed structural validation. Structural
validation must not be described as a successful Claude Code or Claude
Marketplace installation.

## Why the remaining validation has not run

1. Real GPU, cloud GPU, long training, and multi-GPU or Slurm runs can incur
   material compute cost and need explicit authorization or a budget.
2. SSH end-to-end validation depends on a real host, authentication, exact
   remote project path, and established synchronization mechanism; the plugin
   neither stores nor manages credentials.
3. Slurm accounts, partitions, module systems, limits, and submission policies
   depend on the specific cluster and cannot be replaced by a local simulation.
4. Public Marketplace release changes external state. The current authorization
   covers local organization, offline validation, and release preparation only.
5. Native Windows, WSL2, and Claude Code need separate environments; a macOS
   Codex result cannot substitute for them.

## Practical impact

| Use case | Current risk | Notes |
| --- | --- | --- |
| Local research planning, code review, and experiment design | Low | Core routing and workflows are automatically validated |
| Small local CPU/PyTorch experiments | Low | Run one installation smoke test after setup |
| CUDA/GPU training | Medium | Confirm the driver, CUDA, PyTorch, and extension versions together |
| Remote development over SSH | Medium | Confirm authentication, synchronization, and remote path |
| Slurm cluster work | Medium | Adapt to the cluster policy and validate a minimal job |
| Cloud GPU | Medium | Confirm provider, image, storage, networking, and access |
| Local Codex on macOS | Low | Installed/enabled was observed; validate representative behavior in a new task |
| Codex on Windows | Medium | User directory, PowerShell, and desktop loading are not yet exercised |
| Local Claude Code loading | Medium | A compatible Manifest and commands exist; no real-machine acceptance yet |
| Public Marketplace distribution | Medium | One-click installation, update, removal, and publication remain untested |

## Recommended acceptance order

1. In a new macOS Codex task, confirm that all 11 Skills are discoverable and
   can handle a routing example.
2. Validate loading, updating, and removal in Windows Codex, macOS Claude Code,
   and Windows Claude Code separately.
3. Run a few-minute, no-large-download, single-GPU smoke experiment locally or
   on a remote host.
4. Connect to SSH in read-only mode and validate environment capture,
   remote-path discovery, and a synchronization plan.
5. Inspect the Slurm environment and scripts without submitting a job.
6. After explicit authorization, submit one minimal, time-bounded,
   resource-bounded Slurm job.
7. If public distribution is needed, validate public Marketplace installation,
   update, removal, and release.

## Operational gates

The following actions require explicit user authorization or compliance with a
user-provided resource and cost budget:

- downloading large models or datasets;
- starting long training, multi-seed experiments, or multi-GPU jobs;
- submitting a Slurm job;
- creating or using paid cloud resources;
- overwriting or deleting remote files; and
- installing, publishing, updating, or removing Marketplace plugins.

For every real-environment acceptance run, record the environment, command,
resource limit, run ID, result, failure evidence, and the scope of the
conclusion. A single smoke test is not scientific evidence that a model or
method is superior.
