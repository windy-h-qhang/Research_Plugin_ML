# Research Engineering

> 语言： [English](../README.md) | 简体中文

面向深度学习、大模型与 AI 基础设施研究的独立 Agent 插件，以 Codex 为主要
宿主，并提供 Claude Code 兼容层。它采用规格驱动、隔离调试、独立审查和
分层验证，同时根据研究阶段调整流程强度。首版以 PyTorch 生态为第一等支持
对象。

> 本项目不是需要编译的 Python 包或桌面应用。Codex 在运行时读取其中的
> Markdown、JSON 和 Python 脚本；所谓“构建”是结构校验、自动化测试和生成
> 源码归档。ZIP 本身不是可以双击安装的插件安装器。

## 0. 五分钟快速开始

先将公开仓库地址替换到下面的命令中，然后克隆并用 VS Code 打开：

```bash
git clone https://github.com/windy-h-qhang/Research_Plugin_ML.git research-engineering
cd research-engineering
code .
```

这些命令可在 macOS/Linux Shell、Windows PowerShell 和 WSL 中使用。如果
`code` 不在 PATH 中，也可以在 VS Code 选择 **File → Open Folder…**，然后
打开克隆得到的 `research-engineering` 文件夹。

第一次阅读建议从这些文件开始：

| 路径 | 用途 |
|------|------|
| `.codex-plugin/plugin.json` | Codex 插件名称、版本和入口 |
| `.claude-plugin/plugin.json` | Claude Code 兼容层的名称、版本和描述 |
| `skills/*/SKILL.md` | 8 个共享核心 Skills 与 3 个可组合 Profiles |
| `scripts/` | 初始化、环境捕获、运行记录和证据汇总工具 |
| `templates/` | 研究上下文、实验、运行和审查模板 |
| `examples/minimal-project/` | 合成的最小使用示例，不代表真实研究结果 |
| `tests/` | Manifest、Skills、脚本、集成和行为测试 |
| `docs/real-environment-validation.zh-CN.md` | 真实 GPU、SSH、Slurm、云 GPU 和 Marketplace 的验收边界 |

无需安装依赖即可运行离线测试：

```bash
python3 -m unittest discover -s tests -v
```

## 1. 定位与适用范围

本插件为以下场景设计：

- **PyTorch 生态**：模型训练、分布式、推理、CUDA/Triton 算子；
- **大模型研究**：Hugging Face、DeepSpeed/FSDP、PEFT/TRL、vLLM；
- **AI 基础设施**：GPU 集群、Slurm、通信优化、吞吐与延迟工程；
- **可复现研究**：论文实验、Benchmark、消融研究、开源发布。

**不适用**于：JAX/TensorFlow 深度专属支持（首版以 PyTorch 为第一等公民）、自动创建云资源、管理 SSH 凭据或大型数据集。

## 2. 与 Superpowers 的区别

| 维度 | Superpowers | Research Engineering |
|------|-------------|----------------------|
| 主要定位 | 通用软件工程工作流与开发纪律 | 研究代码、实验执行与研究证据 |
| 验证重点 | 对功能与缺陷修复强调测试先行和完成前验证 | 按证据层选择确定性测试、不变量、Smoke、回归或统计验证 |
| 计划粒度 | 偏向可快速执行、可逐项验证的实现步骤 | 按可独立审查的研究或工程单元拆分，不强制固定分钟数 |
| 审查角色 | 通用实现、规格与代码质量审查 | Implementer + Scientific/Engineering/Reproducibility Reviewer |
| 领域规则 | 可用于通用工程任务 | 三个可组合 Profile：ML、LLM、AI Infra |
| 研究运行约定 | 不作为本插件文档的声明对象 | 明确定义本地、SSH、Slurm、云端 GPU、`.research/` 与成本门禁 |

两套插件相互独立，Skill 名称无冲突，可以同时使用。Research Engineering
不会修改、覆盖或依赖 Superpowers；上表只说明两者的主要关注点，不表示
Superpowers 不能处理远端、研究或成本相关任务。

## 3. 平台、验证、打包与安装

### 3.1 平台支持边界

