# Applying AI Infrastructure Profile — Baseline Results

Five fresh evaluators answered each prompt without the Skill. The evaluators
received one prompt, no rubric or expected answer, and no access to tools,
files, the workspace, browsing, or delegation. All completed responses are
verbatim.

## Primary repetition 1

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_p_ctrl_1`

### Observed response

> 不批准。
>
> 这次结果同时改变了 batch size、预热、计时同步方式和 GPU 拓扑，18% 差异无法归因于新路径。应在相同硬件拓扑、模型/精度、batch 与并发、请求集、预热次数下，使用 CUDA 同步的端到端计时，至少多次重复并报告均值、方差及吞吐/延迟分位数后再评审。

### Rubric

- FAIL — rejects approval because of confounds, but does not require numerical
  or functional correctness before any speed claim.
- PASS — identifies the changed batch size and GPU topology as confounds that
  prevent attribution to the new path.
- PASS — requires warm-up and CUDA-synchronized timing in response to both
  measurement errors.
- PASS — requires a matched batch, concurrency, and request set, multiple
  repetitions, and latency percentiles.
- FAIL — holds precision and topology constant, but does not require the
  parallel strategy to be documented and held constant.
- FAIL — requests throughput and latency percentiles, but omits peak memory,
  utilization, and cost.
- FAIL — does not require a documented reproducible regression baseline commit.

### Verdict

FAIL — 3/7 blocking groups passed.

## Primary repetition 2

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_p_ctrl_2`

### Observed response

> 不批准。该结果存在批量大小、预热、计时同步和 GPU 拓扑等关键混杂因素，不能归因于新路径或证明 18% 提升。
>
> 应在相同硬件与拓扑、相同模型/输入/批量设置下，充分预热，并以 CUDA 同步的端到端计时进行多次重复测试，报告均值、方差及吞吐和延迟后再评审。

### Rubric

- FAIL — rejects the benchmark as confounded, but does not require numerical or
  functional correctness before a performance claim.
- PASS — explicitly identifies both changed batch size and topology as
  attribution-breaking confounds.
- PASS — requires sufficient warm-up and CUDA-synchronized timing.
- FAIL — requires controlled inputs and multiple repetitions, but asks only for
  generic latency rather than a latency distribution.
- FAIL — does not require precision and parallel strategy to be documented and
  held constant.
- FAIL — asks for throughput and latency, but omits latency distribution, peak
  memory, utilization, and cost.
- FAIL — does not require a documented reproducible regression baseline commit.

### Verdict

FAIL — 2/7 blocking groups passed.

## Primary repetition 3

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_p_ctrl_3`

### Observed response

> 不批准。
>
> 这次结果无法归因于 vLLM/Triton 路径：batch size、预热、计时同步方式和 GPU 拓扑都同时改变，18% 很可能来自这些混杂因素。
>
> 需在相同硬件拓扑、模型/精度、数据、batch size 和并发条件下，加入充分 warm-up，并在计时边界做 CUDA 同步；多次重复后报告均值、方差/置信区间及端到端与稳态吞吐。这样才可评估是否真实提升。

### Rubric

- FAIL — rejects causal attribution, but does not require numerical or
  functional correctness before speed.
- PASS — flags both batch size and GPU topology as confounds.
- PASS — requires warm-up and synchronization at CUDA timing boundaries.
- FAIL — controls workload and requires repeated trials, but does not require a
  latency distribution.
- FAIL — holds precision and topology constant, but omits the documented,
  constant parallel strategy.
- FAIL — reports throughput and variation, but omits latency distribution, peak
  memory, utilization, and cost.
- FAIL — does not require a documented reproducible regression baseline commit.

### Verdict

FAIL — 2/7 blocking groups passed.

## Primary repetition 4

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_p_ctrl_4`

### Observed response

> I would not approve it.
>
> The 18% result is confounded by batch size, warm-up, asynchronous timing without CUDA synchronization, and GPU topology. It is not an apples-to-apples comparison.
>
> Re-run both paths with identical hardware/topology, model and precision, batch/input mix, warm-up, concurrency, and measurement window; synchronize CUDA (or use a correct end-to-end latency method); report repeated trials with throughput and latency percentiles.

### Rubric

- FAIL — rejects the comparison as invalid, but does not require numerical or
  functional correctness before the speed claim.
