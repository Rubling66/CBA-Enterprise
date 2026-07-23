---
type: phase-0-acceptance
product: CBA-Enterprise
status: LOCKED_DRAFT v3 — full research corpus absorbed
date: 2026-07-23
agent: engineer-grok
revision: 3
source: Commander Phase-0 checklist parts 1–3 (NotebookLM token-split Qs)
note: NotebookLM input token limits may require splitting research queries; reassemble here as single law.
---

# PHASE-0 ACCEPTANCE CHECKLIST  
## Core Compliance & Architecture Gates (v3 — complete)

**Law:** No feature phase (M1–M5) may **process bank or consumer regulated data** in a shared/prod-like environment until every control marked **MUST PASS BEFORE START = YES** is green with evidence (or signed **N/A** where allowed).

**Build order:** Phase 0 → **M1 Ingest + M3 Report** → M2 Track → M4 Verify → M5 Gate.  
**Stress fail = freeze next phase.**

**Related:**  
- `docs/architecture/data-model.md`  
- `docs/architecture/system-architecture.md`  
- `docs/regulatory/OCC-2013-29-vendor-management.md`  
- `docs/compliance/DATA_PLANE_SPEC.md` (backside contracts — this revision)  
- `docs/compliance/artifacts/`

---

## Gate summary (G1–G10)

| # | Control | Must pass before start? | Evidence artifact |
|---|---------|-------------------------|-------------------|
| **G1** | Data lineage & source mapping | **YES** | Data Lineage Document / Mapping Matrix |
| **G2** | Front-end validation & quality sentinel | **YES** | Validation Rules Config Record & Test Log |
| **G3** | Change management & secure SDLC | **YES** | CI/CD Deployment Audit Trail |
| **G4** | Third-party vendor risk & due diligence | **YES** for external API/cloud/models | Vendor Risk Assessment & Executed Contracts |
| **G5** | IAM, MFA & cybersecurity | **YES** | IAM Configuration & Access Control Policy |
| **G6** | Audit logging & real-time monitoring | **YES** | SIEM Configuration & Audit Log Export |
| **G7** | Model risk, procedural fairness & AI comprehension | **YES if AI/ML** | Model Validation Report & AI Comprehension Gate |
| **G8** | Regulatory reporting alignment (HMDA/CRA/1071) | **YES** if regulator-grade fields/export | Regulatory Edit Check Config & Mock Submission File |
| **G9** | Manual review (human-in-the-loop) flagging | **YES** | Exception & Quality Edit Workflow Rules |
| **G10** | Public LLM & uncontrolled third-party boundary | **YES** | Data Classification & AI Guardrails Matrix |

**Docs-only / synthetic offline (no real PII, no external vendors):** design allowed.  
**First cloud host, bank feed, or paid model:** G4 + G5 + G6 + G10 green minimum.

---

## G1 — Data Lineage and Source Mapping

| | |
|--|--|
| **Must pass?** | **YES** — no ingest until origin + transforms mapped |
| **Evidence** | `Data Lineage Document / Mapping Matrix` |
| **Good** | Every reported element → source system + collection point; transforms to regulatory formats documented |
| **Examiner language** | *Monitor assesses data governance for accuracy, completeness, consistency, effectiveness, timeliness… identification and flow of relevant data sources and associated systems.* |
| **Stress** | Unknown source field rejected; silent drop of lineage-required field = FAIL |

---

## G2 — Front-End Validation & Quality Sentinel

| | |
|--|--|
| **Must pass?** | **YES** — no track/report without GIGO gates |
| **Evidence** | `Validation Rules Configuration Record & Test Log` |
| **Good** | Format, range, logical, regulatory rules; incomplete/inconsistent flagged **before** progress |
| **Examiner language** | *Data testing/validation ongoing; sample tests before LAR submission; integrity reviews for trends/outliers before filing.* |
| **Stress** | Bad format, null without NA code, unmapped category |

---

## G3 — Change Management & Secure SDLC

| | |
|--|--|
| **Must pass?** | **YES** |
| **Evidence** | `CI/CD Deployment Audit Trail` |
| **Good** | Change request; **≥2-person** prod approval; SoD; automated CI gates |
| **Examiner language** | *Audit = independent assessment of internal controls… Assess third-party change management for roles, responsibilities, segregation of duties.* |

---

## G4 — Third-Party Vendor Risk & Due Diligence

| | |
|--|--|
| **Must pass?** | **YES** for external APIs, cloud, external models |
| **Evidence** | `Vendor Risk Assessment & Executed Contracts` |
| **Good** | Assessment before onboard; right-to-audit; data handling; return/destruction on termination; incident notify (target ≤72h) |
| **Examiner language** | *Due diligence on all potential third parties before contracts… Contract establishes right to audit, monitor, require remediation.* |

---

## G5 — IAM, MFA & Cybersecurity

| | |
|--|--|
| **Must pass?** | **YES** |
| **Evidence** | `IAM Configuration & Access Control Policy` |
| **Good** | MFA everywhere; RBAC; quarterly access review; no standing admin — JIT for privilege |
| **Examiner language** | *MFA enabled; access reviewed regularly… Sufficient physical/environmental controls for facilities and systems.* |

---

## G6 — Audit Logging & Real-Time Monitoring

| | |
|--|--|
| **Must pass?** | **YES** |
| **Evidence** | `SIEM Configuration & Audit Log Export` |
| **Good** | Continuous logging/alerting; auth + transforms + exceptions; **retain ≥12 months** |
| **Examiner language** | *Logging/alerting across endpoints, servers, cloud… Third party retains timely accurate comprehensive records for bank monitoring.* |

---

## G7 — Model Risk, Procedural Fairness & AI Comprehension

