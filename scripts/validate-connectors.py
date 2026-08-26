#!/usr/bin/env python3
"""Validate connector placeholders in markdown and machine categories in .mcp.json."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_PATH = REPO_ROOT / "plugins" / "references" / "connector-taxonomy.json"

_PLACEHOLDER_RE = re.compile(r"~~([a-z][a-z0-9 -]*)")
_SKIP_DIRS = {".git", ".cursor", "node_modules", "__pycache__", "plugin-management"}
# plugin-management is a maintainer toolkit (not in the catalogue). Its teaching
# examples use generic ~~ placeholders outside this marketplace's taxonomy.


def _load_taxonomy() -> tuple[set[str], set[str], dict[str, str]]:
    with TAXONOMY_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)

    machine_categories: set[str] = set()
    valid_placeholders: set[str] = set()
    for entry in data["categories"]:
        machine_categories.add(entry["machine"])
        valid_placeholders.add(entry["placeholder"])
    valid_placeholders.update(data.get("meta_placeholders", []))
    deprecated: dict[str, str] = dict(data.get("deprecated_placeholders", {}))
    return machine_categories, valid_placeholders, deprecated


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _iter_markdown_files() -> list[Path]:
    paths: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        paths.append(path)
    return sorted(paths)


def _iter_mcp_json_files() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.glob("**/.mcp.json")
        if not any(part in _SKIP_DIRS for part in path.parts)
    )


def _normalize_placeholder(raw: str) -> str:
    return raw.strip().rstrip(".,;:")


def check_markdown(
    path: Path,
    valid_placeholders: set[str],
    deprecated: dict[str, str],
) -> list[str]:
    rel = _display_path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read file: {exc}"]

    errors: list[str] = []
    seen: set[tuple[int, str]] = set()
    for match in _PLACEHOLDER_RE.finditer(text):
        placeholder = _normalize_placeholder(match.group(1))
        key = (match.start(), placeholder)
        if key in seen:
            continue
        seen.add(key)
        if placeholder in deprecated:
            errors.append(
                f"{rel}: deprecated placeholder ~~{placeholder} "
                f"(use ~~{deprecated[placeholder]})"
            )
            continue
        if placeholder not in valid_placeholders:
            errors.append(f"{rel}: unknown placeholder ~~{placeholder}")
    return errors


def check_mcp_json(path: Path, machine_categories: set[str]) -> list[str]:
    rel = _display_path(path)
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{rel}: cannot read JSON: {exc}"]

    errors: list[str] = []
    categories = data.get("recommendedCategories")
    if categories is None:
        return errors
    if not isinstance(categories, list):
        return [f"{rel}: recommendedCategories must be a list"]
    for category in categories:
        if not isinstance(category, str):
            errors.append(f"{rel}: recommendedCategories entries must be strings")
            continue
        if category not in machine_categories:
            errors.append(f"{rel}: unknown machine category {category!r}")
    return errors


def validate_connectors() -> list[str]:
    if not TAXONOMY_PATH.is_file():
        return [f"missing taxonomy file: {_display_path(TAXONOMY_PATH)}"]
    machine_categories, valid_placeholders, deprecated = _load_taxonomy()
    errors: list[str] = []
    for path in _iter_markdown_files():
        errors.extend(check_markdown(path, valid_placeholders, deprecated))
    for path in _iter_mcp_json_files():
        errors.extend(check_mcp_json(path, machine_categories))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check and len(sys.argv) == 1:
        args.check = True
    errors = validate_connectors()
    if errors:
        print("connector validation FAILED:", file=sys.stderr)
        for message in errors:
            print(f"  {message}", file=sys.stderr)
        return 1
    print(
        f"  ✓ connectors valid "
        f"({len(_iter_markdown_files())} markdown file(s), "
        f"{len(_iter_mcp_json_files())} .mcp.json file(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
