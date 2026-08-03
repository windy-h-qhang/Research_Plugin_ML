# Repository Maturity Roadmap

> Status: planned improvements. This document records future work; it does not
> claim that an external configuration, publication, or platform validation has
> been completed.

This roadmap keeps the repository public-safe and focused on verifiable
engineering practices. Current repository files and explicit user instructions
remain authoritative.

## Priority 0: Continuous verification and branch safety

- Add a GitHub Actions workflow that runs the unit-test suite on supported
  CPU-based runners, validates the plugin manifests as JSON, and runs
  `git diff --check`.
- Add branch-protection rules for `main`: require pull requests and successful
  required checks, and prevent force-pushes and branch deletion. Decide whether
  administrators may bypass these rules before enabling the setting.
- Add a CI status badge to the README only after the workflow has completed
  successfully on the default branch.

Acceptance evidence: a reviewed workflow file, successful workflow runs, and
the intended branch-protection settings visible in the repository settings.

## Priority 1: Contribution and security governance

- Add `CONTRIBUTING.md` with local validation commands and expectations for
  focused, reviewable changes.
- Add `SECURITY.md` that directs private vulnerability reports through GitHub's
  private reporting feature when enabled. Do not publish personal contact
  details.
- Add a code of conduct, issue forms, and a pull-request template that request
  reproducible context while warning contributors not to include credentials,
  private paths, or sensitive logs.

## Priority 2: Discoverability and research credit

- Configure accurate GitHub topics, such as `codex`, `pytorch`,
  `machine-learning`, `llm`, `ai-infrastructure`, and `research-engineering`.
- Add a repository social-preview image after confirming that all included
  visual assets are licensed for public distribution.
- Add `CITATION.cff` for academic and research-engineering citations.

## Priority 3: Controlled release process

- Add a concise changelog and a release guide covering versioning, validation,
  tags, GitHub Releases, rollback considerations, and release notes.
- Create tags and GitHub Releases only after explicit approval and after the
  documented validation evidence has been reviewed.
- Keep Marketplace publication separate from repository releases; it requires
  its own explicit authorization and acceptance evidence.

## Evidence and environment boundaries

Automated checks support source-level confidence; they do not establish
end-to-end behavior on Windows, Claude Code, GPU, SSH, Slurm, cloud GPU, or a
public Marketplace. Record any future real-environment work in
[`real-environment-validation.md`](real-environment-validation.md), with its
commands, observations, and limitations. A smoke test is not evidence for a
scientific, quality, throughput, or performance claim.

## Deferred external actions

This document does not authorize remote configuration, pushing, merging,
publishing, Marketplace submission, paid cloud use, large downloads, long
training, multi-GPU or multi-node runs, Slurm submission, or remote overwrite
or deletion. Each such action remains subject to explicit user authorization or
an explicitly provided budget.
