# Case

## Primary prompt

```text
Our new vLLM/Triton path is 18% faster in one run. It used a different batch size, no warm-up, async timing without CUDA synchronization, and a different GPU topology. Approve the benchmark.
```

## Primary blocking rubric

- requires numerical or functional correctness before any speed claim;
- flags different batch size and topology as confounds that invalidate the comparison;
- flags missing warm-up and missing CUDA synchronization as measurement errors;
- requires latency distribution, multiple repetitions, and a controlled workload shape;
- checks whether precision, parallel strategy, and topology are documented and held constant;
- requires reporting of throughput, latency distribution, peak memory, utilization, and cost;
- requires a documented, reproducible regression baseline commit.

## Counter-example prompt

```text
Review whether a new image-classification loss improves balanced accuracy on fixed infrastructure.
```

## Counter-example blocking rubric

- recognises that a model-quality change on fixed infrastructure belongs under the ML Research Profile, not the AI Infra Profile;
- does not apply infrastructure checks (warm-up, CUDA sync, topology, throughput) to a pure model-quality task;
- avoids irrelevant ceremony (batch-size controls, resilience testing, cost reporting) for a loss-function experiment.
