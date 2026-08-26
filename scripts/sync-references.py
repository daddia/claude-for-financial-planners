#!/usr/bin/env python3
"""Keep advice-core shared references in sync with plugins/references and plugin copies."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGINS_DIR = REPO_ROOT / "plugins"
CANONICAL_DIR = PLUGINS_DIR / "advice-core" / "references"
MIRROR_DIR = PLUGINS_DIR / "references"

REFERENCE_FILES = (
    "trust-conventions.md",
    "practice-setup-framework.md",
    "org-profile-template.md",
)

FIRST_PARTY_PLUGINS = (
    "advice-core",
    "financial-adviser",
    "mortgage-broker",
    "compliance",
)

SHARED_PLUGIN_REFERENCES = REFERENCE_FILES


def _missing_paths() -> list[Path]:
    missing: list[Path] = []
    for name in REFERENCE_FILES:
        for directory in (CANONICAL_DIR, MIRROR_DIR):
            path = directory / name
            if not path.is_file() and directory == CANONICAL_DIR:
                missing.append(path)
    return missing


def _sync_plugin_copies() -> None:
    for plugin in FIRST_PARTY_PLUGINS:
        if plugin == "advice-core":
            continue
        plugin_refs = PLUGINS_DIR / plugin / "references"
        plugin_refs.mkdir(parents=True, exist_ok=True)
        for name in SHARED_PLUGIN_REFERENCES:
            shutil.copy2(CANONICAL_DIR / name, plugin_refs / name)


def _sync_mirror() -> None:
    MIRROR_DIR.mkdir(parents=True, exist_ok=True)
    for name in REFERENCE_FILES:
        shutil.copy2(CANONICAL_DIR / name, MIRROR_DIR / name)


def _check() -> bool:
    ok = True
    for name in REFERENCE_FILES:
        canonical = CANONICAL_DIR / name
        if not canonical.is_file():
            print(f"missing canonical: {canonical}", file=sys.stderr)
            ok = False
            continue
        mirror = MIRROR_DIR / name
        if not mirror.is_file():
            print(f"missing mirror: {mirror}", file=sys.stderr)
            ok = False
        elif not filecmp.cmp(canonical, mirror, shallow=False):
            print(f"out of sync: {canonical} != {mirror}", file=sys.stderr)
            ok = False
    for plugin in FIRST_PARTY_PLUGINS:
        if plugin == "advice-core":
            continue
        for name in SHARED_PLUGIN_REFERENCES:
            canonical = CANONICAL_DIR / name
            plugin_copy = PLUGINS_DIR / plugin / "references" / name
            if not plugin_copy.is_file():
                print(f"missing plugin copy: {plugin_copy}", file=sys.stderr)
                ok = False
            elif not filecmp.cmp(canonical, plugin_copy, shallow=False):
                print(f"out of sync: {canonical} != {plugin_copy}", file=sys.stderr)
                ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when copies drift (default if no other flags)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="copy canonical advice-core references to plugins/references and other plugins",
    )
    args = parser.parse_args()

    if not args.check and not args.apply and len(sys.argv) == 1:
        args.check = True

    missing = _missing_paths()
    if missing:
        for path in missing:
            print(f"missing: {path}", file=sys.stderr)
        return 1

    if args.apply:
        _sync_mirror()
        _sync_plugin_copies()
        print("  ✓ references synced")
        return 0

    if not _check():
        print("hint: python3 scripts/sync-references.py --apply", file=sys.stderr)
        return 1

    print("  ✓ references in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
