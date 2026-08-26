# Claude for Australian Financial Planners

**Draft the paperwork around advice and credit — meeting prep, file notes, SOA/ROA/CAR and BID scaffolds, compliance checklists — in minutes. Every output is for a licensed human to review, edit, and sign.**

## Install in one command

In [Claude Code](https://claude.com/product/claude-code) or [Claude Cowork](https://claude.com/product/cowork):

```bash
/plugin marketplace add <path-to-this-repo>
/plugin install advice-core@claude-for-financial-planners
```

Restart Claude Code, then run `/advice-core:practice-setup`. Pick **user scope** when asked. Full walkthrough: [QUICKSTART.md](QUICKSTART.md).

> [!IMPORTANT]
> **Every output is a draft for licensed human review — not personal advice, not credit assistance, not a product or lender recommendation, not a substitute for an AFSL/ACL, and not a digital advice provider under ASIC RG 255.** Source tagging on product facts, rates, and fees; incomplete-information warnings (s961B / RG 273); explicit gates before anything is sent, lodged, or filed. You remain the authorising signatory.

## Plugins at a glance

| Plugin | Best for | First command |
|---|---|---|
| [advice-core](./plugins/advice-core) | Setup, meeting prep, file notes, CRM hygiene, client letters, marketing review | `/advice-core:practice-setup` |
| [financial-adviser](./plugins/financial-adviser) | Fact-find, SOA/ROA/CAR drafts, review packs, APL research, DDO/TMD | `/financial-adviser:practice-setup` |
| [mortgage-broker](./plugins/mortgage-broker) | Needs analysis, policy research, serviceability comparison, BID rationale, trail book | `/mortgage-broker:practice-setup` |
| [compliance](./plugins/compliance) | File review, complaints, breach triage, REP 798 AI governance, audit export | `/compliance:practice-setup` |

Role-based routing: [QUICKSTART.md#which-plugin-is-for-me](QUICKSTART.md#which-plugin-is-for-me).

## Worked examples

Each example produces a **draft artefact for your review**.

### 1. File note from a consented transcript (Advice Core)

**You have:** a consented meeting transcript and the licensee's file-note headings.

**Run:** `/advice-core:file-note`

**You get:** a structured note that separates what the client said from what you said, flags advice-shaped moments you did **not** complete in the meeting, and leaves an audit log with approver TBD.

### 2. SOA scaffold (Financial Adviser)

**You have:** a fact-find, risk-profile artefact, and your recommended strategy in your own words.

**Run:** `/financial-adviser:soa-draft` — paste the fact-find and **your** recommendation.

**You get:** an SOA-shaped draft (CAR only if your licensee has confirmed that regime). Product selection is yours. BID safe-harbour steps appear as a **checklist you complete**, not a certificate. Incomplete information is called out at the top.

### 3. Lender comparison working (Mortgage Broker)

**You have:** Quickli or lender-calculator outputs for three panel lenders.

**Run:** `/mortgage-broker:serviceability-compare`

**You get:** a cost/affordability table and net-benefit **factors**. No winner. You write the BID rationale (`/mortgage-broker:bid-rationale`) after you choose.

## What this marketplace does NOT do

- Provide **personal advice** under the Corporations Act or **credit assistance** under the NCCP
- Autonomously select a product or lender and present it to a client as a recommendation
- Finalise or sign an SOA, CAR, or credit BID file
- Lodge to ApplyOnline, write to XPLAN, or send client email unless you explicitly confirm after a gate (and V1 has **no first-party CRM/lodgement MCP**)
- Certify Best Interests Duty, responsible lending, TMD fit, or reportable situations
- Replace your AFSL/ACL, PI, or compliance function

## Named agents

Job-style names map to slash commands. Scheduled watchers live under `agents/` only.

| Agent | What it does | Command |
|---|---|---|
| **Practice Setup** | Licensee + practice profile interview | `/<plugin>:practice-setup` |
| **Meeting Prep** | Internal briefing pack from prior file | `/advice-core:meeting-prep` |
| **File Note Writer** | Consented transcript → structured file note | `/advice-core:file-note` |
| **SOA Scaffolder** | Fact-find + adviser-authored strategy → SOA/CAR draft | `/financial-adviser:soa-draft` |
| **BID File Note** | Comparison + broker-authored choice → BID rationale scaffold | `/mortgage-broker:bid-rationale` |
| **File Reviewer** | Draft file → gap list against licensee checklist | `/compliance:file-review` |
| **FDS / Renewal Watcher** | Deadline reminder for reviews and FDS | scheduled (`financial-adviser`) |
| **Trail Book Watcher** | Cadence reminder to scan expiries | scheduled (`mortgage-broker`) |
| **File-Aging Watcher** | Files past review threshold | scheduled (`compliance`) |
| **Regulatory Change Watcher** | ASIC/Treasury/APRA bulletin draft | scheduled (`compliance`) |

Full command tables live in each plugin README.

## Trust spine

Shared rules in [`plugins/advice-core/references/trust-conventions.md`](plugins/advice-core/references/trust-conventions.md) (mirrored at [`plugins/references/trust-conventions.md`](plugins/references/trust-conventions.md)):

1. Standing **draft for licensed human review** disclaimer
2. Source tags (`[sourced:]` / `[verify]`) on product facts, rates, fees, legislated thresholds
3. Load-bearing assumptions and **incomplete-information** warnings at the top
4. Never invent numbers — `INPUT NEEDED`
5. Confidence: defensible draft vs structured first pass (never "advice")
6. Licensed-human gate before send / lodge / file
7. Audit log fields; `/compliance:audit-export` for a reconstructable pack
8. Privacy: prefer Australian/APP posture; no PII to unapproved endpoints

## Connectors

Skills work **markdown-in, markdown-out** with no connectors. Optional productivity MCP servers (Gmail, Drive, Calendar, Slack, Notion, Microsoft Graph) are listed in [CONNECTORS.md](./CONNECTORS.md). Dominant AU platforms (XPLAN, aggregator CRMs, ApplyOnline) did not ship first-party MCP servers at design time — paste extracts instead.

## Licence

Apache-2.0. See [LICENSE](./LICENSE).

This repository is a **design-and-prompt product, not legal advice**. Implementation should be reviewed by the licensee's compliance function and legal counsel against the current Corporations Act, NCCP Act, Privacy Act, TPB rules, and ASIC/AFCA requirements. Regulatory reform (including DBFO / Client Advice Record) is staged — verify current status before relying on SOA-vs-CAR defaults.
