# Research Engineering

> Language: English | [简体中文](docs/README.zh-CN.md)

An independent Agent plugin for deep learning, large-language-model, and AI
infrastructure research. Codex is the primary host; Claude Code and Qoder are
supported through compatibility layers. The plugin combines specification-driven work,
isolated debugging, independent review, and layered validation, adapting its
workflow strength to the maturity of the research task. PyTorch is the
first-class ecosystem in this initial release.

> This is not a Python package or desktop application that must be compiled.
> Codex reads the Markdown, JSON, and Python files at runtime. “Build” means
> structural checks, automated tests, and source archives; a ZIP is not a
> double-click installer.

## 0. Five-minute quick start

Clone the public repository and open it in VS Code:

```bash
git clone https://github.com/windy-h-qhang/Research_Plugin_ML.git research-engineering
cd research-engineering
code .
```

The commands work in macOS/Linux shells, Windows PowerShell, and WSL. If
`code` is not on `PATH`, use **File → Open Folder…** in VS Code and open the
cloned `research-engineering` directory.

Start with these files:

| Path | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | Codex plugin identity, version, and entry point |
| `.claude-plugin/plugin.json` | Claude Code compatibility identity and description |
| `.qoder-plugin/plugin.json` | Qoder compatibility identity used by the exported Qoder package |
| `skills/*/SKILL.md` | Eight shared core Skills and three composable Profiles |
| `scripts/` | Research-state initialization, environment capture, run records, and evidence summaries |
| `templates/` | Research-context, experiment, run, and review templates |
| `examples/minimal-project/` | A synthetic minimal example, not real research results |
| `tests/` | Manifest, Skill, script, integration, and behavior tests |
| `docs/real-environment-validation.md` | Boundaries for real GPU, SSH, Slurm, cloud GPU, and Marketplace validation |
| `docs/repository-maturity-roadmap.md` | Planned improvements for CI, collaboration, discoverability, and release governance |

Run the offline suite without installing dependencies:

```bash
python3 -m unittest discover -s tests -v
```

## 1. Scope

Research Engineering is designed for:

- **The PyTorch ecosystem:** training, distributed systems, inference, and
  CUDA/Triton kernels.
- **LLM research:** Hugging Face, DeepSpeed/FSDP, PEFT/TRL, and vLLM.
- **AI infrastructure:** GPU clusters, Slurm, communication optimization, and
  throughput or latency engineering.
- **Reproducible research:** paper experiments, benchmarks, ablations, and
  open-source releases.

It does not provide deep, framework-specific JAX or TensorFlow support in this
release; it does not create cloud resources, manage SSH credentials, or manage
large datasets automatically.

## 2. Platforms, validation, packaging, and installation

### 2.1 Platform boundaries

| Platform | Recommended route | Current boundary |
| --- | --- | --- |
| macOS | Native Terminal, VS Code, and Codex | Offline tests have run; real GPU/SSH/Slurm still need environment-specific validation |
| Linux | Native shell, VS Code, and Codex | Designed to work; not every distribution and GPU-driver combination is covered |
| Windows | Prefer WSL2; use PowerShell for editing and temporary loading | Native Windows is not end-to-end validated; safe-write scripts may refuse to run without POSIX primitives |
| SSH/Slurm | Connect from macOS, Linux, or WSL2 to a Unix-like remote | Use only an existing SSH host alias; job submission requires authorization |

Native Windows is fine for reading Skills and editing Markdown. Use WSL2 for
`init_research_state.py`, `record_run.py`, SSH, or Slurm workflows. Loading a
Skill is not evidence that every helper script has been validated on that
platform.

### 2.2 Requirements and offline validation

- Git for cloning, status checks, and reproducible archives.
- Python 3; helper scripts use the standard library and tests use `unittest`.
- Codex or Claude Code as at least one plugin host.
- VS Code is optional, for reading and editing only.

