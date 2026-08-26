#!/usr/bin/env python3
"""Mechanically validate SKILL.md frontmatter and required headings.

Checks the parts of `plugins/references/skill-design-framework.md`
that do not require judgment:

  - `metadata.work_shape` (or top-level `work_shape`) is one of five enum values
  - `metadata.permission_tier` is one of three enum values and matches `allowed-tools`
  - `metadata.version`, `metadata.owner`, `metadata.review_cadence` are present
  - body contains `## Outputs` and `## Worked example` headings
  - non-`practice-setup` skills contain `## Propose profile update`

Exits non-zero with one error line per violation. Exits 0 when all checked
files pass.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

WORK_SHAPES: tuple[str, ...] = (
    "hypothesis-driven-analysis",
    "option-evaluation",
    "structured-aggregation",
    "narrative-synthesis",
    "governance-tracking",
)

REQUIRED_METADATA_FIELDS = ("version", "owner", "review_cadence", "permission_tier")
REQUIRED_HEADINGS = ("## Outputs", "## Worked example")
PROPOSE_PROFILE_HEADING = "## Propose profile update"

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_HEADING_RE = re.compile(r"^## .+$", re.MULTILINE)
_FRONTMATTER_KEY_RE = re.compile(r"^(\s*)([A-Za-z0-9_-]+):\s*(.*)$")


def _strip_scalar(value: str) -> str | None:
    value = value.strip()
    if not value or value in {"|", ">"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def _parse_frontmatter_fields(raw: str) -> dict:
    """Parse the frontmatter fields this linter cares about."""
    root: dict[str, str] = {}
    metadata: dict[str, str] = {}
    in_metadata = False

    for line in raw.splitlines():
        match = _FRONTMATTER_KEY_RE.match(line)
        if not match:
            continue
        indent, key, rest = match.groups()
        level = len(indent)
        scalar = _strip_scalar(rest)

        if level == 0 and key == "metadata":
            in_metadata = True
            root["metadata"] = metadata
            continue

        if level == 0:
            in_metadata = False
            if scalar is not None:
                root[key] = scalar
            continue

        if in_metadata and level >= 2 and scalar is not None:
            metadata[key] = scalar

    return root


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


def _parse_frontmatter(text: str) -> tuple[dict | None, str, list[str]]:
    """Return (frontmatter dict or None, body, errors)."""
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return None, text, ["missing YAML frontmatter delimiters (---)"]
    raw = match.group(1)
    if not raw.strip():
        return None, text[match.end() :], ["empty frontmatter block"]
    return _parse_frontmatter_fields(raw), text[match.end() :], []


def _work_shape_value(frontmatter: dict) -> str | None:
    metadata = frontmatter.get("metadata")
    if isinstance(metadata, dict) and metadata.get("work_shape") is not None:
        value = metadata.get("work_shape")
    else:
        value = frontmatter.get("work_shape")
    if value is None:
        return None
    return str(value).strip()


def _metadata_mapping(frontmatter: dict) -> dict:
    metadata = frontmatter.get("metadata")
    if isinstance(metadata, dict):
        return metadata
    return {}


def _heading_present(body: str, heading: str) -> bool:
    return heading in _HEADING_RE.findall(body)


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def validate_skill(path: Path) -> list[str]:
    """Return a list of human-readable violation strings (empty if clean)."""
    rel = _display_path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read file: {exc}"]

    frontmatter, body, parse_errs = _parse_frontmatter(text)
    errs = [f"{rel}: {msg}" for msg in parse_errs]
    if frontmatter is None:
        return errs

    metadata = _metadata_mapping(frontmatter)
    for field in REQUIRED_METADATA_FIELDS:
        value = metadata.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errs.append(f"{rel}: missing metadata.{field}")

    work_shape = _work_shape_value(frontmatter)
    if work_shape is None:
        errs.append(
            f"{rel}: missing work_shape "
            f"(set metadata.work_shape to one of: {', '.join(WORK_SHAPES)})"
        )
    elif work_shape not in WORK_SHAPES:
        errs.append(
            f"{rel}: invalid work_shape {work_shape!r}; "
            f"valid options: {', '.join(WORK_SHAPES)}"
        )

    for heading in REQUIRED_HEADINGS:
        if not _heading_present(body, heading):
            errs.append(f"{rel}: missing required heading {heading!r}")

    skill_name = path.parent.name
    if skill_name != "practice-setup" and not _heading_present(body, PROPOSE_PROFILE_HEADING):
        errs.append(f"{rel}: missing required heading {PROPOSE_PROFILE_HEADING!r}")

    return errs


def check_skills(paths: list[Path]) -> list[str]:
    all_errs: list[str] = []
    for path in paths:
        all_errs.extend(validate_skill(path))
    return all_errs


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SKILL.md frontmatter and required headings against "
            "skill-design-framework.md."
        )
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when any checked skill fails validation (default)",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="specific SKILL.md paths to check (default: all first-party skills)",
    )
    args = parser.parse_args()

    if not args.check and len(sys.argv) == 1:
        args.check = True

    if args.files:
        paths = [Path(p).resolve() for p in args.files]
    else:
        paths = _first_party_skill_paths()

    if not paths:
        print("no SKILL.md files found to check", file=sys.stderr)
        return 2

    errs = check_skills(paths)
    tier_script = REPO_ROOT / "scripts" / "sync-skill-permission-tiers.py"
    tier_result = subprocess.run(
        [sys.executable, str(tier_script), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if tier_result.returncode != 0:
        if tier_result.stderr:
            print(tier_result.stderr, file=sys.stderr, end="")
        return 1

    if errs:
        print("skill validation FAILED:", file=sys.stderr)
        for message in errs:
            print(f"  {message}", file=sys.stderr)
        return 1

    print(f"  ✓ {len(paths)} skill(s) valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
