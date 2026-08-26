# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~crm` might mean XPLAN, AdviserLogic, Connective Mercury, or any other practice CRM with an MCP server or API bridge.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. Each plugin's `.mcp.json` pre-configures the productivity servers listed below as "Included servers"; any MCP server in that category works just as well.

**V1 skills work without connectors** — paste a transcript, a fact-find, or a file note and get a draft. Connectors enrich meeting prep, CRM hygiene, and the watcher agents when they exist.

## Connectors for this marketplace

| Category | Placeholder | Included servers | Other options / AU platforms |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Gmail | Microsoft 365 / Outlook |
| Documents | `~~documents` | Google Drive | OneDrive, SharePoint, FYI Docs |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Knowledge base | `~~knowledge base` | Notion | Confluence, licensee clause library |
| CRM / practice management | `~~crm` | — (none first-party MCP yet) | XPLAN/Iress, AdviserLogic, Worksorted, Practifi, Salesforce FSC; aggregator CRMs (Connective Mercury, AFG, LMG, Finsure/Infynity, Salestrekker, BrokerEngine) |
| E-signature | `~~e-signature` | — | DocuSign, Adobe Sign, Annature |
| Spreadsheet | `~~spreadsheet` | Google Drive | Excel / Microsoft 365 |
| Web & news monitoring | `~~web monitoring` | Native web search | ASIC, APRA, Treasury, AFCA feeds |

## Australian advice and broking platforms

As of the design research, **none of the dominant AU platforms ship a first-party MCP server**. Treat `~~crm` as a category, not a live XPLAN or ApplyOnline connector:

- **Adviser stack:** XPLAN/Iress (Open Standard API, OAuth2; Partnership tier), AdviserLogic, Worksorted, Midwinter, Salesforce Financial Services Cloud, Practifi; document tools FYI Docs, Nod.
- **Broker stack:** aggregator CRMs feeding NextGen.Net ApplyOnline; Quickli (serviceability), Sherlok (repricing), Equifax/illion (verification).

When a vendor ships or blesses an MCP server, add it to the relevant plugin's `.mcp.json` and record it in that plugin's `CONNECTORS.md`. Until then, skills fall back to user-uploaded files and pasted extracts.

## Notes

- **Microsoft Graph (Enterprise)** is listed in `.mcp.json` for Outlook/SharePoint/Teams tenants that enable Agent365 MCP — see each plugin's `CONNECTORS.md`.
- **Privacy default:** do not send client PII to an unapproved endpoint. Prefer Australian hosting / APP-compliant contractual commitments recorded in the org profile.
- **Watchers** (`compliance` file-aging and regulatory-change; `financial-adviser` FDS-renewal; `mortgage-broker` trail-book opportunity) degrade to a workspace file when `~~chat` is not connected. They are **invoked on demand in V1** — nothing here creates a recurring task yet.
