#!/usr/bin/env python3
"""Set allowed-tools and metadata.permission_tier on first-party SKILL.md files."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

ADVISORY_TOOLS = "Read, Grep, Glob"
ARTEFACT_TOOLS = "Read, Grep, Glob, Write"

ARTEFACT_SKILL_NAMES = frozenset(
    {
        "practice-setup",
        "ai-governance-setup",
        "audit-export",
    }
)

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
_ALLOWED_TOOLS_RE = re.compile(r"^allowed-tools:\s*.+$", re.MULTILINE)
_PERMISSION_TIER_RE = re.compile(r"^  permission_tier:\s*.+$", re.MULTILINE)


def _first_party_skill_paths() -> list[Path]:
    with MARKETPLACE_PATH.open(encoding="utf-8") as handle:
        marketplace = json.load(handle)
    paths: list[Path] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("./"):
            continue
        plugin_dir = REPO_ROOT / source.removeprefix("./")
        paths.extend(sorted(plugin_dir.glob("skills/**/SKILL.md")))
    return paths


def _skill_name(frontmatter: str) -> str | None:
    match = _NAME_RE.search(frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def _tier_for_name(name: str) -> str:
    if name in ARTEFACT_SKILL_NAMES:
        return "artefact-writer"
    return "advisory"


def _tools_for_tier(tier: str) -> str:
    if tier == "artefact-writer":
        return ARTEFACT_TOOLS
    return ADVISORY_TOOLS


def _expected_for_path(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing frontmatter")
    name = _skill_name(match.group(1))
    if not name:
        raise ValueError(f"{path}: missing name in frontmatter")
    tier = _tier_for_name(name)
    return tier, _tools_for_tier(tier)


def _parse_tools(value: str) -> frozenset[str]:
    return frozenset(part.strip() for part in value.split(",") if part.strip())


def _apply_path(path: Path, dry_run: bool) -> list[str]:
    rel = path.relative_to(REPO_ROOT)
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return [f"{rel}: missing frontmatter"]
    tier, tools = _expected_for_path(path)
    frontmatter = match.group(1)
    current_tools = _ALLOWED_TOOLS_RE.search(frontmatter)
    current_tier = _PERMISSION_TIER_RE.search(frontmatter)
    current_tools_val = (
        current_tools.group(0).split(":", 1)[1].strip() if current_tools else None
    )
    current_tier_val = (
        current_tier.group(0).split(":", 1)[1].strip() if current_tier else None
    )
    errs: list[str] = []
    if current_tools_val is None or _parse_tools(current_tools_val) != _parse_tools(tools):
        errs.append(f"{rel}: allowed-tools is {current_tools_val!r}, want {tools!r}")
    if current_tier_val != tier:
        errs.append(f"{rel}: permission_tier is {current_tier_val!r}, want {tier!r}")
    if not errs:
        return []
    if dry_run:
        return errs
    raise RuntimeError(f"{rel}: refusing to rewrite in this repo copy — fix frontmatter by hand")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift only; exit 1 on mismatch",
    )
    args = parser.parse_args()
    dry_run = args.check or True
    paths = _first_party_skill_paths()
    all_errs: list[str] = []
    for path in paths:
        all_errs.extend(_apply_path(path, dry_run=True))
    if all_errs:
        print("permission tier check FAILED:", file=sys.stderr)
        for message in all_errs:
            print(f"  {message}", file=sys.stderr)
        return 1
    print(f"  ✓ {len(paths)} skill(s) permission tiers checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