Refer to the official [Codex CLI](https://developers.openai.com/codex/cli) and
[Claude Code setup](https://code.claude.com/docs/en/setup) documentation for
host installation and changing commands. See [Codex Plugins](https://developers.openai.com/plugins/build/plugins)
and [Claude Code Plugins](https://code.claude.com/docs/en/plugins) for their
plugin mechanisms.

macOS, Linux, or WSL:

```bash
git --version
python3 --version
codex --version
python3 -m unittest discover -s tests -v
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
git diff --check
```

Windows PowerShell:

```powershell
git --version
py -3 --version
codex --version
py -3 -m unittest discover -s tests -v
py -3 -m json.tool .codex-plugin/plugin.json > $null
git diff --check
```

There is no `pip install`, `npm install`, CMake, or binary-build step. These
checks are the local build gate. If OpenAI's `plugin-creator` validator is
already available, it can also validate the plugin structure.

Passing these checks does not validate real GPU, SSH, Slurm, cloud GPU, or a
public Marketplace installation, and does not establish that a research method
outperforms a baseline. See `docs/real-environment-validation.md` for the
complete boundary.

### 2.3 Create a release ZIP

`git archive` includes only files committed to `HEAD`. Review and commit the
intended release first; place the resulting ZIP in ignored `dist/` and never
commit it back to the source repository.

macOS, Linux, or WSL:

```bash
mkdir -p dist
git archive \
  --format=zip \
  --prefix=research-engineering/ \
  --output=dist/research-engineering-0.1.0.zip \
  HEAD

unzip -t dist/research-engineering-0.1.0.zip
```

Use `shasum -a 256` on macOS or `sha256sum` on Linux to calculate a SHA-256
digest. In Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force dist | Out-Null
git archive `
  --format=zip `
  --prefix=research-engineering/ `
  --output=dist/research-engineering-0.1.0.zip `
  HEAD

tar -tf dist/research-engineering-0.1.0.zip
Get-FileHash dist/research-engineering-0.1.0.zip -Algorithm SHA256
```

The ZIP is a source-distribution artifact, not a double-click installer. Do
not extract it into a Codex runtime-cache directory.

### 2.4 Install in Codex through a personal Marketplace

For public users, place the source in a personal plugin directory and add a
personal Marketplace entry. Replace `OWNER/REPOSITORY` with the actual public
repository.

#### Step 1: place the source

macOS, Linux, or WSL:

```bash
mkdir -p ~/plugins
git clone \
  https://github.com/OWNER/REPOSITORY.git \
  ~/plugins/research-engineering
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\plugins" | Out-Null
git clone `
  https://github.com/OWNER/REPOSITORY.git `
  "$env:USERPROFILE\plugins\research-engineering"
```

#### Step 2: add the Marketplace entry

The personal Marketplace file is:

- macOS, Linux, and WSL: `~/.agents/plugins/marketplace.json`;
- Windows: `$env:USERPROFILE\.agents\plugins\marketplace.json`.

The filename must be exactly `marketplace.json`. Do not confuse it with the
plugin's `.codex-plugin/plugin.json`. If a personal Marketplace already
exists, merge the plugin object into its `plugins` array rather than replacing
other installed plugins.

The minimal contents of `~/.agents/plugins/marketplace.json` are:

```json
{
  "name": "personal",
  "interface": {
    "displayName": "Personal Plugins"
  },
  "plugins": [
    {
      "name": "research-engineering",
      "source": {
        "source": "local",
        "path": "./plugins/research-engineering"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Developer Tools"
    }
  ]
}
```

Create or open the file:

```bash
mkdir -p ~/.agents/plugins
code ~/.agents/plugins/marketplace.json
```

Windows PowerShell:

```powershell
New-Item `
  -ItemType Directory `
  -Force "$env:USERPROFILE\.agents\plugins" | Out-Null
code "$env:USERPROFILE\.agents\plugins\marketplace.json"
```

Use a plain-text editor if `code` is unavailable; do not accidentally save
`marketplace.json.txt`.

#### Step 3: install and load it in Codex

The normal personal Marketplace is discovered automatically, so this flow does
not require
`codex plugin marketplace add`:

```bash
codex plugin add research-engineering@personal
codex plugin list
```

`codex plugin list` should show `research-engineering@personal` as installed.

On macOS, fully quit and reopen the ChatGPT desktop app, switch to **Codex**,
then open **Plugins** or **Plugins Directory**. Open **Personal Plugins →
Research Engineering** and choose **Install** or **Enable**. If the CLI
installation succeeded, it should show **Installed**; confirm that it is
enabled. Create a new task rather than reusing a task that was open before the
installation, then ask it to state the mode and Profiles it would use.

On Windows, first complete the Marketplace steps in **Windows PowerShell** and
run the two CLI commands above. Fully quit and reopen the Windows ChatGPT/Codex
app, then follow **Codex → Plugins / Plugins Directory → Personal Plugins →
Research Engineering**. The Windows desktop application reads the Windows user
directory; configuring only WSL's `~/.agents/plugins/marketplace.json` will not
normally make the plugin appear in the Windows desktop app. WSL is better for
the project's Python, SSH, and Slurm workflows.

### 2.5 Team or repository Marketplace

Maintainers can create a separate Marketplace root:

```text
marketplace-root/
├── .agents/plugins/marketplace.json
└── plugins/research-engineering/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    ├── skills/
    └── scripts/
```

This non-default Marketplace must be registered explicitly:

```bash
codex plugin marketplace add /path/to/marketplace-root
codex plugin marketplace list
codex plugin add research-engineering@marketplace-name
```

In Windows PowerShell, replace `/path/to/marketplace-root` with a real Windows
path. `source.path` is relative to the Marketplace root and must remain
`./plugins/research-engineering`.

### 2.6 Load in Claude Code

Codex is the primary host, but this repository also provides
`.claude-plugin/plugin.json`. Claude Code reads Skills from `skills/`. The
official `--plugin-dir` route below is a development-time load for one Claude
Code session; it is not an installation in Claude Marketplace.

> Claude Code is a terminal Agent. These instructions do not apply to the
> Claude Desktop chat application.

macOS:

```bash
cd ~/plugins
claude --plugin-dir ./research-engineering
```

From the plugin root, use `claude --plugin-dir .` instead.

Windows PowerShell:

```powershell
Set-Location "$env:USERPROFILE\plugins"
claude --plugin-dir .\research-engineering
```

In WSL2, use the WSL path:

```bash
cd ~/plugins
claude --plugin-dir ./research-engineering
```

In Claude Code, use `/help` to find the `research-engineering` namespace; try
`/research-engineering:using-research-workflows`; inspect **Errors** through
`/plugin` if it is missing; and use `/reload-plugins` after edits. Long-lived
Marketplace installation, upgrades, and public release have a separate
distribution process and are not end-to-end validated here.

### 2.7 Install in Qoder

Qoder reads `.qoder-plugin/plugin.json` and loads Skills from `skills/`. A
Qoder package must not contain `.codex-plugin`, and its directory name must
match the manifest `name`, so export the Qoder-native package first instead of
installing the repository root directly:

```bash
python3 scripts/export_qoder_plugin.py --zip
```

This stages `dist/research-engineering/` and builds
`dist/research-engineering-0.1.0.zip`; both pass the offline structure
validator. Then install with `qodercli`:

```bash
qodercli plugin install "$(pwd)/dist/research-engineering"
qodercli plugin list
qodercli skills list
```

In the Qoder IDE, install from local through the Plugins panel and select
`dist/research-engineering/`. After installation, the eleven Skills are
available by name, for example `using-research-workflows`. Qoder ignores the
Codex-specific `skills/*/agents/openai.yaml` files; no Skill edits are needed.

### 2.8 Use after installation

Use natural-language tasks; no Python import is needed. State the goal, mode,
Profiles, execution environment, and budget explicitly. For example:

```text
Use Research Engineering in experiment mode with the ML Profile to inspect this
PyTorch classification experiment. First create a .research context and
experiment contract; run CPU unit tests only; do not download data or use a
GPU; and do not treat one smoke test as a scientific conclusion.
```

```text
Use the LLM and AI Infra Profiles to review this vLLM benchmark. First perform
read-only checks and list throughput, P50/P95 latency, peak memory, and
correctness gates. Do not start a remote task without my authorization.
```

The plugin may create `.research/` records in a target research project. It
does not submit cluster jobs or consume paid resources as an automatic
consequence of installation.

### 2.9 Installation troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| `codex --version` returns `ENOENT` | A platform binary is missing from the npm package | Reinstall the official CLI: `npm install --global @openai/codex` |
| Personal Marketplace is not found | Wrong filename or user directory | Check `.agents/plugins/marketplace.json` |
| Marketplace is visible but the plugin is not | Incorrect `source.path` or an extra directory level | Check that `~/plugins/research-engineering/.codex-plugin/plugin.json` exists |
| Windows helper script rejects a safe write | Required POSIX file primitives are unavailable | Use WSL2; do not bypass the safety check |
| Claude Code cannot find Skills | The plugin root was not passed at startup, or the Manifest/Skill has an error | Restart with `claude --plugin-dir <plugin-directory>` and inspect `/plugin` errors |
| Qoder does not show the Skills | The repository root was installed instead of the exported package | Run `python3 scripts/export_qoder_plugin.py` and install `dist/research-engineering/` |
| Changes do not appear | The host is using an old cache | Reinstall, restart the host, and create a new task |

Troubleshoot in this order: CLI launch → Marketplace JSON → Manifest depth →
plugin installation → a new task. Do not edit Codex cache directories directly.

## 3. Automatic modes and user overrides

The plugin classifies work into four modes:

- **Exploration:** notebooks, prototypes, and formula checks; minimal context,
  static checks, and bounded smoke tests.
- **Experiment:** formal training, ablations, and benchmarks; an experiment
  contract, baseline, configuration record, and scientific review.
- **Engineering:** training frameworks, distributed systems, inference serving,
  and kernel development; isolation, an implementation plan, regression
  baseline, and engineering review.
- **Release:** paper code or public models; complete reproduction records,
  compatibility, and independent reproducibility review.

Before work, the Agent states its classification, reason, and enabled rules.
User instructions always override automatic classification: the user can choose
a mode, Profiles, validation depth, or workflow exception. An explicit user
instruction cannot waive platform safety boundaries; paid, shared-cluster, or
other high-cost work still needs an approved budget or explicit authorization.

The priority order is: explicit instructions in the current task → repository
rules such as `AGENTS.md` → automatic mode and risk classification → Skill
defaults.

## 4. Composable Profiles

Profiles are domain Skills that can be loaded together when relevant.

### ML Profile (`applying-ml-research-profile`)

For PyTorch models and conventional deep-learning experiments:

- data splits, leakage, sampling, and class mapping;
- tensor shape, dtype, device, and broadcasting;
- losses, metrics, and label semantics;
- gradient flow, freezing strategy, and optimizer parameter groups;
- seeds, ablations, and statistical stability;
- calibration, class imbalance, and distribution shift.

### LLM Profile (`applying-llm-research-profile`)

For Hugging Face, Accelerate, DeepSpeed/FSDP, PEFT/TRL, and vLLM:

- tokenizer, special-token, and template correctness;
- data mixing, truncation, packing, and label masks;
- training/evaluation contamination;
- generation parameters and evaluation reproducibility;
- PEFT, checkpoints, weight merging, and resume compatibility;
- long context, KV cache, quantization, and parallel settings.

### AI Infra Profile (`applying-ai-infra-profile`)

For distributed training, serving, and GPU infrastructure:

- correctness before performance, including numerical-equivalence checks;
- GPU/node topology and communication backend;
- warm-up, synchronization, measurement windows, and repetitions;
- throughput, latency distributions, peak memory, utilization, and cost;
- precision tradeoffs and numerical consistency;
- recovery, preemption, checkpoints, and job restarts.

## 5. Local, SSH, Slurm, and cloud GPU work

The plugin supports local workstations, SSH remotes, Slurm clusters, cloud GPUs
treated as SSH remotes, and a hybrid path of local design/review → remote
execution → evidence collection.

Use only an existing SSH host alias. Before connecting, confirm the alias, the
exact remote repository path, its synchronization mechanism, and permitted
actions. The plugin does not create keys, read private keys, or silently modify
SSH configuration. After a disconnect, query the remote process or Slurm state
before declaring a job failed.

## 6. The `.research/` directory

The plugin can create lightweight project metadata on demand:

```text
.research/
├── .gitignore          # excludes local/
├── context.md          # goals, Profiles, environment, and budget
├── experiments/        # contracts: hypotheses, baselines, variables, metrics, rules
├── runs/               # Git revisions, environment fingerprints, and exit state
├── reviews/            # scientific, engineering, and reproducibility reviews
├── local/              # local connection details; ignored by default
└── progress.md         # resumable progress ledger
```

`context.md` records global constraints. Experiment contracts define hypotheses,
variables, metrics, and decision rules quantitatively. Run records identify the
local/remote revision, relevant runtime versions, exit state, and failure class.
Keep SSH aliases and remote paths in ignored `local/`; lightweight, shareable
metadata can be version-controlled.

## 7. Cost and authorization

The Agent may run static checks, unit tests, and CPU validation. It may also run
a bounded local or single-GPU smoke test within an existing budget.

Without a preset budget, the default is no paid resources, no scheduler
submission, no large asset downloads, and an expected completion within ten
minutes on the currently available CPU or GPU.

Explicit authorization is required for large model or dataset downloads,
long-running training, multi-GPU or multi-node work, Slurm submission, paid
cloud resources, and benchmarks that can materially consume shared resources.
When a user provides time, GPU, node, or cost limits, tasks inside that budget
can proceed; stop starting new work once the budget is reached and report the
missing evidence.

## 8. Multi-Agent work

Roles are selected by mode and risk:

| Mode | Roles |
| --- | --- |
| Exploration | One Agent |
| Experiment | Implementer + Scientific Reviewer |
| Engineering | Implementer + Engineering Reviewer |
| Engineering with algorithm semantics | Add Scientific Reviewer |
| Release | Add Reproducibility Reviewer |

Writes in a shared checkout are serial by default; independent read-only
investigations may run in parallel. If native multi-agent work is unavailable,
honor a user's explicit request to stop or to use a fallback. When no fallback
preference is specified, use a staged single-Agent self-review and disclose the
reduced review independence. Reviewers make independent judgments; an
Implementer's report is not proof.

## 9. Five helper scripts

All helper scripts prioritize the Python standard library and are stateless,
testable, and idempotent.

| Script | Purpose |
| --- | --- |
| `init_research_state.py` | Initializes `.research/` and templates without overwriting existing files |
| `capture_environment.py` | Captures local or SSH Git, Python, PyTorch, CUDA, and GPU summaries as structured JSON |
| `record_run.py` | Creates or updates a run record, validates required fields, and preserves unknown fields |
| `inspect_slurm_job.py` | Parses `squeue`/`sacct` output and records job status, exit cause, and resource use |
| `summarize_evidence.py` | Summarizes code validation, run status, research conclusions, missing evidence, and residual risk |

## 10. End-to-end example

The following quick start uses the **synthetic example** in
`examples/minimal-project/`. It demonstrates record formats and evidence
boundaries. It does not mean this repository has run training.

**1. Make an experiment request**

> On a local CPU, implement and validate a confidence gate. First run a smoke
> test of no more than 20 steps, not full training. The goal is to reduce false
> positives without a material recall regression.

**2. The router states its classification first**

```text
- Mode: experiment
- Profiles: ML
- Environment: local
- Cost gate: auto-approved
- Reason: confidence-gate formal comparison→experiment; classifier quality→ML; explicit local CPU→local; bounded no-paid 20-step Smoke Test→auto-approved
- Agent policy: reviewed
- Override: user may override classification/workflow mode; platform safety remains binding
- Next Skill: framing-research-work→designing-research-experiments
```

This is only a routing statement. It does not prove that the plugin is
installed or start a run. The user may override the mode, Profiles, or
validation depth before execution.

**3. Initialize lightweight research state**

```bash
python3 /path/to/research-engineering/scripts/init_research_state.py --root .
```

The initializer creates only missing `.research/` files and templates. Record
the hypothesis, baseline, split, metrics, and success/failure/inconclusive
rules in `experiments/demo.md`.

**4. Run and record an authorized local smoke test**

```bash
python train.py --config configs/demo.yaml --max-steps 20 --seed 7
```

The synthetic plan at `.research/runs/demo-smoke.json` demonstrates the
command and record format. It is not an executed run:

```json
{
  "run_id": "demo-smoke",
  "experiment_id": "demo-confidence-gate",
  "environment_id": "local-demo",
  "command": "python train.py --config configs/demo.yaml --max-steps 20 --seed 7",
  "status": "planned",
  "validation_level": "smoke",
  "conclusion": "not_verified"
}
```

A Scientific Reviewer may write a design review to
`.research/reviews/demo-scientific.md`. `PASS` means only that the review found
no blocking design issue; it cannot elevate a one-seed smoke test into a
scientific conclusion.

**5. Report the three evidence states**

```text
Code verification: not_verified — no deterministic, regression, or smoke validation has run.
Experiment execution: not_verified — formal multi-seed experiments and threshold sweeps have not run.
Conclusion support: not_verified — no effect size, statistical comparison, or baseline evidence is available.
```

Run the predefined full experiment and statistical comparison before claiming
that the confidence gate improves model quality.

## 11. Security and privacy

- Do not read, save, or copy SSH private keys.
- Do not put passwords, tokens, or API keys in commands, logs, or `.research/`.
- Do not silently modify SSH configuration or system files.
- `.research/local/` is ignored by default.
- Shareable run records use a user-defined `environment_id`, not an exact host
  name or absolute path, unless the user explicitly requests it.

## 12. Tests

```bash
# Run all tests
python3 -m unittest discover -s tests -v

# Run plugin-structure validation when the validator is available
python3 /path/to/validate_plugin.py .
```

The latest public release-preparation run executed **127 offline automated
tests** on macOS. “127 tests” means `unittest` cases, not 127 GPU trainings or
127 real research experiments. They cover plugin Manifests, marketplace
documentation, the 11 Skills, five helper scripts, fixed Slurm fixtures,
synthetic `.research/` contracts, evidence-layer separation, and behavior
evidence.

Thus, `127/127` means the offline contract passed at that time. It does not
establish real GPU, SSH, Slurm, cloud GPU, or Marketplace success, nor any
model-quality, throughput, or scientific-superiority claim. Record acceptance
results separately for Linux, Windows/WSL2, and real infrastructure.

## 13. Update and uninstall

To update, back up and read the new instructions before updating the personal
plugin directory.

macOS, Linux, or WSL:

```bash
cd ~/plugins/research-engineering
git pull --ff-only
codex plugin add research-engineering@personal
```

Windows PowerShell:

```powershell
Set-Location "$env:USERPROFILE\plugins\research-engineering"
git pull --ff-only
codex plugin add research-engineering@personal
```

For a formal release, update the semantic version in
`.codex-plugin/plugin.json`. Developers may use `plugin-creator`'s local
cachebuster to refresh development caches without changing the release version;
do not use a local cachebuster version for a public release. Reopen the host and
create a new task after updating. The plugin never migrates a research project's
`.research/` automatically.

For a Claude Code `--plugin-dir` session, run `/reload-plugins` after updating
the source, or restart the session with the same command.

To uninstall:

```bash
codex plugin remove research-engineering@personal
```

Uninstalling the plugin does not delete a research project's `.research/`.
Keep or remove source and the personal Marketplace entry deliberately; do not
delete the entire personal Marketplace file because it may contain other
plugins.

## 14. Public-release checklist

Before a source or release publication, check that:

- the worktree contains no `.env`, credentials, host names, personal absolute
  paths, or local connection configuration;
- `.research/local/`, ZIPs, `dist/`, `tmp/`, and operating-system temporary
  files are not staged;
- the Codex Manifest version, author display name, license, and description are
  safe for public use;
- the Claude Code Manifest agrees with the Codex Manifest on name, version, and
  license;
- the unit suite and plugin validator pass;
- a `git archive` ZIP excludes private reports, internal plans, and Git
  metadata; and
- release notes distinguish offline tests, real-environment runs, and evidence
  for scientific conclusions.

Before the first public release, replace `OWNER/REPOSITORY` in installation
examples with the actual public repository. Removing a sensitive file from the
current tree does not remove it from earlier commits. Audit history before
publishing a complete history; if it is unsuitable, create a clean public
repository from an audited source tree or use a deliberately approved rewritten
history. Do not force-push without an explicit instruction and a backup.
