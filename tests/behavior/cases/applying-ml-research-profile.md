# Case

## Primary prompt

```text
Our classifier is highly imbalanced. I tuned the confidence threshold on the test set, changed class sampling, and report only overall accuracy. Review whether the experiment is valid.
```

## Primary blocking rubric

- flags confidence-threshold tuning on the test set as leakage;
- notes that changing class sampling without per-class metrics hides per-class behavior;
- states that overall accuracy is insufficient for an imbalanced classifier and requires per-class metrics;
- checks calibration, class-map drift, or preprocessing consistency;
- requires controlled seeds, data order, and repeated runs for quality claims;
- does not load the AI Infra or LLM Profile for an ML model-quality task.

## Counter-example prompt

```text
Review the p99 latency measurement for a Triton kernel with no model-quality change.
```

## Counter-example blocking rubric

- recognises that a pure systems benchmark belongs under the AI Infra Profile, not the ML Research Profile;
- does not apply ML-specific checks such as per-class metrics, calibration, or data-split leakage;
- avoids irrelevant ML ceremony (class balancing, seed control, ablations) for a non-model-quality task.
