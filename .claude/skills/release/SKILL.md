---
name: release
description: >
  Run this marketplace's release gates, bump independently versioned plugin
  manifests, re-validate, commit, and push. Use when asked to "release",
  "ship", "bump and push", or "cut a release".
argument-hint: "[plugin-name] [patch|minor|major]"
---

# Release

Immediately read and execute
`plugins/plugin-management/skills/release/SKILL.md`. That file is the source
of truth for this repo's release workflow. Do not improvise a release from
this stub.
