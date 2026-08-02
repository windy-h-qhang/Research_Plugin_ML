---
name: applying-ai-infra-profile
description: Use when work involves distributed training, inference serving, CUDA or Triton kernels, GPU memory, throughput, latency, Slurm, communication, resilience, or infrastructure cost
---

# Applying AI Infrastructure Profile

Use this Profile for distributed training, inference serving, GPU kernels,
performance, resilience, or infrastructure cost.

## Select the right Profile

For a pure model-quality experiment on fixed infrastructure, state that the ML
Research Profile is primary and do not apply this Profile. Do not add
infrastructure warm-up, synchronization, topology, throughput, batch-size,
resilience, or cost-reporting ceremony to a loss, metric, or calibration
experiment.

## Performance approval contract

Do not approve a performance claim unless the response covers every check.
In the approval response, state all seven checks explicitly; do not compress or
omit one:

1. Prove numerical and functional correctness against a trusted baseline at the
   same precision before discussing speed.
2. Hold workload shape, including batch size, and hardware/network topology
   constant. Treat a difference in either as a confound that invalidates the
   comparison.
3. Warm up before timing and use explicit CUDA synchronization at measurement
   boundaries. Unsynchronized asynchronous timing measures queued work, not
   runtime.
4. Run multiple repetitions over a controlled workload and report a latency
   distribution, not a single point estimate.
5. Explicitly document and hold constant all three of precision, parallel
   strategy, and topology. Record GPU/CPU model and count, interconnect/NUMA,
   software stack, workload dimensions, measurement window, and repetition
   count.
6. Report throughput, latency distribution (p50, p95, p99, max), peak GPU
   memory, GPU utilization, failures, and estimated cost.
7. Explicitly identify the documented, reproducible baseline commit and require
   it to pass the same correctness checks.

For systems that make resilience claims, also test checkpoint save/load,
preemption handling, retry, and restart.
