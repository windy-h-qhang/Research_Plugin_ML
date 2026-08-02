# Applying AI Infrastructure Profile — Skilled Results

Fresh evaluators received the current Skill inline before one prompt. They
received no rubric or expected answer and had no access to tools, files, the
workspace, browsing, or delegation. All completed responses are verbatim.

Transport whitespace note: four responses arrived with Markdown hard-break
trailing spaces. Those trailing spaces alone were removed for repository diff
hygiene. All non-whitespace text tokens, paragraph order, identities, evidence,
and scores are unchanged; no response semantics were edited.

## Iteration 1 — failed and superseded

Iteration 1 stopped after the first primary repetition because a blocking
failure requires a minimal Skill revision and a complete fresh-context restart
of both prompts.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill_1`

#### Observed response

> Do not approve it.
>
> The result is invalid as a performance comparison: it changes batch size and GPU topology, lacks warm-up, and uses unsynchronized async timing. One run also cannot establish an 18% improvement.
>
> Require same-precision correctness against a reproducible baseline, fixed workload/topology, synchronized repeated measurements with latency distribution, and reporting of throughput, p50/p95/p99/max latency, peak memory, utilization, failures, and cost.

#### Rubric

- PASS — requires same-precision correctness against a trusted reproducible
  baseline before the speed claim can be approved.
- PASS — says changed batch size and GPU topology invalidate the comparison.
- PASS — flags missing warm-up and unsynchronized timing as errors and requires
  synchronized measurement.
- PASS — rejects one run and requires a fixed workload, repetitions, and a
  latency distribution.
- FAIL — requires precision and topology to be fixed but omits the parallel
  strategy and does not explicitly require all three to be documented.
- PASS — requires throughput, p50/p95/p99/max latency, peak memory,
  utilization, failures, and cost.
- FAIL — requires a reproducible baseline but does not identify it as a
  documented baseline commit.

#### Verdict

FAIL — 5/7 blocking groups passed.

### Iteration 1 aggregate

- Primary: 5/7; 0/1 complete.
- Counter-example: not run after the blocking primary failure.
- Status: failed and superseded; the response is retained and is not part of
  the final arm.
- Excluded or replaced samples: none.

## Iteration 2 — final GREEN arm

After the minimal revision, both prompts restarted from zero in entirely new
fresh contexts.

### Primary repetition 1

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill2_1`

#### Observed response

> 不批准该 benchmark。18% 单次结果不可用：批量大小、GPU 拓扑均不同，且没有预热与 CUDA 同步，比较存在关键混杂和异步计时误差。
>
> 1. 尚未在相同精度下对可信基线证明数值与功能正确性。
> 2. 工作负载形状（含 batch size）和硬件/网络拓扑未保持一致，比较无效。
> 3. 未预热，且测量边界没有显式 CUDA synchronization；异步计时不能代表真实运行时间。
> 4. 只有一次运行，未进行受控重复，也没有延迟分布。
> 5. 未完整记录并固定精度、并行策略、拓扑；还应记录 GPU/CPU 型号与数量、互连/NUMA、软件栈、工作负载维度、测量窗口和重复次数。
> 6. 未报告吞吐量、p50/p95/p99/最大延迟、峰值显存、GPU 利用率、失败情况和估算成本。
> 7. 未明确可复现的基线 commit，也未证明该基线通过相同的正确性检查。
>
> 应在相同 batch size、相同拓扑与固定配置下，先完成正确性验证，再预热、同步计时并多次重复后重新评估。

#### Rubric

- PASS — requires numerical and functional correctness against a trusted
  same-precision baseline before approval.
- PASS — says batch-size and topology differences invalidate the comparison.
- PASS — identifies missing warm-up and CUDA synchronization as measurement
  errors.
- PASS — requires controlled repetitions and a latency distribution.
- PASS — explicitly requires precision, parallel strategy, and topology to be
  recorded and fixed.
- PASS — requires throughput, p50/p95/p99/max latency, peak memory, utilization,
  failures, and estimated cost.
