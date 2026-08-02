"""Summarize code, execution, and conclusion evidence independently."""

from __future__ import annotations

from collections.abc import Collection


CODE_LEVELS = {"deterministic", "invariant", "smoke", "regression", "conclusion"}
FAILED_STATUSES = {"failed", "cancelled"}


def summarize(
    runs: list[dict[str, object]],
    reviews: list[str],
    required_run_ids: Collection[str] | None = None,
) -> dict[str, object]:
    """Return verdicts for all supplied or explicitly required evidence.

    When ``required_run_ids`` is omitted, every supplied conclusion-level
    attempt is required. Reviews are retained but never used to derive status.
    Missing or incomplete required runs are ``not_verified`` execution;
    failed or cancelled required runs are ``failed`` execution.
    """
    by_run_id: dict[object, list[dict[str, object]]] = {}
    for run in runs:
        by_run_id.setdefault(run.get("run_id"), []).append(run)

    conclusion_records = [
        run for run in runs if run.get("validation_level") == "conclusion"
    ]
    if required_run_ids is None:
        required_ids = sorted({
            str(run.get("run_id"))
            for run in conclusion_records if run.get("run_id")
        })
        required_records = conclusion_records
    else:
        declared_ids = list(required_run_ids)
        seen_ids: set[str] = set()
        for run_id in declared_ids:
            if run_id in seen_ids:
                raise ValueError(
                    f"required_run_ids contains duplicate ID: {run_id}"
                )
            seen_ids.add(run_id)
        required_ids = sorted(declared_ids)
        required_records = [
            run for run_id in required_ids for run in by_run_id.get(run_id, [])
        ]

    missing_evidence: list[str] = []
    contract_invalid = False
    for run_id in required_ids:
        matches = by_run_id.get(run_id, [])
        if not matches:
            missing_evidence.append(f"required run '{run_id}' is missing")
            contract_invalid = True
        elif len(matches) != 1:
            missing_evidence.append(
                f"required run '{run_id}' appears {len(matches)} times"
            )
            contract_invalid = True
        else:
            required_record = matches[0]
            if required_record.get("validation_level") != "conclusion":
                missing_evidence.append(
                    f"required run '{run_id}' is not conclusion-level"
                )
                contract_invalid = True
            status = str(required_record.get("status") or "unknown")
            if status in FAILED_STATUSES:
                missing_evidence.append(
                    f"required run '{run_id}' failed with status '{status}'"
                )
                contract_invalid = True
            elif status != "completed":
                missing_evidence.append(
                    f"required run '{run_id}' is incomplete with status '{status}'"
                )
                contract_invalid = True

    unnamed_conclusion_runs = [
        (index, run)
        for index, run in enumerate(runs)
        if run.get("validation_level") == "conclusion" and not run.get("run_id")
    ]
    for index, run in unnamed_conclusion_runs:
        status = str(run.get("status") or "unknown")
        missing_evidence.append(
            f"conclusion-level run at index {index} has no run_id "
            f"and status '{status}'"
        )
        contract_invalid = True

    if required_run_ids is not None:
        required_id_set = set(required_ids)
        checked_unlisted_ids: set[str] = set()
        for run in conclusion_records:
            run_id = run.get("run_id")
            normalized_run_id = str(run_id)
            if (
                not run_id
                or normalized_run_id in required_id_set
                or normalized_run_id in checked_unlisted_ids
            ):
                continue
            checked_unlisted_ids.add(normalized_run_id)
            matches = by_run_id.get(run_id, [])
            if len(matches) != 1:
                missing_evidence.append(
                    f"supplied conclusion run '{run_id}' appears "
                    f"{len(matches)} times"
                )
                contract_invalid = True
                continue
            status = str(matches[0].get("status") or "unknown")
            if status in FAILED_STATUSES:
                missing_evidence.append(
                    f"supplied conclusion run '{run_id}' failed with "
                    f"status '{status}'"
                )
            elif status != "completed":
                missing_evidence.append(
                    f"supplied conclusion run '{run_id}' is incomplete "
                    f"with status '{status}'"
                )
                contract_invalid = True

    if not conclusion_records:
        missing_evidence.append("formal conclusion-level experiment")

    code_records = [
        run for run in runs if run.get("validation_level") in CODE_LEVELS
    ]
    completed_code = any(
        run.get("status") == "completed" for run in code_records
    )
    failed_code = any(
        run.get("status") in FAILED_STATUSES for run in code_records
    )
    incomplete_code = any(
        run.get("status") not in FAILED_STATUSES | {"completed"}
        for run in code_records
    )
    if completed_code and failed_code:
        code_verification = "inconclusive"
    elif failed_code:
        code_verification = "failed"
    elif completed_code and not incomplete_code:
        code_verification = "verified"
    else:
        code_verification = "not_verified"

    failed_conclusion = any(
        run.get("status") in FAILED_STATUSES for run in conclusion_records
    )
    if not conclusion_records:
        experiment_execution = "not_verified"
    elif failed_conclusion:
        experiment_execution = "failed"
    elif contract_invalid:
        experiment_execution = "not_verified"
    else:
        experiment_execution = "verified"

    completed_conclusions = [
        run for run in conclusion_records if run.get("status") == "completed"
    ]
    conclusions = {run.get("conclusion") for run in completed_conclusions}
    if experiment_execution != "verified":
        conclusion_support = "not_verified"
    elif {"supported", "not_supported"}.issubset(conclusions):
        conclusion_support = "inconclusive"
    elif conclusions == {"supported"}:
        conclusion_support = "verified"
    elif conclusions == {"not_supported"}:
        conclusion_support = "failed"
    else:
        conclusion_support = "inconclusive"

    remaining_risks: list[str] = []
    if contract_invalid:
        remaining_risks.append(
            "Required evidence is incomplete; the conclusion cannot be verified."
        )
    elif {"supported", "not_supported"}.issubset(conclusions):
        remaining_risks.append(
            "Completed conclusion outcomes conflict and require an aggregation policy."
        )
    elif experiment_execution == "verified" and conclusions not in (
        {"supported"},
        {"not_supported"},
    ):
        remaining_risks.append(
            "Completed conclusion evidence lacks a recognized scientific outcome."
        )

    return {
        "code_verification": code_verification,
        "experiment_execution": experiment_execution,
        "conclusion_support": conclusion_support,
        "missing_evidence": missing_evidence,
        "remaining_risks": remaining_risks,
        "reviews": reviews,
    }


def render_markdown(summary: dict[str, object]) -> str:
    """Render the independently derived evidence verdicts as Markdown."""
    missing = summary.get("missing_evidence", [])
    remaining_risks = summary.get("remaining_risks", [])
    lines = [
        "# Evidence Summary",
        "",
        f"- Code verification: {summary['code_verification']}",
        f"- Experiment execution: {summary['experiment_execution']}",
        f"- Conclusion support: {summary['conclusion_support']}",
        "",
        "## Missing evidence",
    ]
    lines.extend(f"- {item}" for item in missing)
    lines.extend(["", "## Remaining risks"])
    lines.extend(f"- {item}" for item in remaining_risks)
    return "\n".join(lines) + "\n"
