---
name: applying-ml-research-profile
description: Use when research work involves PyTorch models, supervised or self-supervised learning, losses, metrics, calibration, data splits, sampling, or model-quality experiments
---

# Applying ML Research Profile

For PyTorch model-quality work, apply this Profile before accepting experiment
design, validation, debugging, or review claims.

## Data

Verify data identity and splits before any metric. Detect leakage: overlapping
examples, duplicate records across splits, class-map drift, sampling changes,
and preprocessing mismatches between train and test. Fit preprocessing only on
training data. When class sampling changes, keep the class map and evaluation
distribution explicit, compare the sampling change against the prior setup, and
state the causal connection: sampling changes can hide or distort per-class
behavior, so inspect per-class metrics for the comparison in the same review
point rather than listing sampling and per-class metrics separately.

## Tensor and gradient hygiene

Check loss, label, and metric semantics. Verify tensor shape, dtype, device,
gradient flow, frozen parameters, and optimizer parameter groups. Confirm that
zero-grad, backward, and optimizer-step ordering is correct.

## Imbalanced and calibrated systems

When classes are imbalanced or calibration matters, require per-class metrics
(precision, recall, F1) and balanced metrics in addition to any aggregate
score. Overall accuracy alone is never sufficient for an imbalanced classifier.
Check calibration, including per-class calibration when relevant. Set thresholds
on held-out validation data, never on the test set.

## Reproducibility

Control seeds (Python, NumPy, PyTorch, CUDA) and data order. Use predeclared
seeds and report every run. For model-quality claims, compare the changed factor
against a control while holding the other settings fixed. Pair each candidate
and control run with the same seed and identical data order, repeat those paired
comparisons across multiple predeclared seeds, and report uncertainty or a
statistical comparison. A single seed or selected run does not establish a
quality claim.

## When not to use

Skip this Profile for a pure systems benchmark where no model-quality question
is being asked and the task is latency, throughput, or resource measurement of
infrastructure (Triton kernels, CUDA graphs, communication collectives). Those
tasks belong under the AI Infrastructure Profile. Start the review by stating
that the AI Infrastructure Profile is primary and the ML Research Profile does
not apply. Then use only relevant systems checks; do not add ML ceremony such
as data-split leakage, class balancing, per-class metrics, calibration, ML seed
control, or model-quality ablations.