| 平台 | 建议方式 | 当前边界 |
|------|----------|----------|
| macOS | 原生 Terminal、VS Code、Codex | 已运行离线测试；真实 GPU/SSH/Slurm 仍需按环境验收 |
| Linux | 原生 Shell、VS Code、Codex | 设计为支持；尚未覆盖所有发行版和 GPU 驱动组合 |
| Windows | 优先使用 WSL2；编辑和临时加载可用 PowerShell | 原生 Windows 未完成端到端验证，安全写入脚本可能因缺少 POSIX 文件原语而拒绝执行 |
| SSH/Slurm | 从 macOS、Linux 或 WSL2 连接 Unix-like 远端 | 只使用已有 SSH Host Alias；提交作业仍需授权 |

Windows 用户若只阅读 Skills 或编辑 Markdown，可以使用原生 VS Code。若需要
运行 `init_research_state.py`、`record_run.py`、SSH 或 Slurm 工作流，推荐在
WSL2 中使用本插件。不要把“能够加载 Skills”误报为“全部辅助脚本已在该平台
验证通过”。

### 3.2 环境要求与离线验证

- Git：克隆源码、检查版本状态和生成可复现归档；
- Python 3：辅助脚本只依赖标准库，测试使用 `unittest`；
- Codex 或 Claude Code：至少安装一个插件宿主；
- VS Code：可选，仅用于阅读和编辑。