- PASS — requires an explicit reproducible baseline commit passing the same
  correctness checks.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 2

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill2_2`

#### Observed response

> 不批准该基准结论。“单次快 18%”在当前条件下没有可比性：批大小和 GPU 拓扑均不同，且没有预热、未在 CUDA 计时边界同步，异步计时只能反映排队时间。
>
> 必须满足以下七项后才能批准性能声明：
>
> 1. 同一精度下先对照可信基线证明数值与功能正确性。
> 2. 固定工作负载形状（含 batch size）及硬件/网络拓扑。
> 3. 计时前预热，并在测量边界显式 CUDA 同步。
> 4. 在受控工作负载下多次重复，报告延迟分布而非单点。
> 5. 固定并记录精度、并行策略、拓扑，以及 GPU/CPU 型号和数量、互连/NUMA、软件栈、工作负载维度、测量窗口、重复次数。
> 6. 报告吞吐、p50/p95/p99/max 延迟、峰值 GPU 内存、GPU 利用率、失败情况与估算成本。
> 7. 明确可复现的基线提交，并要求其通过同样的正确性检查。
>
> 因此，当前结果最多是待验证的观察，不能作为“vLLM/Triton 路径快 18%”的批准结论。

#### Rubric

- PASS — correctness is required first against a same-precision trusted
  baseline.
- PASS — workload shape, batch size, and topology must be held constant.
- PASS — warm-up and explicit CUDA synchronization are required.
- PASS — controlled repetitions and latency distribution are required.
- PASS — precision, parallel strategy, and topology must all be fixed and
  recorded.
- PASS — every required throughput, latency, memory, utilization, failure, and
  cost measure is requested.
- PASS — explicitly requires a reproducible baseline commit with the same
  correctness checks.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 3

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill2_3`

#### Observed response

> 不批准。该“18% 更快”结果存在关键混杂因素，不能作为性能结论：
>
> 1. 尚未证明与可信基线在相同精度下的数值与功能正确性。
> 2. 批大小和 GPU 拓扑不同，工作负载形状与硬件/网络条件未保持一致，比较无效。
> 3. 未预热，且异步计时没有 CUDA 同步；测到的可能只是排队时间。
> 4. 仅一次运行，必须在受控负载下多次重复并报告延迟分布。
> 5. 必须明确并固定精度、并行策略、拓扑；记录 GPU/CPU 型号与数量、互连/NUMA、软件栈、工作负载维度、测量窗口和重复次数。
> 6. 必须报告吞吐量、p50/p95/p99/最大延迟、峰值 GPU 显存、GPU 利用率、失败情况和估算成本。
> 7. 必须明确可复现的基线提交，并要求它通过同样的正确性检查。
>
> 请在相同批大小与拓扑下完成预热、同步计时和重复测试后，再评估 vLLM/Triton 路径是否确实更快。

#### Rubric

- PASS — requires same-precision numerical and functional correctness first.
- PASS — identifies batch size and topology as invalidating confounds.
- PASS — identifies missing warm-up and CUDA synchronization.
- PASS — requires controlled repetitions and latency distribution.
- PASS — explicitly fixes and records precision, parallel strategy, and
  topology.
- PASS — requests all required performance, resource, failure, and cost
  measures.
- PASS — explicitly requires a reproducible baseline commit passing the same
  checks.

#### Verdict

PASS — 7/7 blocking groups passed.

### Excluded primary attempt

Agent `/root/task_18_replacement/t18_p_skill2_4` remained running beyond the
normal single-sample time limit and returned no response. It was interrupted
and excluded before scoring. The fresh replacement below is the fourth formal
primary repetition.

