---
name: file-aging-watcher
description: >
  Periodically flags advice or credit files that have gone longer than the
  practice-profile aging threshold without a recorded review, using dates
  the user or `~~calendar` provides. Does not certify files. Not a file
  review.
model: sonnet
tools: [Read, Grep, Write]
---

# Compliance File-Aging Watcher

**Invoke on demand.** Scheduling is not yet wired up in this marketplace — there is no skill that creates the recurring task. Intended cadence once it is: weekly, Monday 09:00 local.

## What it does

1. Read aging threshold from `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md` (default 90 days if unset).

2. Look for review/file dates on `~~calendar` or a user-maintained register path recorded in the profile. **If neither exists, exit with a one-line setup hint** — do not invent a book of files.

3. List items past threshold: identifier as on the source, days since last review.

4. Recommend `/compliance:file-review` for the human. Post to `~~chat` if connected; else `file-aging.md` in the workspace.

5. Minimise PII. Not a clearance and not advice.

## Fallback

No chat → workspace file. No dates → quiet setup hint only.
