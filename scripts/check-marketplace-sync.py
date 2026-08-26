#!/usr/bin/env python3
"""Verify marketplace.json plugin entries match each plugin's plugin.json.

For first-party plugins (local ``./<dir>`` sources), ``name``, ``description``,
and ``author`` in ``.claude-plugin/marketplace.json`` must match the
corresponding fields in ``<dir>/.claude-plugin/plugin.json``.

Exits 0 when in sync, 1 when any field diverges.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

SYNC_FIELDS = ("name", "description", "author")


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def check_sync() -> list[str]:
    """Return human-readable mismatch messages (empty when clean)."""
    marketplace = _load_json(MARKETPLACE_PATH)
    errs: list[str] = []

    for index, entry in enumerate(marketplace.get("plugins", [])):
        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("./"):
            continue

        plugin_dir = REPO_ROOT / source.removeprefix("./")
        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        label = f"plugins[{index}] ({source})"

        if not manifest_path.is_file():
            errs.append(f"{label}: missing {_display_path(manifest_path)}")
            continue

        plugin_manifest = _load_json(manifest_path)
        for field in SYNC_FIELDS:
            market_value = entry.get(field)
            plugin_value = plugin_manifest.get(field)
            if market_value != plugin_value:
                errs.append(
                    f"{label}: {field} mismatch — "
                    f"marketplace.json has {market_value!r}, "
                    f"plugin.json has {plugin_value!r}"
                )

    return errs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when marketplace and plugin.json fields diverge (default)",
    )
    args = parser.parse_args()

    if not args.check and len(sys.argv) == 1:
        args.check = True

    errs = check_sync()
    if errs:
        print("marketplace sync FAILED:", file=sys.stderr)
        for message in errs:
            print(f"  {message}", file=sys.stderr)
        return 1

    print("  ✓ marketplace.json in sync with plugin manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