- PASS — flags changed batch size and topology as invalidating confounds.
- PASS — flags both absent warm-up and unsynchronized asynchronous timing and
  requires their correction.
- PASS — controls batch/input mix and measurement window, requires repeated
  trials, and requests latency percentiles.
- FAIL — holds precision and topology constant, but does not document or hold
  the parallel strategy constant.
- FAIL — requests throughput and latency percentiles, but omits peak memory,
  utilization, and cost.
- FAIL — does not require a documented reproducible regression baseline commit.

### Verdict

FAIL — 3/7 blocking groups passed.

## Excluded primary attempt

Agent `/root/task_18_replacement/t18_p_ctrl_5` returned only a transport error:
`stream disconnected before completion`. It produced no complete response and
was excluded before scoring. The fresh replacement below is the fifth formal
primary repetition.

## Primary repetition 5

### Case

Primary prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_p_ctrl_5r`

### Observed response

> Do not approve it.
>
> The 18% result is confounded by batch size, warm-up omission, asynchronous timing without CUDA synchronization, and different GPU topology. It does not establish that the new vLLM/Triton path caused the improvement.
>
> Re-run with identical workload/batch size, warm-up, synchronized timing, same hardware/topology and software settings, multiple trials, and report latency/throughput distributions plus variance.

### Rubric

- FAIL — rejects causal attribution, but does not require numerical or
  functional correctness before speed.
- PASS — identifies batch size and topology as confounds.
- PASS — identifies missing warm-up and synchronization and requires both.
- PASS — requires an identical workload, multiple trials, and latency
  distributions.
- FAIL — holds topology constant but does not require precision and parallel
  strategy to be documented and held constant.
- FAIL — asks for latency and throughput distributions, but omits peak memory,
  utilization, and cost.
- FAIL — does not require a documented reproducible regression baseline commit.

### Verdict

FAIL — 3/7 blocking groups passed.

## Counter-example repetition 1

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_c_ctrl_1`

### Observed response

> To assess whether the new loss improves balanced accuracy under fixed infrastructure:
>
> - Keep the model architecture, data splits, preprocessing, augmentation, optimizer, schedule, batch size, training budget, seed set, and evaluation code identical.
> - Compare only the baseline loss against the new loss across multiple fixed random seeds.
> - Report per-seed balanced accuracy, mean ± standard deviation, paired per-seed differences, and confidence intervals.
> - Use a paired statistical test appropriate to the same seed/split setup (for example, paired bootstrap over test predictions or a paired test over seed-level results).
> - Check class-wise recall and confusion matrices to confirm the gain is not hiding degradation in an important class.
> - Include training stability, convergence behavior, and compute/runtime as secondary outcomes.
> - Predefine the primary metric, comparison, and acceptance threshold before running experiments.
>
> Conclusion should be conditional: claim improvement only if the new loss shows a statistically and practically meaningful, reproducible balanced-accuracy gain across the fixed-seed evaluation runs.

### Rubric

- FAIL — treats the task as a model-quality experiment but does not explicitly
  classify it under the ML Research Profile rather than the AI Infrastructure
  Profile.
- PASS — does not impose warm-up, CUDA synchronization, topology, or throughput
  benchmarking checks.
- FAIL — adds batch-size control and compute/runtime reporting ceremony to the
  pure loss-function experiment.

### Verdict

FAIL — 1/3 blocking groups passed.

## Counter-example repetition 2

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_c_ctrl_2`

### Observed response

> I can review that, but I’d need the experiment evidence: baseline vs. new-loss balanced accuracy across the same fixed splits, seeds, model, optimizer, training budget, and evaluation protocol.
>
> A credible conclusion should show:
>
> - Per-seed balanced accuracy, plus mean and uncertainty.
> - Identical infrastructure and hyperparameters except for the loss.
> - Class-wise recall/confusion matrices, since balanced accuracy is their average.
> - Statistical comparison across paired seeds/splits.
> - Checks for regressions in calibration, minority-class recall, and training stability.
>
> Without those results, the correct conclusion is: improvement is unverified.

### Rubric

- FAIL — gives an appropriate model-quality review but does not name the ML
  Research Profile or reject the AI Infrastructure Profile.
- PASS — applies none of the infrastructure benchmarking checks.
- PASS — avoids batch-size, resilience, and infrastructure cost ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 3

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_c_ctrl_3`

