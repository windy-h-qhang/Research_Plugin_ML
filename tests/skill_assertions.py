"""Static contract checks for Codex Skill files."""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional


_FIELD_PATTERN = re.compile(r"^([A-Za-z0-9_-]+):[ \t]*(.*)$")
_SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
_REQUIRED_FIELDS = ("name", "description")


def validate_skill(path: Path) -> List[str]:
    """Return stable, human-readable contract errors for a Skill file."""
    if not path.exists():
        return ["skill file does not exist"]
    if not path.is_file():
        return ["skill path is not a file"]

    try:
        contents = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ["skill file could not be read"]

    lines = contents.splitlines()
    if not lines or lines[0] != "---":
        return ["missing opening frontmatter delimiter"]

    closing_index = next(
        (index for index, line in enumerate(lines[1:], start=1) if line == "---"),
        None,
    )
    if closing_index is None:
        return ["missing closing frontmatter delimiter"]

    values = _frontmatter_values(lines[1:closing_index])
    errors: List[str] = []
    for field in _REQUIRED_FIELDS:
        if len(values[field]) != 1:
            errors.append(f'frontmatter must contain exactly one "{field}" field')

    name = _single_value(values["name"])
    description = _single_value(values["description"])
    if name is not None:
        if not _SKILL_NAME_PATTERN.fullmatch(name):
            errors.append("skill name must use kebab-case")
        if path.parent.name != name:
            errors.append("skill directory name must match the skill name")
    if description is not None and not description.startswith("Use when"):
        errors.append('description must start with "Use when"')
    if not "\n".join(lines[closing_index + 1 :]).strip():
        errors.append("skill body must not be empty")

    return errors


def _frontmatter_values(lines: List[str]) -> Dict[str, List[str]]:
    values: Dict[str, List[str]] = {field: [] for field in _REQUIRED_FIELDS}
    for line in lines:
        match = _FIELD_PATTERN.fullmatch(line)
        if match and match.group(1) in values:
            values[match.group(1)].append(_normalize_scalar(match.group(2)))
    return values


def _normalize_scalar(value: str) -> str:
    value = value.strip()
    if len(value) < 2:
        return value
    if value[0] == "'" and value[-1] == "'":
        return _normalize_single_quoted_scalar(value)
    if value[0] == '"' and value[-1] == '"':
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError:
            return value
        if isinstance(decoded, str):
            return decoded
    return value


def _normalize_single_quoted_scalar(value: str) -> str:
    inner = value[1:-1]
    normalized = []
    index = 0
    while index < len(inner):
        if inner[index] != "'":
            normalized.append(inner[index])
            index += 1
        elif index + 1 < len(inner) and inner[index + 1] == "'":
            normalized.append("'")
            index += 2
        else:
            return value
    return "".join(normalized)


def _single_value(values: List[str]) -> Optional[str]:
    return values[0] if len(values) == 1 else None
