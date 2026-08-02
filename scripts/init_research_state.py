from __future__ import annotations

import argparse
import inspect
import os
import secrets
import shutil
import stat
from pathlib import Path
from typing import Optional, Sequence


DIRECTORIES = ("experiments", "runs", "reviews", "local")
FILES = {
    "context.md": "context.md",
    "progress.md": "progress.md",
    ".gitignore": "research.gitignore",
}


class ResearchStatePathError(ValueError):
    """Raised when repository-controlled state paths are unsafe."""


class SecureOperationsUnavailable(RuntimeError):
    """Raised when the platform cannot provide no-follow file operations."""


_DIRECTORY_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
_NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)


def _secure_operations_supported() -> bool:
    required_dir_fd = (os.open, os.stat, os.mkdir, os.unlink, os.link)
    try:
        link_parameters = inspect.signature(os.link).parameters
        return (
            bool(getattr(os, "O_DIRECTORY", 0))
            and bool(getattr(os, "O_NOFOLLOW", 0))
            and all(
                function in os.supports_dir_fd for function in required_dir_fd
            )
            and os.stat in os.supports_follow_symlinks
            and os.link in os.supports_follow_symlinks
            and "src_dir_fd" in link_parameters
            and "dst_dir_fd" in link_parameters
            and "follow_symlinks" in link_parameters
        )
    except (AttributeError, TypeError, ValueError):
        return False


def _require_secure_operations() -> None:
    if not _secure_operations_supported():
        raise SecureOperationsUnavailable(
            "secure file operations are unavailable on this platform"
        )


def _entry_stat(directory_fd: int, name: str) -> Optional[os.stat_result]:
    try:
        return os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None
    except OSError:
        raise ResearchStatePathError("unsafe research state path") from None


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
            raise ResearchStatePathError("unsafe research state path") from None
        entry = _entry_stat(directory_fd, name)
    if entry is None or not stat.S_ISDIR(entry.st_mode):
        raise ResearchStatePathError("unsafe research state path")
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
        raise ResearchStatePathError("unsafe research state path") from None
    if (
        not stat.S_ISDIR(opened.st_mode)
        or (entry.st_dev, entry.st_ino) != (opened.st_dev, opened.st_ino)
    ):
        os.close(child_fd)
        raise ResearchStatePathError("unsafe research state path")
    return child_fd


def _open_root(root: Path) -> tuple[Path, int]:
    _require_secure_operations()
    root_fd: Optional[int] = None
    try:
        resolved = root.expanduser().resolve(strict=True)
        entry = resolved.lstat()
        if not stat.S_ISDIR(entry.st_mode):
            raise ResearchStatePathError("root must be an existing directory")
        root_fd = os.open(resolved, _DIRECTORY_FLAGS | _NOFOLLOW)
        opened = os.fstat(root_fd)
        if (
            not stat.S_ISDIR(opened.st_mode)
            or (entry.st_dev, entry.st_ino) != (opened.st_dev, opened.st_ino)
        ):
            raise ResearchStatePathError("root must be an existing directory")
    except ResearchStatePathError:
        if root_fd is not None:
            os.close(root_fd)
        raise
    except OSError:
        if root_fd is not None:
            os.close(root_fd)
        raise ResearchStatePathError("root must be an existing directory") from None
    return resolved, root_fd


def _validate_or_create_file(
    research_fd: int,
    target: str,
    source: Path,
    *,
    create: bool,
) -> None:
    entry = _entry_stat(research_fd, target)
    if entry is not None:
        if not stat.S_ISREG(entry.st_mode):
            raise ResearchStatePathError("unsafe research state path")
        return
    if not create:
        return
    temporary_name: Optional[str] = None
    temporary_fd: Optional[int] = None
    try:
        with source.open("rb") as source_handle:
            for _ in range(100):
                candidate = f".{target}.{secrets.token_hex(8)}.tmp"
                try:
                    temporary_fd = os.open(
                        candidate,
                        os.O_WRONLY | os.O_CREAT | os.O_EXCL | _NOFOLLOW,
                        0o666,
                        dir_fd=research_fd,
                    )
                except FileExistsError:
                    continue
                temporary_name = candidate
                break
            if temporary_fd is None or temporary_name is None:
                raise ResearchStatePathError("could not create research state file")
            with os.fdopen(temporary_fd, "wb") as destination_handle:
                temporary_fd = None
                shutil.copyfileobj(source_handle, destination_handle)
                destination_handle.flush()
                os.fsync(destination_handle.fileno())
        try:
            os.link(
                temporary_name,
                target,
                src_dir_fd=research_fd,
                dst_dir_fd=research_fd,
                follow_symlinks=False,
            )
        except FileExistsError:
            raced_entry = _entry_stat(research_fd, target)
            if raced_entry is None or not stat.S_ISREG(raced_entry.st_mode):
                raise ResearchStatePathError("unsafe research state path")
        os.unlink(temporary_name, dir_fd=research_fd)
        temporary_name = None
        os.fsync(research_fd)
    except ResearchStatePathError:
        raise
    except OSError:
        raise ResearchStatePathError("unsafe research state path") from None
    finally:
        if temporary_fd is not None:
            os.close(temporary_fd)
        if temporary_name is not None:
            try:
                os.unlink(temporary_name, dir_fd=research_fd)
            except FileNotFoundError:
                pass


def initialize(root: Path, templates: Path, dry_run: bool = False) -> list[Path]:
    _, root_fd = _open_root(root)
    research = root / ".research"
    planned = [research / name for name in DIRECTORIES]
    planned.extend(research / target for target in FILES)
    research_fd: Optional[int] = None
    try:
        research_fd = _open_child_directory(
            root_fd, ".research", create=not dry_run
        )
        if research_fd is None:
            return planned
        for directory in DIRECTORIES:
            child_fd = _open_child_directory(
                research_fd, directory, create=not dry_run
            )
            if child_fd is not None:
                os.close(child_fd)
        for target, source in FILES.items():
            _validate_or_create_file(
                research_fd,
                target,
                templates / source,
                create=not dry_run,
            )
        return planned
    finally:
        if research_fd is not None:
            os.close(research_fd)
        os.close(root_fd)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--templates", type=Path, default=Path(__file__).parents[1] / "templates"
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        planned = initialize(args.root, args.templates, args.dry_run)
    except (ResearchStatePathError, SecureOperationsUnavailable) as error:
        parser.error(str(error))
    for path in planned:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
