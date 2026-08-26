# Record-keeping and audit export

**Not legal advice.**

## Retention

- AFS licensees: financial records **7 years** (Corporations Act s286)
- Personal-advice records: RG 175 and ASIC Corporations (Record-Keeping Requirements … when Giving Personal Advice) Instrument **2024/508** (notional s912G(7) — records of information relied on to demonstrate client-interest priority)
- Credit files: keep to the licensee's ACL policy; AFCA will expect a reconstructable file

Prompts, outputs, and interaction metadata are **business records** for AFSL/ACL audits and PI/complaints defence.

## What `/compliance:audit-export` should assemble

A pack (markdown unless the user asks for another format) containing:

1. Matter identifier (client code the user supplies — do not invent)
2. Skill(s) invoked and date range
3. Inputs relied on (file names, CRM extracts, transcripts, policy PDFs)
4. Draft outputs (or pointers to where they were saved)
5. Reviewer / authorising signatory (blank if not yet signed)
6. Gaps still open (`INPUT NEEDED`, `[verify]`, incomplete-information warnings)
7. Disclaimer that the pack is a reconstruction aid, not a certified file

Never invent an approver or a file-note that was not produced in session or supplied by the user.
