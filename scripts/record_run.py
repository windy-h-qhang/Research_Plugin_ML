"""Validate and store lightweight, reproducible research run records."""

import argparse
import inspect
import json
import os
import secrets
import stat
from pathlib import Path
from typing import Optional, Sequence


REQUIRED = (
    "run_id",
    "experiment_id",
    "status",
    "environment_id",
    "command",
)
STATUSES = {
    "planned",
    "queued",
    "running",
    "completed",
    "failed",
    "cancelled",
    "unknown",
}


class RunPathError(ValueError):
    """Raised when a run-record path is unsafe."""


class SecureOperationsUnavailable(RuntimeError):
    """Raised when the platform cannot provide no-follow file operations."""


_DIRECTORY_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
_NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)


def _secure_operations_supported() -> bool:
    required_dir_fd = (os.open, os.stat, os.mkdir, os.unlink)
    try:
        replace_parameters = inspect.signature(os.replace).parameters
        return (
            bool(getattr(os, "O_DIRECTORY", 0))
            and bool(getattr(os, "O_NOFOLLOW", 0))
            and all(
                function in os.supports_dir_fd for function in required_dir_fd
            )
            and os.stat in os.supports_follow_symlinks
            and "src_dir_fd" in replace_parameters
            and "dst_dir_fd" in replace_parameters
        )
    except (AttributeError, TypeError, ValueError):
        return False


def _require_secure_operations() -> None:
    if not _secure_operations_supported():
        raise SecureOperationsUnavailable(
            "secure file operations are unavailable on this platform"
        )


def validate_record(record: dict[str, object]) -> list[str]:
    """Return all schema errors for a lightweight run record."""
    errors = [field + " is required" for field in REQUIRED if not record.get(field)]
    status = record.get("status")
    if status and status != "planned" and not record.get("started_at"):
        errors.append("started_at is required")
    if status and (not isinstance(status, str) or status not in STATUSES):
        errors.append(f"unsupported status: {status}")
    return errors


def _entry_stat(directory_fd: int, name: str) -> Optional[os.stat_result]:
    try:
        return os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None
    except OSError:
        raise RunPathError("unsafe research run path") from None


def _open_child_directory(
    directory_fd: int,
    name: str,
    *,
    create: bool,
) -> Optional[int]:
    entry = _entry_stat(directory_fd, name)
    if entry is None:
        if not create:
            return None
        try:
            os.mkdir(name, dir_fd=directory_fd)
        except OSError:
            raise RunPathError("unsafe research run path") from None
        entry = _entry_stat(directory_fd, name)
    if entry is None or not stat.S_ISDIR(entry.st_mode):
        raise RunPathError("unsafe research run path")
    child_fd: Optional[int] = None
    try:
        child_fd = os.open(
            name,
            _DIRECTORY_FLAGS | _NOFOLLOW,
            dir_fd=directory_fd,
        )
        opened = os.fstat(child_fd)
    except OSError:
        if child_fd is not None:
            os.close(child_fd)
        raise RunPathError("unsafe research run path") from None
    if (
        not stat.S_ISDIR(opened.st_mode)
        or (entry.st_dev, entry.st_ino) != (opened.st_dev, opened.st_ino)
    ):
        os.close(child_fd)
        raise RunPathError("unsafe research run path")
    return child_fd


def _open_root(root: Path) -> tuple[Path, int]:
    _require_secure_operations()
    root_fd: Optional[int] = None
    try:
        resolved = root.expanduser().resolve(strict=True)
        entry = resolved.lstat()
        if not stat.S_ISDIR(entry.st_mode):
            raise RunPathError("root must be an existing directory")
        root_fd = os.open(resolved, _DIRECTORY_FLAGS | _NOFOLLOW)
        opened = os.fstat(root_fd)
        if (
            not stat.S_ISDIR(opened.st_mode)
            or (entry.st_dev, entry.st_ino) != (opened.st_dev, opened.st_ino)
        ):
            raise RunPathError("root must be an existing directory")
    except RunPathError:
        if root_fd is not None:
            os.close(root_fd)
        raise
    except OSError:
        if root_fd is not None:
            os.close(root_fd)
        raise RunPathError("root must be an existing directory") from None
    return resolved, root_fd


def _load_existing(directory_fd: int, name: str) -> dict[str, object]:
    entry = _entry_stat(directory_fd, name)
    if entry is None:
        return {}
    if not stat.S_ISREG(entry.st_mode) or entry.st_nlink != 1:
        raise RunPathError("unsafe research run path")
    record_fd: Optional[int] = None
    try:
        record_fd = os.open(
            name,
            os.O_RDONLY | _NOFOLLOW,
            dir_fd=directory_fd,
        )
        opened = os.fstat(record_fd)
        if (
            not stat.S_ISREG(opened.st_mode)
            or opened.st_nlink != 1
            or (entry.st_dev, entry.st_ino) != (opened.st_dev, opened.st_ino)
        ):
            raise RunPathError("unsafe research run path")
        with os.fdopen(record_fd, "r", encoding="utf-8") as handle:
            record_fd = None
            loaded = json.load(handle)
    except RunPathError:
        raise
    except OSError:
        raise RunPathError("unsafe research run path") from None
    finally:
        if record_fd is not None:
            os.close(record_fd)
    if not isinstance(loaded, dict):
        raise ValueError("existing run record must be a JSON object")
    return loaded