### Primary repetition 4

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill2_4r`

#### Observed response

> 不批准。该结果目前不能证明“快 18%”：批量大小和 GPU 拓扑均不同，且未预热、没有 CUDA 同步，单次异步计时只可能测到排队时间。
>
> 七项审批检查均未满足或未提供证据：
>
> 1. 未证明与可信基线在相同精度下的数值与功能正确性。
> 2. 工作负载形状（batch size）和硬件/网络拓扑不一致，比较存在混杂因素。
> 3. 未预热，且测量边界未显式 CUDA synchronization。
> 4. 只有一次运行，未报告多次受控重复的延迟分布。
> 5. 未完整记录并固定精度、并行策略、拓扑，以及软硬件和工作负载配置。
> 6. 未报告吞吐、p50/p95/p99/max 延迟、峰值显存、GPU 利用率、失败情况和成本。
> 7. 未给出可复现的基线提交，并证明基线通过同样的正确性检查。
>
> 请在相同 batch size、相同拓扑和固定配置下，先做正确性校验，再预热并同步计时，进行多次重复后重新提交基准结果。

#### Rubric

- PASS — requires same-precision numerical and functional correctness first.
- PASS — flags batch size and topology as confounds.
- PASS — requires warm-up and explicit CUDA synchronization.
- PASS — requires controlled repetitions and a latency distribution.
- PASS — explicitly requires precision, parallel strategy, and topology to be
  recorded and fixed.
- PASS — requests throughput, all latency percentiles, peak memory,
  utilization, failures, and cost.
- PASS — requires a reproducible baseline commit passing the same correctness
  checks.

#### Verdict

PASS — 7/7 blocking groups passed.

### Primary repetition 5

#### Case

Primary prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_p_skill2_5`

#### Observed response

> 不批准该性能基准。
>
> 1. 尚未在同精度下对可信基线证明数值与功能正确性。
> 2. 批量大小和 GPU 拓扑不同，比较存在混杂因素，结果无效。
> 3. 未预热且未在计时边界进行 CUDA 同步；异步计时只反映排队时间。
> 4. 只有一次运行，未在受控负载下重复，也没有延迟分布。
> 5. 未完整固定并记录精度、并行策略与拓扑；还需记录 GPU/CPU 型号和数量、互连/NUMA、软件栈、工作负载维度、测量窗口和重复次数。
> 6. 未报告吞吐量、p50/p95/p99/最大延迟、峰值 GPU 内存、GPU 利用率、失败情况和估算成本。
> 7. 未提供可复现、已记录提交的基线，且基线也必须通过相同的正确性检查。
>
> “快 18%”只能算待验证的初步信号。请在相同 batch size、相同硬件/网络拓扑下，完成预热、CUDA 同步、多次重复和完整指标报告后再评审。

#### Rubric

- PASS — requires same-precision numerical and functional correctness first.
- PASS — says batch size and topology differences invalidate the result.
- PASS — identifies warm-up and synchronization measurement errors.
- PASS — requires controlled repetitions and latency distribution.
- PASS — explicitly requires precision, parallel strategy, and topology to be
  fixed and recorded.
- PASS — requests the complete required metric set.
- PASS — explicitly requires a recorded reproducible baseline commit with the
  same correctness checks.

#### Verdict

PASS — 7/7 blocking groups passed.

### Counter-example repetition 1

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_c_skill2_1`

#### Observed response

> 这是固定基础设施上的模型质量实验，应以 ML Research Profile 为主，不应引入吞吐、CUDA 同步、拓扑、成本或韧性测试作为结论门槛。
>
> 要判断新损失是否提升 balanced accuracy：
>
> - 使用相同数据划分、模型、训练预算、增强、优化器和评估流程。
> - 与明确版本化的基线损失比较，至少多随机种子重复训练。
> - 报告各次 balanced accuracy、均值、标准差/置信区间，以及每类召回率与混淆矩阵。
> - 用配对比较或合适的显著性/置信区间分析，确认改进不只是随机波动。
> - 同时检查总体准确率、校准和少数类表现，避免 balanced accuracy 的提升来自不可接受的副作用。
> - 若改进在预先规定的多种子标准下稳定复现，才可声称该损失改善 balanced accuracy；否则应表述为初步信号。

#### Rubric

- PASS — explicitly selects the ML Research Profile instead of the AI
  Infrastructure Profile.
- PASS — explicitly rejects throughput, synchronization, and topology checks.
- PASS — avoids batch-size, resilience, and cost-reporting ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 2

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_c_skill2_2`

#### Observed response

> 这是固定基础设施上的模型质量实验，应以 ML Research Profile 为主，不适用基础设施性能审批流程。
>
> 评审应聚焦：使用相同数据划分、训练预算、随机种子策略和评估阈值，对比新损失与明确的基线损失；报告各类别准确率、混淆矩阵、balanced accuracy 的均值与不确定性，并在独立测试集上验证。还应检查是否牺牲了总体准确率、少数类召回率或校准表现，并做消融以确认提升来自该损失本身。
>
> 在未提供可复现实验结果前，不能批准“提升 balanced accuracy”的结论。

