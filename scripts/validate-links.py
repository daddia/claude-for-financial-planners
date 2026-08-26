#!/usr/bin/env python3
"""Validate in-repo relative links in catalogue plugin markdown.

Convention (AGENTS.md § references): reference paths are written from the
*skill's* location — `../../references/<file>.md` from `skills/<name>/` —
regardless of which file the token appears in. Plugin `CLAUDE.md` and
`references/*.md` are instructions consumed by a skill, so they use the same
frame. This checker therefore resolves `../../<rest>` against the owning
plugin root, not against the containing file's directory.

Links written from the containing file's own directory (`./x.md`, `../x.md`
in READMEs) are resolved normally.

Skips plugins/plugin-management/ — its teaching examples use illustrative
paths that do not resolve in this repo.
"""
import os
import re
import sys

CATALOGUE = ["advice-core", "financial-adviser", "mortgage-broker", "compliance"]
# `../../<rest>` means <plugin-root>/<rest> under the skill-frame convention.
SKILL_FRAME = re.compile(r"\.\./\.\./([A-Za-z0-9._/-]+\.(?:md|json))")
# Normal relative links in backticks or markdown link syntax.
INLINE = re.compile(r"`(\./[^`\s]+\.(?:md|json))`")
MDLINK = re.compile(r"\]\((\.{1,2}/[^)\s]+)\)")


def plugin_root_for(path):
    parts = path.split(os.sep)
    if len(parts) >= 2 and parts[0] == "plugins" and parts[1] in CATALOGUE:
        return os.path.join("plugins", parts[1])
    return None


def check_file(path, errors):
    root = plugin_root_for(path)
    text = open(path, encoding="utf-8").read()

    for m in SKILL_FRAME.finditer(text):
        if root is None:
            continue  # mirror/contributor copies have no owning plugin
        target = os.path.join(root, m.group(1))
        if not os.path.exists(target):
            errors.append(f"{path}: `../../{m.group(1)}` -> missing {target}")

    for pattern in (INLINE, MDLINK):
        for m in pattern.finditer(text):
            link = m.group(1).split("#")[0]
            if link.startswith("../../"):
                continue  # handled by SKILL_FRAME
            target = os.path.normpath(os.path.join(os.path.dirname(path), link))
            if not os.path.exists(target):
                errors.append(f"{path}: `{link}` -> missing {target}")


def main():
    errors = []
    checked = 0
    for base, dirs, files in os.walk("."):
        dirs[:] = [
            d
            for d in dirs
            if d not in {".git", "node_modules", "__pycache__"}
            and os.path.join(base, d) != os.path.join(".", "plugins", "plugin-management")
        ]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.relpath(os.path.join(base, name), ".")
            if path.startswith("plugins/plugin-management"):
                continue
            checked += 1
            check_file(path, errors)

    if errors:
        for e in errors:
            print(f"  ✗ {e}")
        print(f"  ✗ {len(errors)} broken link(s) in {checked} markdown file(s)")
        return 1
    print(f"  ✓ links valid ({checked} markdown file(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