宿主安装与命令变化请以
[Codex 官方文档](https://developers.openai.com/codex/cli)和
[Claude Code 官方文档](https://code.claude.com/docs/en/setup)为准；插件机制
分别见 [Codex Plugins](https://developers.openai.com/plugins/build/plugins) 和
[Claude Code Plugins](https://code.claude.com/docs/en/plugins)。

macOS、Linux 或 WSL：

```bash
git --version
python3 --version
codex --version
python3 -m unittest discover -s tests -v
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
git diff --check
```

Windows PowerShell：

```powershell
git --version
py -3 --version
codex --version
py -3 -m unittest discover -s tests -v
py -3 -m json.tool .codex-plugin/plugin.json > $null
git diff --check
```

本项目没有 `pip install`、`npm install`、CMake 或二进制编译步骤。以上检查
就是本项目的本地构建门。如本机提供 OpenAI `plugin-creator`，还可以运行其
`validate_plugin.py` 验证插件结构。

这些检查不证明真实 GPU、SSH、Slurm、云 GPU 或公开 Marketplace 已完成
端到端验收，也不证明某种研究方法优于基线。完整边界见
`docs/real-environment-validation.zh-CN.md`。

### 3.3 生成发布 ZIP

`git archive` 只包含已经提交到 `HEAD` 的文件。打包前应先审查并提交准备
发布的改动；生成的 ZIP 放在已忽略的 `dist/`，不要提交回源码仓库。

macOS、Linux 或 WSL：

```bash
mkdir -p dist
git archive \
  --format=zip \
  --prefix=research-engineering/ \
  --output=dist/research-engineering-0.1.0.zip \
  HEAD

unzip -t dist/research-engineering-0.1.0.zip
```

校验 SHA-256 时，macOS 使用：

```bash
shasum -a 256 dist/research-engineering-0.1.0.zip
```

Linux 使用：

```bash
sha256sum dist/research-engineering-0.1.0.zip
```

Windows PowerShell：

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

ZIP 是源码分发产物，不是可双击安装的应用，也不应直接解压到 Codex 的运行时
缓存目录。

### 3.4 安装到 Codex：个人 Marketplace

公开用户最简单的安装方式是把插件放在个人插件目录，并在个人 Marketplace
中添加条目。下面的 `OWNER/REPOSITORY` 必须替换为真实公开仓库。

#### 第一步：放置插件源码

macOS、Linux 或 WSL：

```bash
mkdir -p ~/plugins
git clone \
  https://github.com/OWNER/REPOSITORY.git \
  ~/plugins/research-engineering
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\plugins" | Out-Null
git clone `
  https://github.com/OWNER/REPOSITORY.git `
  "$env:USERPROFILE\plugins\research-engineering"
```

#### 第二步：添加个人 Marketplace 条目

个人 Marketplace 文件位于：

- macOS、Linux、WSL：`~/.agents/plugins/marketplace.json`；
- Windows：`$env:USERPROFILE\.agents\plugins\marketplace.json`。

文件名必须严格为 `marketplace.json`。`.codex-plugin/plugin.json` 是插件自身
Manifest，两者不能混用。如果个人 Marketplace 已经存在，应把下面的插件
对象合并到其 `plugins` 数组，不要覆盖其他已安装插件。

`~/.agents/plugins/marketplace.json` 的最小内容为：

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

创建目录：

```bash
mkdir -p ~/.agents/plugins
code ~/.agents/plugins/marketplace.json
```

Windows PowerShell 对应命令：

```powershell
New-Item `
  -ItemType Directory `
  -Force "$env:USERPROFILE\.agents\plugins" | Out-Null
code "$env:USERPROFILE\.agents\plugins\marketplace.json"
```

将上面的 JSON 粘贴到打开的文件并保存。没有 `code` 命令时，可用任意纯文本
编辑器创建同名文件；不要保存成 `marketplace.json.txt`。

#### 第三步：安装并在 Codex 软件端载入

默认个人 Marketplace 会被 Codex 自动发现，不需要执行
`codex plugin marketplace add`：

```bash
codex plugin add research-engineering@personal
codex plugin list
```

`codex plugin list` 中应出现 `research-engineering@personal`，并显示为已安装。

##### macOS：Codex 桌面端

1. 完全退出并重新打开 ChatGPT 桌面应用；
2. 在顶部切换器中选择 **Codex**；
3. 打开 **Plugins** 或 **Plugins Directory**；
4. 选择 **Personal Plugins**，打开 **Research Engineering**；
5. 点击 **Install** 或 **Enable**。如果前面的 CLI 安装已成功，此处应显示
   **Installed**，只需确认插件处于开启状态；
6. 新建一个 **task**，不要继续复用安装前已经打开的 task；
7. 输入“请使用 Research Engineering 说明将采用的 Mode 和 Profiles”，确认
   新 task 能发现插件 Skills。

##### Windows：Codex 桌面端

必须先在 **Windows PowerShell** 中完成前两步，把 Marketplace 写到
`$env:USERPROFILE\.agents\plugins\marketplace.json`，再执行：

```powershell
codex plugin add research-engineering@personal
codex plugin list
```

随后完全退出并重新打开 Windows 上的 ChatGPT/Codex 应用，依次进入
**Codex → Plugins / Plugins Directory → Personal Plugins → Research
Engineering**，点击 **Install** 或 **Enable**，最后新建 task 验证。

Windows 桌面应用读取的是 Windows 用户目录。仅在 WSL 的
`~/.agents/plugins/marketplace.json` 中配置，通常不会自动出现在 Windows
桌面应用中；要给桌面应用安装，请使用上面的 PowerShell 路径。WSL 更适合
运行本项目的 Python、SSH 和 Slurm 工作流。

### 3.5 团队或仓库 Marketplace

团队维护者可以创建独立 Marketplace 根目录：

```text
marketplace-root/
├── .agents/plugins/marketplace.json
└── plugins/research-engineering/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    ├── skills/
    └── scripts/
```

这种非默认 Marketplace 需要显式注册：

```bash
codex plugin marketplace add /path/to/marketplace-root
codex plugin marketplace list
codex plugin add research-engineering@marketplace-name
```

Windows PowerShell 可将 `/path/to/marketplace-root` 换成类似
`C:\path\to\marketplace-root` 的真实路径。`source.path` 必须以 Marketplace
根目录为基准，并使用 `./plugins/research-engineering`。

### 3.6 在 Claude Code 中载入

本仓库以 Codex 为主要宿主，同时提供 `.claude-plugin/plugin.json` 兼容层。
Claude Code 会从插件根目录的 `skills/` 读取 Skills。这里使用官方的
`--plugin-dir` 开发加载方式；它只对本次启动的 Claude Code 会话生效，不等于
已经安装到 Claude Marketplace。

> Claude Code 是在终端中运行的 Agent。下面的操作不是 Claude Desktop
> 聊天应用的扩展安装流程。

#### macOS：Claude Code

如果已经按 Codex 步骤把仓库克隆到 `~/plugins/research-engineering`：

```bash
cd ~/plugins
claude --plugin-dir ./research-engineering
```

如果当前终端已经位于插件根目录，也可以执行：

```bash
claude --plugin-dir .
```

#### Windows：Claude Code

在 Windows PowerShell 中执行：

```powershell
Set-Location "$env:USERPROFILE\plugins"
claude --plugin-dir .\research-engineering
```

若在 WSL2 中运行 Claude Code，应使用 WSL 路径，而不是 Windows
`$env:USERPROFILE`：

```bash
cd ~/plugins
claude --plugin-dir ./research-engineering
```

#### 确认 Claude Code 已载入

进入 Claude Code 后：

1. 运行 `/help`，查找命名空间为 `research-engineering` 的 Skills；
2. 尝试 `/research-engineering:using-research-workflows`，或直接用自然语言要求
   Claude 使用 Research Engineering；
3. 如果没有发现插件，运行 `/plugin` 并查看 **Errors**；
4. 修改插件文件后运行 `/reload-plugins`，或退出后重新执行 `--plugin-dir` 命令。

Claude 的长期 Marketplace 安装、升级和公开发布使用另一套 Marketplace 清单
与分发流程，本版本尚未完成该端到端验收。不要把本节的本地临时加载表述为
“已经发布到 Claude Marketplace”。

### 3.7 安装后如何使用

插件通过自然语言任务触发，不需要导入 Python 模块。建议明确目标、模式、
Profile、执行环境和预算。例如：

```text
请使用 Research Engineering，以 experiment 模式和 ML Profile 检查这个
PyTorch 分类实验。先建立 .research 上下文和实验契约，只运行 CPU 单元测试，
不要下载数据、不要使用 GPU，也不要把一次 smoke test 当作科学结论。
```

```text
请使用 LLM + AI Infra Profiles 审查这个 vLLM benchmark。先做只读检查，
列出吞吐、P50/P95 延迟、峰值显存和正确性门槛；未经我授权不要启动远端任务。
```

插件可能在目标研究项目中创建 `.research/` 记录，但不会修改 Superpowers，
也不会因为安装动作自动提交集群作业或使用付费资源。

### 3.8 安装故障速查

| 现象 | 最可能原因 | 处理方式 |
|------|------------|----------|
| `codex --version` 报 `ENOENT` | npm 包中的平台二进制缺失 | 重新安装官方 CLI：`npm install --global @openai/codex` |
| 找不到个人 Marketplace | 文件名或用户目录错误 | 确认文件名是 `.agents/plugins/marketplace.json` |
| Marketplace 可见但插件不可见 | `source.path` 错误或目录多套一层 | 确认 `~/plugins/research-engineering/.codex-plugin/plugin.json` 存在 |
| Windows 辅助脚本拒绝安全写入 | 缺少所需 POSIX 文件原语 | 改在 WSL2 中运行，不要绕过安全检查 |
| Claude Code 中没有插件 Skills | 启动时未传入插件根目录，或 Manifest/Skill 有错误 | 用 `claude --plugin-dir <插件目录>` 重启，再用 `/plugin` 查看 Errors |
| 修改后行为未刷新 | 宿主仍在使用旧缓存 | 重新安装插件、重启宿主并创建新 task |

排查顺序应为：CLI 能否启动 → Marketplace JSON 是否有效 → 插件 Manifest
是否位于正确层级 → 插件是否安装 → 新 task 是否加载。不要直接修改 Codex
缓存目录。

## 4. 自动模式与用户覆盖

插件根据任务内容自动判定四种工作模式：

- **探索模式**：Notebook、原型、公式验证。最少上下文记录 + 静态检查 + 有界 Smoke Test；
- **实验模式**：正式训练、消融、Benchmark。要求实验契约、基线、配置记录、科学审查；
- **工程模式**：训练框架、分布式系统、推理服务、算子开发。要求隔离环境、实施计划、回归基线、工程审查；
- **发布模式**：论文开源、公开模型。要求完整复现记录、兼容性、独立复现审查。

Agent 在开始工作前会声明判定、原因和将启用的规则。用户可以手动指定模式、Profile、验证深度或流程例外，用户指令始终覆盖自动判断。

决策优先级为：当前任务中的明确用户指令 → `AGENTS.md` 等项目规则 →
插件自动分类与成本/风险判断 → Skill 默认行为。用户覆盖优先于插件自动
分类，但不能取消平台安全边界；涉及付费、共享集群或其他高成本资源时，
仍需符合已声明预算或取得明确授权。

## 5. 三个 Profile

Profile 是可按需组合加载的领域 Skill：

### ML Profile（`applying-ml-research-profile`）

覆盖 PyTorch 模型与传统深度学习实验：

- 数据划分、泄漏检查、采样与类别映射
- 张量形状、dtype、device 和广播
- 损失函数、指标与标签语义
- 梯度流、冻结策略和优化器参数组
- 随机种子、消融与统计稳定性
- 校准、类别不平衡和分布漂移

### LLM Profile（`applying-llm-research-profile`）

覆盖 Hugging Face、Accelerate、DeepSpeed/FSDP、PEFT/TRL、vLLM：

- Tokenizer、特殊 Token 和模板正确性
- 数据混合、截断、Packing 和 Label Mask
- 训练与评测数据污染检测
- 生成采样参数和评测可复现性
- PEFT、Checkpoint、权重合并和恢复兼容性
- 长上下文、KV Cache、量化与并行配置

### AI Infra Profile（`applying-ai-infra-profile`）

覆盖分布式训练、推理服务和 GPU 基础设施：

- 正确性优先于性能（数值一致性检查）
- GPU/节点拓扑与通信后端
- Warm-up、同步点、测量窗口和重复次数
- 吞吐、延迟分布、峰值显存、利用率和成本
- 数值一致性与精度权衡
- 故障恢复、抢占、Checkpoint 和作业重启

## 6. 本地、SSH、Slurm 与云端 GPU

插件支持四种执行环境和一种混合流程：

- **本地工作站**：直接执行，适合快速原型和小规模 Smoke Test；
- **SSH 远端**：通过用户已有的 SSH Host Alias 操作远端 GPU 工作站；
- **Slurm 集群**：通过 SSH 登录入口节点后提交和管理作业；
- **云端 GPU**：视为 SSH 远端环境，插件不创建、销毁或扩缩容云资源。
- **混合流程**：本地设计审查 → 远端执行 → 取回证据。

SSH 连接只使用用户已经配置的 Host Alias。连接前应确认 Alias、精确远端
仓库路径、代码同步方式和允许的操作，例如用户明确要求后才使用
`ssh gpu-lab`；不会创建密钥、读取私钥或静默修改 SSH 配置。精确 Alias 与
远端路径可写入 `.research/local/connections.json`，该目录默认忽略。SSH
断开后先重新查询远端进程或 Slurm 状态，不把连接中断直接判为作业失败。

## 7. .research/ 目录

插件在项目根目录按需创建轻量元数据目录：

```text
.research/
├── .gitignore          # 排除 local/
├── context.md          # 项目目标、Profile、环境、预算
├── experiments/        # 实验契约（假设、基线、变量、指标、判据）
├── runs/               # 运行记录（Git 提交、环境指纹、退出状态）
├── reviews/            # 审查报告（科学/工程/复现审查）
├── local/              # 本地连接细节（默认被 .gitignore 排除）
└── progress.md         # 进度账本（长任务恢复不依赖聊天记忆）
```

- `context.md` 记录模式、Profile、environment_id、预算等全局约束；
- 实验契约定量定义假设、变量、指标和结论判据；
- 运行记录包含本地和远端 Git 提交、Python/PyTorch/CUDA/GPU/NCCL 版本、退出状态和失败分类；
- `local/` 保存 SSH Host Alias 和远端路径，不在版本控制中共享；
- 其余轻量元数据可进入版本控制。

## 8. 成本与授权

Agent 可自主执行：

- 静态检查、单元测试、CPU 验证
- 已有预算范围内、时间有上限的本地或单卡 Smoke Test

未预设预算时的默认上限：不产生付费资源、不提交调度器作业、不下载大型资产，且预计能在当前可用 GPU 或 CPU 上于 10 分钟内完成。

**需要用户授权**的操作：

- 下载大型数据集或模型
- 长时间训练、多 GPU/多节点任务
- 提交 Slurm 作业
- 使用付费云资源
- 可能显著占用共享资源的 Benchmark

用户可预设时间、GPU、节点或费用预算。预算内无需逐次确认；达到预算后停止新任务，保存状态并报告尚缺证据。

## 9. 多 Agent

根据模式和风险自动分配角色：

| 模式 | 角色 |
|------|------|
| 探索 | 单 Agent |
| 实验 | Implementer + Scientific Reviewer |
| 工程 | Implementer + Engineering Reviewer |
| 工程（涉及算法语义） | + Scientific Reviewer |
| 发布 | + Reproducibility Reviewer |

- 共享工作区的写任务默认串行；独立只读调查可并行；
- 原生 Multi-Agent 不可用时先遵守用户显式要求停止或采用安全降级的指令；
  用户未指定降级偏好时才退化为单 Agent 分阶段自检，并明确审查独立性降低；
- Reviewer 必须独立判断，不能把 Implementer 自述视为证明。

## 10. 五个辅助脚本

所有脚本使用 Python 标准库优先，保持无状态、可测试、幂等。

| 脚本 | 功能 |
|------|------|
| `init_research_state.py` | 初始化 `.research/` 目录和模板，不覆盖已有文件 |
| `capture_environment.py` | 采集本地或 SSH 远端的 Git、Python、PyTorch、CUDA、GPU 等环境摘要，输出结构化 JSON |
| `record_run.py` | 创建或更新运行记录，校验必需字段，保留已有未知字段 |
| `inspect_slurm_job.py` | 解析 `squeue`/`sacct` 输出，记录 Job 状态、退出原因和资源使用 |
| `summarize_evidence.py` | 汇总代码验证、运行状态、研究结论、缺失证据和剩余风险 |

## 11. 完整示例

以下 quick start 使用 `examples/minimal-project/` 中的**合成示例**，用于展示
记录格式和证据边界；它不表示本仓库真的执行过训练。

**1. 发出实验请求**

> 请在本地 CPU 上实现并验证一个置信度门控。先做不超过 20 步的 Smoke
> Test，不运行完整训练；目标是减少误报，同时避免召回率明显下降。

**2. Router 先显式声明自动判定**

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

这只是路由声明，不代表插件已经安装，也不会自动开始运行。用户可以在执行
前覆盖模式、Profile 或验证深度。

**3. 初始化轻量研究状态**

```bash
python3 /path/to/research-engineering/scripts/init_research_state.py --root .
```

初始化器只创建缺失的 `.research/` 目录与模板，不覆盖已有文件。随后在
`experiments/demo.md` 中记录 `demo-confidence-gate` 的假设、基线、数据
划分、指标和成功/失败/不确定判据。

**4. 经确认后运行并记录本地 Smoke Test**

```bash
python train.py --config configs/demo.yaml --max-steps 20 --seed 7
```

对应的合成计划记录位于 `.research/runs/demo-smoke.json`。它只展示待运行命令
和记录格式，不是一次已完成执行；核心字段为：

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

Scientific Reviewer 可把设计审查写入
`.research/reviews/demo-scientific.md`。`PASS` 只表示该审查未发现阻塞项，
不能把单种子 Smoke Test 提升为研究结论。

**5. 输出最终三态证据报告**

```text
Code verification: not_verified — 尚未执行确定性、回归或 Smoke 验证。
Experiment execution: not_verified — 正式多种子实验与阈值扫描尚未执行。
Conclusion support: not_verified — 尚无效应量、统计比较或基线证据。
```

下一步应执行预先定义的完整实验与统计比较；在此之前不得声称置信度门控
改善了模型质量。

## 12. 安全与隐私

- 不读取、保存或复制 SSH 私钥；
- 不在命令、日志或 `.research/` 中写入密码、Token 或 API Key；
- 不静默修改 SSH 配置或系统文件；
- `.research/local/` 默认被 `.gitignore` 排除，不会进入版本控制；
- 可共享的运行记录使用用户定义的 `environment_id`，不写入精确主机名或绝对路径（除非用户明确要求）。

## 13. 测试

```bash
# 运行所有测试
python3 -m unittest discover -s tests -v

# 运行插件结构验证
python3 /path/to/validate_plugin.py .
```

最近一次公开发布准备在 macOS 上运行了 **127 个离线自动化测试**。这里的
“127 项”是 `unittest` 收集到的测试用例数，不是 127 次 GPU 训练或 127 个
真实研究实验。它们覆盖：

- 插件 Manifest、Marketplace 安装文档和目录结构契约；
- 11 个 Skills 的 Frontmatter、名称、路由和必需语义；
- 五个辅助脚本的正常输入、非法输入、幂等性和安全边界；
- Slurm 输出解析，但使用的是固定样例，不连接真实集群；
- 最小示例的 `.research/` 结构、实验契约和本地连接排除；
- Smoke、代码验证、实验执行和科学结论三者必须分离；
- 行为评估固件中的 baseline/skilled 证据和预期差异。

因此，`127/127` 只说明这套离线契约在当时全部通过。它不等于真实 GPU、
SSH、Slurm、云 GPU 或 Marketplace 安装已经成功，也不支持任何模型效果、
吞吐提升或科学优越性结论。Linux、Windows/WSL2 和真实基础设施仍应分别
记录验收结果。

## 14. 更新与卸载

**更新**：先备份并阅读新版说明，再更新个人插件目录。

macOS、Linux 或 WSL：

```bash
cd ~/plugins/research-engineering
git pull --ff-only
codex plugin add research-engineering@personal
```

Windows PowerShell：

```powershell
Set-Location "$env:USERPROFILE\plugins\research-engineering"
git pull --ff-only
codex plugin add research-engineering@personal
```

正式发布必须更新 `.codex-plugin/plugin.json` 的语义化版本。开发者若需要在
不改正式版本号的情况下刷新本地缓存，可以使用 `plugin-creator` 提供的
`update_plugin_cachebuster.py`；公开 Release 不应使用本地 cachebuster 版本。

更新后请重新打开宿主并新建一个新 task。插件不会自行更新或迁移研究项目中
的 `.research/`；跨版本使用前应检查格式变化。

Claude Code 使用 `--plugin-dir` 的用户更新源码后，可在现有 Claude Code 会话
运行 `/reload-plugins`；若仍未刷新，退出会话并按第 3.6 节重新启动。

**卸载**：

```bash
codex plugin remove research-engineering@personal
```

卸载后可以自行决定是否保留插件源码和个人 Marketplace 条目。不要删除整个
个人 Marketplace 文件，因为其中可能还有其他插件。卸载插件不会删除研究
项目中的 `.research/`；只有确认研究记录不再需要时才应单独处理它。

## 15. 公开发布检查

发布源码或 Release 前至少检查：

- 工作树中没有 `.env`、凭据、主机名、个人绝对路径或本地连接配置；
- `.research/local/`、ZIP、`dist/`、`tmp/` 和操作系统临时文件未进入提交；
- `.codex-plugin/plugin.json` 的版本、作者显示名、许可证和描述适合公开；
- `.claude-plugin/plugin.json` 与 Codex Manifest 的名称、版本和许可证一致；
- `python3 -m unittest discover -s tests -v` 与插件验证器通过；
- `git archive` 生成的 ZIP 不包含内部计划、私有报告或 Git 元数据；
- 发布说明明确区分离线测试、真实环境执行和科学结论证据。

首次发布前还应把 README 中的 `OWNER/REPOSITORY` 替换为真实公开仓库地址。

删除当前版本中的敏感文件不会自动清除旧提交。公开完整 Git 历史前，应使用
`git log --all --format='%h %an <%ae>'` 审查作者身份，并检查历史提交是否包含
敏感路径或凭据。如果历史不适合公开，优先从已审计的源码树创建干净的公开
仓库或经过确认的压缩历史；不要在未备份时直接重写并强制推送现有历史。