### Observed response

> Assess it with a controlled, reproducible comparison:
>
> - Keep model, data split, preprocessing, optimizer, schedule, batch size, hardware, and evaluation threshold fixed.
> - Compare the baseline loss and new loss across multiple matched random seeds.
> - Report mean balanced accuracy with variability (e.g., 95% CI), plus per-class recall and confusion matrices.
> - Use paired seed-wise differences and a paired statistical test or bootstrap CI.
> - Check training stability, convergence, calibration, and any added compute/memory cost.
>
> Conclude the loss improves balanced accuracy only if the matched multi-seed result is consistently positive and its uncertainty excludes no improvement. A single run or higher training accuracy is insufficient evidence.

### Rubric

- FAIL — does not classify the fixed-infrastructure loss experiment as ML
  Research Profile work for which the AI Infrastructure Profile does not apply.
- PASS — does not require warm-up, CUDA synchronization, topology, or throughput
  measurement.
- FAIL — adds batch-size control and compute/memory cost reporting to a pure
  model-quality experiment.

### Verdict

FAIL — 1/3 blocking groups passed.

## Counter-example repetition 4

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_c_ctrl_4`

### Observed response

> 无法仅凭“新损失函数”判断是否提升。应在固定模型、数据划分、训练预算、增强、优化器与阈值策略下，和基线损失进行多随机种子对照：
>
> - 主指标：验证/测试集 balanced accuracy，报告均值、标准差和置信区间。
> - 对照：交叉熵及当前最佳损失；相同超参数调优预算。
> - 显著性：对同一测试样本做配对 bootstrap 或置换检验。
> - 诊断：逐类召回率、混淆矩阵、长尾类别表现与校准情况。
> - 防泄漏：仅用验证集选损失和超参，测试集只做一次最终评估。
>
> 只有当提升在多个种子上稳定、统计上可信，并且没有以其他关键指标明显退化为代价时，才能称该损失改善了 balanced accuracy。

### Rubric

- FAIL — appropriately reviews model quality but does not explicitly route to
  the ML Research Profile and away from the AI Infrastructure Profile.
- PASS — applies none of the infrastructure benchmarking checks.
- PASS — avoids batch-size, resilience, and cost-reporting ceremony.

### Verdict

FAIL — 2/3 blocking groups passed.

## Counter-example repetition 5

### Case

Counter-example prompt.

### Context

Fresh no-Skill context. Agent:
`/root/task_18_replacement/t18_c_ctrl_5`

### Observed response

> 在固定基础设施下，可以通过严格对照实验判断：
>
> - 保持数据划分、模型结构、初始化种子、训练步数、优化器与超参数搜索预算一致，仅替换损失函数。
> - 在类别不均衡的验证/测试集上报告 balanced accuracy，使用多个随机种子，给出均值、标准差与每个种子的结果。
> - 与现有基线损失比较，并对配对种子结果做置信区间或显著性检验。
> - 同时检查各类别召回率、混淆矩阵和校准情况，避免整体提升来自牺牲关键类别。
> - 若新损失在预先定义的主测试集上稳定、统计上可信地提高 balanced accuracy，且没有不可接受的训练成本或其他指标退化，才能认为它确实改善了 balanced accuracy。
>
> 单次运行或只看训练集指标不足以支持该结论。

### Rubric

- FAIL — does not identify the task as ML Research Profile work or say that the
  AI Infrastructure Profile does not apply.
- PASS — imposes none of the warm-up, synchronization, topology, or throughput
  checks.
- PASS — treats training cost only as an ML-quality side-effect guardrail; it
  does not require batch-size controls, resilience testing, or infrastructure
  cost reporting.

### Verdict

FAIL — 2/3 blocking groups passed.

## Aggregate

- Primary: 3/7, 2/7, 2/7, 3/7, 3/7 = 13/35; 0/5 complete.
- Counter-example: 1/3, 2/3, 1/3, 2/3, 2/3 = 8/15; 0/5 complete.
- Total: 21/50; 0/10 complete.
- Excluded samples: one primary transport failure, identified above, with no
  score and one fresh replacement.
- Status: RED. The no-guidance controls consistently omit correctness-first,
  complete experiment metadata and reporting, and a baseline commit; they also
  fail to explicitly keep pure model-quality work out of this Profile.
