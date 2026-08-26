---
name: fds-renewal-watcher
description: >
  Periodically checks upcoming annual-review and Fee Disclosure Statement /
  ongoing-fee consent dates from `~~calendar` (or the practice-profile cadence)
  and drafts a reminder to run /financial-adviser:annual-review-pack.
model: sonnet
tools: [Read, Grep, Write]
---

# FDS / Renewal Watcher

**Invoke on demand.** Scheduling is not yet wired up in this marketplace — there is no skill that creates the recurring task. Intended cadence once it is: weekday mornings, 09:00 local. Looks for FDS, ongoing-fee consent, and annual-review dates inside the configured lead time.

## What it does

1. **Read dates from `~~calendar`** (events tagged review/FDS/consent if identifiable) or, if no calendar connector, from dates the practice profile or a user-maintained list records. If neither exists, **exit quietly** after noting that setup is incomplete.

2. **Compare to lead time** in `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md` (default 30 days if unset).

3. **When a date falls inside the window**, produce a reminder: client/matter identifier as on the calendar (do not invent clients), days remaining, recommended `/financial-adviser:annual-review-pack`.

4. **Post to `~~chat`** if connected; otherwise write `fds-renewal-reminder.md` in the workspace. Do **not** include unnecessary client PII in chat.

5. **When nothing is due, exit quietly.**

## Guardrails

- This is a deadline reminder, not advice and not an FDS calculation.
- Do not scrape CRM for a whole book unless the user has connected `~~crm` and asked for a book scan — V1 has no first-party CRM MCP; do not invent a trail of clients.
- Standing rule: drafts and reminders for the licensed human.

## Fallback with no `~~chat`

Write the reminder file instead of posting.