| | |
|--|--|
| **Must pass?** | **YES if** AI/ML for credit/eligibility, generative UX, or compliance monitoring |
| **Evidence** | `Model Validation Report & AI Comprehension Gate` |
| **Good** | Procedural fairness tests; comprehension gate; no black-box to prod |
| **Examiner language** | *ECOA/Reg B — no different underwriting standards by demographic group… CEC regularization at model development…* |
| **Default v1** | **No AI on bank exam path** → signed **N/A — no AI** until model proposed |

---

## G8 — Regulatory Reporting Alignment (HMDA / CRA / 1071)

| | |
|--|--|
| **Must pass?** | **YES** if track/extract for regulatory or regulator-grade export |
| **Evidence** | `Regulatory Edit Check Configuration & Mock Submission File` |
| **Good** | Fields map to current FFIEC/CFPB specs (pin year/edition); syntactical + validity + quality edits **before** progress |
| **Examiner language** | *Validations ensure entries correct and ready to submit… Quality edits check expected values in fields/combinations.* |
| **CBA note** | Product is CBA/consent-order reporter, not full HMDA LAR filer — **edit-check discipline still required** where we claim alignment |

---

## G9 — Manual Review (Human-in-the-Loop) Flagging Control  
*(Part 3 — NEW)*

| | |
|--|--|
| **Must pass before start?** | **YES** — no unreviewed high-stakes exception or silent discard of anomalous data |
| **Evidence artifact** | `Exception & Quality Edit Workflow Rules` |
| **What “good” looks like** | Reasonableness / quality-edit / policy-exception triggers **pause** and **flag**. Human must document justification or correction; system logs **reviewer_id**, **timestamp**, **rationale** before record proceeds |
| **Examiner-facing language** | *“The loan/application register cannot be submitted until the filer either confirms the accuracy of all values flagged by quality edits… or corrects the flagged values.”* *“Records detailing policy exceptions or overrides, exception reporting and monitoring processes.”* |
| **CBA-Enterprise mapping** | `man_review_status` lock; Verify `needs_human_review`; Report **file** blocked while open quality flags; M4 anomalies never auto-prove |
| **Stress** | Auto-clear flag without reviewer = FAIL; proceed-to-file with open exception = FAIL |

**Artifact path:** `docs/compliance/artifacts/EXCEPTION_AND_QUALITY_EDIT_WORKFLOW.md`

---

## G10 — Public LLM & Uncontrolled Third-Party Boundary Control  
*(Part 3 — NEW)*

| | |
|--|--|
| **Must pass before start?** | **YES** |
| **Evidence artifact** | `Data Classification & AI Guardrails Matrix` |
| **What “good” looks like** | Technical blockers (redaction/hash gateways) before data leaves controlled env. **NEVER** enter public LLM or uncontrolled third party: (1) PII — SSN, exact KYC/AML, account numbers, biometrics; (2) private non-public federal info / unredacted consumer credit files; (3) proprietary source / infra configs; (4) internal risk assessments, compliance vulnerability reports, **SAR** data |
| **Examiner-facing language** | *“Prohibit the third party and its subcontractors from using or disclosing the bank’s information, except as necessary to provide the contracted activities or comply with legal requirements.”* *“The AI assistant accesses strictly controlled information; this use case is within the scope of FedRAMP.”* (pattern: controlled scope, not casual public AI) |
| **CBA-Enterprise mapping** | Token/local-compute law; G4 subprocessors; synthetic-only for demos; Ollama/local for redacted text only |
| **Stress** | Attempted export of restricted class to public model endpoint = BLOCK + LOG |

**Artifact path:** `docs/compliance/artifacts/DATA_CLASSIFICATION_AND_AI_GUARDRAILS_MATRIX.md`

---

## Phase freeze rules

```
IF regulated data OR external vendor path:
  REQUIRE G1–G6, G9, G10 GREEN
  REQUIRE G7 GREEN or signed N/A-no-AI
  REQUIRE G8 GREEN if regulator-grade fields/export in scope
THEN open Phase 1 (M1+M3) on non-prod → stress → next phase
ELSE (docs + synthetic offline only):
  Design allowed; scoreboard may remain OPEN with plan dates
```

| Phase | Modules | Extra gates |
|-------|---------|-------------|
| 0 | Controls | Full G1–G10 |
| 1 | M1 + M3 | G1, G2, G8, G9 (file lock), G10 |
| 2 | M2 | G2 + G9 on quality edits |
| 3 | M4 | G7 if ML; G9 human review queue |
| 4 | M5 | G5/G6/G10 elevated PII |

---

## Scoreboard

| Gate | Status | Evidence path | Owner | Date |
|------|--------|---------------|-------|------|
| G1 Lineage | ⬜ OPEN | | | |
| G2 Validation | ⬜ OPEN | | | |
| G3 SDLC/CI | ⬜ OPEN | | | |
| G4 Vendor DD | ⬜ OPEN | | | |
| G5 IAM/MFA | ⬜ OPEN | | | |
| G6 Audit/SIEM | ⬜ OPEN | | | |
| G7 Model/AI | ⬜ OPEN / N/A | | | |
| G8 HMDA/CRA/1071 | ⬜ OPEN | | | |
| G9 Human-in-loop | ⬜ OPEN | | | |
| G10 LLM boundary | ⬜ OPEN | | | |

**Phase-0 overall:** 🔴 **NOT GREEN** (law complete; evidence not filled)

---

## Research ops note (NotebookLM)

Input token limits apply. Split long research questions (as Commander did). **Always reassemble answers into this checklist + `DATA_PLANE_SPEC.md`** so construction has one freeze law, not three chat fragments.