def _atomic_write(directory_fd: int, name: str, record: dict[str, object]) -> None:
    payload = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode("utf-8")
    temporary_name: Optional[str] = None
    temporary_fd: Optional[int] = None
    try:
        for _ in range(100):
            candidate = f".{name}.{secrets.token_hex(8)}.tmp"
            try:
                temporary_fd = os.open(
                    candidate,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL | _NOFOLLOW,
                    0o600,
                    dir_fd=directory_fd,
                )
            except FileExistsError:
                continue
            temporary_name = candidate
            break
        if temporary_fd is None or temporary_name is None:
            raise RunPathError("could not create run record")
        with os.fdopen(temporary_fd, "wb") as handle:
            temporary_fd = None
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(
            temporary_name,
            name,
            src_dir_fd=directory_fd,
            dst_dir_fd=directory_fd,
        )
        temporary_name = None
        os.fsync(directory_fd)
    except RunPathError:
        raise
    except OSError:
        raise RunPathError("could not write run record") from None
    finally:
        if temporary_fd is not None:
            os.close(temporary_fd)
        if temporary_name is not None:
            try:
                os.unlink(temporary_name, dir_fd=directory_fd)
            except FileNotFoundError:
                pass


def _upsert_run_at(
    directory_fd: int,
    name: str,
    patch: dict[str, object],
    *,
    dry_run: bool,
) -> dict[str, object]:
    existing = _load_existing(directory_fd, name)
    merged = {**existing, **patch}
    errors = validate_record(merged)
    if errors:
        raise ValueError("\n".join(errors))
    if not dry_run:
        _atomic_write(directory_fd, name, merged)
    return merged


def _open_record_parent(
    path: Path,
    *,
    create: bool,
) -> tuple[Optional[int], list[int]]:
    supplied = path.expanduser()
    if not supplied.is_absolute():
        supplied = Path.cwd() / supplied
    if any(component in {".", ".."} for component in supplied.parts):
        raise RunPathError("unsafe research run path")

    parent = supplied.parent
    parent_parts = parent.parts
    if len(parent_parts) > 1:
        anchor = Path(parent_parts[0], parent_parts[1])
        components = parent_parts[2:]
    else:
        anchor = Path(parent_parts[0])
        components = ()
    _, root_fd = _open_root(anchor)
    opened_fds = [root_fd]
    try:
        parent_fd: Optional[int] = root_fd
        for component in components:
            parent_fd = _open_child_directory(
                parent_fd, component, create=create
            )
            if parent_fd is None:
                return None, opened_fds
            opened_fds.append(parent_fd)
        return parent_fd, opened_fds
    except Exception:
        for opened_fd in reversed(opened_fds):
            os.close(opened_fd)
        raise


def upsert_run(
    path: Path,
    patch: dict[str, object],
    dry_run: bool = False,
) -> dict[str, object]:
    """Merge a patch into one run record, validating before an atomic write."""
    _require_secure_operations()
    if (
        not path.name
        or path.name in {".", ".."}
        or any(component in {".", ".."} for component in path.parts)
    ):
        raise RunPathError("unsafe research run path")
    opened_fds: list[int] = []
    try:
        parent_fd, opened_fds = _open_record_parent(
            path, create=not dry_run
        )
        if parent_fd is None:
            merged = dict(patch)
            errors = validate_record(merged)
            if errors:
                raise ValueError("\n".join(errors))
            return merged
        return _upsert_run_at(parent_fd, path.name, patch, dry_run=dry_run)
    except RunPathError:
        raise
    except OSError:
        raise RunPathError("unsafe research run path") from None
    finally:
        for opened_fd in reversed(opened_fds):
            os.close(opened_fd)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Record one run under ``<root>/.research/runs``."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--experiment-id", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--environment-id", required=True)
    parser.add_argument("--command", required=True)
    parser.add_argument("--started-at")
    parser.add_argument(
        "--artifact",
        action="append",
        help="reference to an output, log, tracker, or checkpoint; may be repeated",
    )
    parser.add_argument("--dry-run", action="store_true")
    arguments = parser.parse_args(argv)

    patch: dict[str, object] = {
        "run_id": arguments.run_id,
        "experiment_id": arguments.experiment_id,
        "status": arguments.status,
        "environment_id": arguments.environment_id,
        "command": arguments.command,
    }
    if arguments.started_at is not None:
        patch["started_at"] = arguments.started_at
    if arguments.artifact is not None:
        patch["artifacts"] = arguments.artifact

    root_fd: Optional[int] = None
    research_fd: Optional[int] = None
    runs_fd: Optional[int] = None
    try:
        if (
            not arguments.run_id
            or arguments.run_id in {".", ".."}
            or "/" in arguments.run_id
            or "\\" in arguments.run_id
        ):
            raise ValueError("run_id must be a single filename component")
        _, root_fd = _open_root(arguments.root)
        research_fd = _open_child_directory(
            root_fd, ".research", create=not arguments.dry_run
        )
        if research_fd is None:
            result = dict(patch)
            errors = validate_record(result)
            if errors:
                raise ValueError("\n".join(errors))
        else:
            runs_fd = _open_child_directory(
                research_fd, "runs", create=not arguments.dry_run
            )
            if runs_fd is None:
                result = dict(patch)
                errors = validate_record(result)
                if errors:
                    raise ValueError("\n".join(errors))
            else:
                result = _upsert_run_at(
                    runs_fd,
                    f"{arguments.run_id}.json",
                    patch,
                    dry_run=arguments.dry_run,
                )
    except (RunPathError, SecureOperationsUnavailable) as error:
        parser.error(str(error))
    except ValueError as error:
        parser.error(str(error))
    finally:
        if runs_fd is not None:
            os.close(runs_fd)
        if research_fd is not None:
            os.close(research_fd)
        if root_fd is not None:
            os.close(root_fd)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