#### Rubric

- PASS — explicitly routes to the ML Research Profile and says the
  infrastructure approval process does not apply.
- PASS — applies no warm-up, CUDA synchronization, topology, or throughput
  checks.
- PASS — avoids batch-size, resilience, and cost-reporting ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 3

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_c_skill2_3`

#### Observed response

> 不应使用 AI 基础设施 Profile 作为主审查框架：这是固定基础设施上的模型质量实验，应以 ML Research Profile 为主。
>
> 审查重点应是：
>
> - 固定数据划分、模型、训练预算、随机种子与评估流程；
> - 与明确基线损失函数进行公平对照；
> - 报告多随机种子的 balanced accuracy 分布、均值与不确定性；
> - 检查类别不平衡处理、阈值选择和是否存在验证/测试集泄漏；
> - 做消融实验，证明提升来自该损失而非权重、采样或训练配置变化；
> - 将结论限定为所测数据集与设置，避免泛化或性能承诺。

#### Rubric

- PASS — explicitly makes ML primary and rejects the AI Infrastructure Profile.
- PASS — imposes none of the infrastructure benchmark checks.
- PASS — avoids batch-size, resilience, and cost-reporting ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 4

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_c_skill2_4`

#### Observed response

> 这是固定基础设施上的模型质量实验，**应以 ML Research Profile 为主，不适用 AI Infrastructure Profile 的性能审批流程**。
>
> 评审要点：
>
> - 使用相同的数据划分、图像预处理、模型初始化策略、训练步数与超参数，比较新损失和基线损失。
> - 指标以验证/测试集的 balanced accuracy 为主，同时报告每类召回率、混淆矩阵和总体准确率，避免少数类别改善被掩盖。
> - 使用多个随机种子，报告均值、标准差与置信区间；不要凭单次训练结果宣称改进。
> - 保留可复现的基线提交、配置、数据版本和评估脚本；确认新损失没有实现错误或数据泄漏。
> - 若提升仅出现在训练集、个别种子或阈值调参后，结论应为“不足以证明改进”。
>
> 结论标准：只有当新损失在独立测试集上跨多个种子稳定提高 balanced accuracy，且没有显著损害关键类别召回或其他预先定义的约束指标时，才可认为其改善了分类效果。

#### Rubric

- PASS — explicitly selects ML and rejects the AI Infrastructure approval
  process.
- PASS — does not apply infrastructure timing, topology, or throughput checks.
- PASS — avoids batch-size, resilience, and cost-reporting ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Counter-example repetition 5

#### Case

Counter-example prompt.

#### Context

Fresh skilled context. Agent:
`/root/task_18_replacement/t18_c_skill2_5`

#### Observed response

> 这是固定基础设施上的模型质量实验，应以 **ML Research Profile** 为主，不适用 AI 基础设施性能审批流程。
>
> 结论：仅凭“新损失函数提升了 balanced accuracy”的说法不能批准。应在相同数据划分、随机种子集合、训练预算、模型与超参数搜索预算下，与明确基线做多次独立训练；报告各次 balanced accuracy、均值/置信区间或配对统计检验，并按类别检查收益是否真实改善了少数类表现。还应排除数据泄漏、阈值调优只偏向新方法、以及挑选最佳 seed 的影响。
>
> 无需加入 CUDA warm-up、同步计时、拓扑、吞吐、显存、成本或容错测试；这些不会证明损失函数的 balanced accuracy 改进。

#### Rubric

- PASS — explicitly selects the ML Research Profile and says the AI
  Infrastructure process does not apply.
- PASS — explicitly rejects warm-up, synchronization, topology, and throughput
  checks.
- PASS — avoids batch-size controls and rejects cost and resilience ceremony.

#### Verdict

PASS — 3/3 blocking groups passed.

### Iteration 2 aggregate

- Primary: 7/7, 7/7, 7/7, 7/7, 7/7 = 35/35; 5/5 complete.
- Counter-example: 3/3, 3/3, 3/3, 3/3, 3/3 = 15/15; 5/5 complete.
- Total: 50/50; 10/10 complete.
- Excluded samples: one primary timeout with no response, identified above,
  followed by one fresh replacement.
- Status: GREEN. Every blocking group passed in all ten formal final
  repetitions.
