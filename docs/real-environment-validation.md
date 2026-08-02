# 真实环境验收边界与后续计划

更新日期：2026-08-03

## 当前结论

`research-engineering` 0.1.0 已完成插件结构、Skills 路由、辅助脚本、行为证据、
打包规则和安全检查，可进入受控试用。macOS 上已观察到本地 Codex
Marketplace 条目处于 installed/enabled 状态。

当前状态应表述为：**已完成离线构建与自动化验证，以及一次 macOS 本地 Codex
安装状态核对；尚未完成公开 Marketplace、Claude Marketplace、Windows、真实
GPU、SSH、Slurm 和云 GPU 的端到端验收。** 这不代表插件主体不完整，但意味
着不能宣称已经兼容所有宿主和基础设施组合。

## 已验证范围

- 8 个共享核心 Skills 和 3 个可组合研究 Profile；
- 自动识别 exploration、experiment、engineering、release 成熟度，且用户明确指令优先；
- PyTorch 优先的 ML、LLM 与 AI Infra 工作流；
- `.research/` 初始化、环境捕获、运行记录、Slurm 检查和证据汇总；
- 确定性测试、有限冒烟测试、回归证据和科学结论证据分层；
- SSH 只读优先、远程路径确认、同步方式确认和高风险操作审批；
- 127 项离线自动化测试、11 个 Skill 校验、插件校验、行为评估和独立审查；
- Git 导出和 ZIP 排除规则；
- macOS 本地 Codex 安装条目的 installed/enabled 状态。

Claude 兼容 Manifest 已做结构校验，但尚未把结构校验表述为 Claude Code 或
Claude Marketplace 的真实安装成功。

## 尚未执行的原因

1. 真实 GPU、云 GPU、长时间训练和多 GPU/Slurm 作业可能产生明显算力成本；按照插件的安全策略，必须先取得用户授权或预算。
2. SSH 端到端测试需要真实主机、认证方式、远程项目路径和既有同步机制，插件不会记录或代管凭据。
3. Slurm 的账号、分区、模块系统、资源限制和提交规范依赖具体集群，不能用通用本地模拟替代。
4. 公开 Marketplace 发布会改变外部状态；当前授权范围仅包含本地文件整理、
   离线验证和公开发布准备。
5. Windows 原生、WSL2 和 Claude Code 需要独立环境，不能由 macOS Codex 的
   结果代替。

## 对实际使用的影响

| 使用场景 | 当前风险 | 说明 |
| --- | --- | --- |
| 本地研究规划、代码审查、实验设计 | 低 | 核心路由和工作流已经自动化验证 |
| 本地 CPU/PyTorch 小实验 | 低 | 建议安装后执行一次冒烟测试 |
| CUDA/GPU 训练 | 中 | 仍需确认驱动、CUDA、PyTorch 和扩展版本组合 |
| SSH 远程开发 | 中 | 仍需确认认证、同步方式和远程路径 |
| Slurm 集群 | 中 | 仍需适配具体集群策略并验证最小作业 |
| 云 GPU | 中 | 仍需确认供应商、镜像、存储、网络和权限 |
| macOS 本地 Codex | 低 | 已观察安装并启用；仍应在新 task 中做代表性行为验收 |
| Windows Codex | 中 | 用户目录、PowerShell 和桌面端载入尚未实机验收 |
| Claude Code 本地加载 | 中 | 已提供兼容清单和命令，尚未实机验收 |
| 公开 Marketplace 分发 | 中 | 一键安装、升级、卸载和公开发布尚未验收 |

## 推荐验收顺序

1. 在 macOS Codex 新 task 中确认 11 个 Skills 可发现并执行路由样例。
2. 分别在 Windows Codex、macOS Claude Code 和 Windows Claude Code 中验证载入、
   更新和卸载流程。
3. 在本地或远程主机运行几分钟、无需大规模下载的单 GPU 冒烟实验。
4. 以只读方式连接 SSH，验证环境捕获、远程路径发现和同步计划。
5. 检查 Slurm 环境与脚本，不提交作业。
6. 经用户明确授权后提交一个最小、限时、限资源的 Slurm 作业。
7. 如需公开分发，再执行公开 Marketplace 安装、升级、卸载和发布验收。

## 操作门禁

以下动作必须获得用户明确授权，或遵守用户预先给定的预算与资源上限：

- 下载大型模型或数据集；
- 启动长时间训练、多个种子实验或多 GPU 作业；
- 提交 Slurm 作业；
- 创建或使用付费云资源；
- 覆盖或删除远程文件；
- 安装、发布、升级或卸载 Marketplace 插件。

每次真实环境验收应记录环境、命令、资源上限、运行 ID、结果、失败证据和结论适用范围。单次冒烟测试不能作为模型或方法优越性的科学证据。
