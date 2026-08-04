#!/usr/bin/env python3
"""Export the Qoder-native plugin package from this repository.

The repository ships plugin manifests for multiple hosts. Qoder packages must
carry `.qoder-plugin/plugin.json` at the root, live in a directory whose name
matches the manifest `name`, and must not include `.codex-plugin` or local
runtime state. This script stages that installable form under `dist/` and can
optionally zip it for distribution.

Usage:
    python3 scripts/export_qoder_plugin.py [--zip] [--output-dir PATH]
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / ".qoder-plugin" / "plugin.json"

# Host manifests, local history, and build/runtime state that must never be
# packaged for Qoder. `.claude-plugin` is intentionally kept as upstream
# metadata (the manifest sets preserveUpstreamMetadata).
EXCLUDED_DIRS = {
    ".git",
    ".codex-plugin",
    ".local-history",
    ".worktrees",
    "dist",
    "tmp",
    "__pycache__",
}
EXCLUDED_FILES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".zip", ".pyc", ".pyo"}


def plugin_name() -> str:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    name = manifest.get("name", "").strip()
    if not name:
        sys.exit("error: .qoder-plugin/plugin.json is missing a name field")
    return name


def ignore_for_copy(_src: str, entries: list[str]) -> set[str]:
    skipped: set[str] = set()
    for entry in entries:
        path = Path(_src) / entry
        if entry in EXCLUDED_DIRS and path.is_dir():
            skipped.add(entry)
        elif entry in EXCLUDED_FILES or entry.endswith(tuple(EXCLUDED_SUFFIXES)):
            skipped.add(entry)
        elif entry.startswith(".env"):
            skipped.add(entry)
    return skipped


def export(output_dir: Path) -> Path:
    name = plugin_name()
    dest = output_dir / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(REPO_ROOT, dest, ignore=ignore_for_copy)
    return dest


def zip_package(plugin_root: Path, output_dir: Path) -> Path:
    manifest = json.loads((plugin_root / ".qoder-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = manifest.get("version", "0.0.0")
    archive = output_dir / f"{plugin_root.name}-{version}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(plugin_root.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(plugin_root))
    return archive


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", action="store_true", help="also build a distributable zip")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "dist",
        help="output directory for the staged plugin (default: dist/)",
    )
    args = parser.parse_args()

    if not MANIFEST.exists():
        sys.exit("error: .qoder-plugin/plugin.json not found; run from the repository root")

    plugin_root = export(args.output_dir)
    print(f"staged: {plugin_root}")
    if args.zip:
        print(f"zip: {zip_package(plugin_root, args.output_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
