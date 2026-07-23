---
type: phase-0-acceptance
product: CBA-Enterprise
status: LOCKED_DRAFT v2 — Commander research (part 1 + continuation)
date: 2026-07-23
agent: engineer-grok
revision: 2
source: Commander Phase-0 checklist (NotebookLM / regulatory corpus)
---

# PHASE-0 ACCEPTANCE CHECKLIST  
## Core Compliance & Architecture Gates (v2)

**Law:** No feature phase (M1–M5) may **process bank or consumer regulated data** in a shared/prod-like environment until every control marked **MUST PASS BEFORE START = YES** is green with evidence.

**Build order:** Phase 0 → **M1 Ingest + M3 Report** → M2 Track → M4 Verify → M5 Gate.  
**Stress fail = freeze next phase.**

**Related:**  
- `docs/regulatory/OCC-2013-29-vendor-management.md`  
- `docs/architecture/system-architecture.md`  
- `docs/architecture/data-model.md`  
- `docs/compliance/artifacts/` (evidence stubs)

**Revision note (v2):** Continuation absorbed — vendor risk elevated to **YES** for any external API/cloud/model path; IAM + audit restated; **G7 Model Risk / AI Fairness** and **G8 HMDA/CRA/1071 alignment** added. Prior “G5 parallel for all internal build” is **narrowed**: docs/scaffold OK; **no external integration** without G4 green.

---

## Gate summary

| # | Control | Must pass before start? | Evidence artifact | Blocks |
|---|---------|-------------------------|-------------------|--------|
| **G1** | Data lineage & source mapping | **YES** | Data Lineage Document / Mapping Matrix | Any **Ingest** of real/bank feeds |
| **G2** | Front-end validation & quality sentinel | **YES** | Validation Rules Config Record & Test Log | **Track** + **Report** on live data |
| **G3** | Change management & secure SDLC | **YES** | CI/CD Deployment Audit Trail | Deploys to envs holding financial/consumer data |
| **G4** | Third-party vendor risk & due diligence | **YES** *for external APIs, cloud, external models* | Vendor Risk Assessment & Executed Contracts | Integrations, subprocessors, hosted prod with third parties |
| **G5** | IAM, MFA & cybersecurity | **YES** | IAM Configuration & Access Control Policy | Any deploy holding regulated data |
| **G6** | Audit logging & real-time monitoring | **YES** | SIEM Configuration & Audit Log Export | Features processing financial data |
| **G7** | Model risk, procedural fairness & AI comprehension | **YES** *if AI/ML used* | Model Validation Report & AI Comprehension Gate | Credit/eligibility AI, generative UX, ML compliance monitoring |
| **G8** | Regulatory reporting alignment (HMDA/CRA/1071) | **YES** *if fields feed regulatory-style submit/export* | Regulatory Edit Check Config & Mock Submission File | Track/extract for regulatory or regulator-adjacent schemas |

**Docs-only / synthetic local scaffold:** allowed without full green **if** no external network vendors and no real bank/consumer PII.  
**First cloud host, bank API, or paid model API:** G4 + G5 + G6 required green.

---

## G1 — Data Lineage and Source Mapping Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no ingestion until origin and transformation rules are mapped |
| **Evidence artifact** | `Data Lineage Document / Mapping Matrix` |
| **What “good” looks like** | Every reported data element traces to exact source system and collection point; all field transformations between source and regulatory reporting formats documented |
| **Examiner-facing language** | *“The Monitor will assess the Bank’s data governance framework for accuracy, completeness, consistency, effectiveness, and timeliness of TD Bank’s AML data processing… including the identification and flow of relevant data sources and associated systems.”* |
| **CBA-Enterprise mapping** | Commitment/Disbursement/ReportLine lineage; versioned bank-code → taxonomy map; `AuditEvent` on remap |
| **Stress** | Unknown source field rejected; silent drop of required lineage field = FAIL |

**Artifact path:** `docs/compliance/artifacts/DATA_LINEAGE_MAPPING_MATRIX.md`

---

## G2 — Front-End Validation & Quality Sentinel Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no tracking/reporting without automated GIGO gates |
| **Evidence artifact** | `Validation Rules Configuration Record & Test Log` |
| **What “good” looks like** | Multi-layer validation: format, range, logical relationships, regulatory business rules (HMDA/ECOA-adjacent where applicable). Incomplete/inconsistent rows flagged **before** workflow progress |
| **Examiner-facing language** | *“Data testing and validation are ongoing processes. Before LAR submission, compliance teams should perform audits, or sample tests, on the data… Systemic data integrity reviews of your CRA and HMDA LARs can also be very helpful in identifying data trends and outlier values…”* |
| **CBA-Enterprise mapping** | Track quarantine; Report cannot **file** with open critical validation fails; category ∈ taxonomy |
| **Stress** | Bad geo/ZIP rules, negative $, unmapped category, duplicate idempotency key |

**Artifact path:** `docs/compliance/artifacts/VALIDATION_RULES_AND_TEST_LOG.md`

---

## G3 — Change Management & Secure Development Lifecycle (SDLC)

| | |
|--|--|
| **Must pass before start?** | **YES** — no financial/consumer-data env deploys without auditable review |
| **Evidence artifact** | `CI/CD Deployment Audit Trail` |
| **What “good” looks like** | Formal change request/approval; **≥ two-person** production approval; segregation of duties (author ≠ sole prod approver); automated test gates in CI/CD |
| **Examiner-facing language** | *“An audit is an independent assessment and validation of an institution’s system of internal controls…”* *“Assess the third party’s change management processes to ensure… segregation of duties are in place.”* |
| **CBA-Enterprise mapping** | Protected main; PR required; `.github/workflows` gates; no solo force-push to bank-facing env |
| **Stress** | Deploy without PR = blocked; red tests = blocked |

**Artifact path:** `docs/compliance/artifacts/CICD_DEPLOYMENT_AUDIT_TRAIL.md`

---

## G4 — Third-Party Vendor Risk & Due Diligence Control  
*(Continuation §4 — elevated)*

| | |
|--|--|
| **Must pass before start?** | **YES** for any feature integrating **external APIs, cloud services, or external models** |
| **Evidence artifact** | `Vendor Risk Assessment & Executed Contracts` |
| **What “good” looks like** | Standardized vendor assessment **before** onboarding: security posture, financial condition, compliance status. Contracts include **right-to-audit**, strict data handling, **data return/destruction on termination**, incident notification (target ≤ 72h), remediation rights |
| **Examiner-facing language** | *“A bank should conduct due diligence on all potential third parties before selecting and entering into contracts or relationships.”* *“Ensure that the contract establishes the bank’s right to audit, monitor performance, and require remediation when issues are identified.”* |
| **CBA-Enterprise mapping** | Hostinger / Render / IONOS / any LLM API / city data vendors = register entries; fourth-party list in OCC posture doc |
| **Parallel allowed** | Pure local docs + synthetic offline design **without** external network vendors |
| **Stress** | Undeclared subprocessor in data path = FAIL |

**Artifact path:** `docs/compliance/artifacts/VENDOR_RISK_REGISTER.md`

---

## G5 — Identity, Access Management (IAM) & Cybersecurity Control  
*(Continuation §5)*

| | |
|--|--|
| **Must pass before start?** | **YES** — no deploy without zero-trust boundaries and access governance |
| **Evidence artifact** | `IAM Configuration & Access Control Policy` |
| **What “good” looks like** | MFA on all systems, cloud consoles, and internal dashboards; RBAC + least privilege; **quarterly** access reviews; **no standing admin** — JIT for privileged ops |
| **Examiner-facing language** | *“Ensure MFA is enabled for all systems and user access is reviewed regularly.”* *“Evaluate whether the third party has sufficient physical and environmental controls to ensure the safety and security of its facilities, technology systems, and employees.”* |
| **CBA-Enterprise mapping** | Roles: `bank_admin`, `bank_analyst`, `auditor_ro`, `vendor_operator`; tenant isolation; MFA before prod secrets |
| **Stress** | Cross-tenant access → deny; access without MFA → deny |

**Artifact path:** `docs/compliance/artifacts/IAM_ACCESS_CONTROL_POLICY.md`

---

## G6 — Audit Logging & Real-Time Monitoring Control  
*(Continuation §6)*

| | |
|--|--|
| **Must pass before start?** | **YES** — no financial data processing without immutable searchable trail |
| **Evidence artifact** | `SIEM Configuration & Audit Log Export` |
| **What “good” looks like** | Continuous logging/alerting across endpoints, servers, cloud apps; captures authentication, data transformations, system exceptions; **retain ≥ 12 months** for post-incident and exams |
| **Examiner-facing language** | *“Implement logging and alerting across endpoints, servers, and cloud apps.”* *“Ensure that the contract requires the third party to provide and retain timely, accurate, and comprehensive information such as records and reports that allow bank management to monitor performance, service levels, and risks.”* |
| **CBA-Enterprise mapping** | Append-only `AuditEvent`; filed report hashes; export path for bank/auditor |
| **Stress** | Missing auth log on privileged action = FAIL; log tamper detectable |

**Artifact path:** `docs/compliance/artifacts/SIEM_AND_AUDIT_LOG_EXPORT.md`

---

## G7 — Model Risk, Procedural Fairness & AI Comprehension Control  
*(Continuation §7 — NEW)*

| | |
|--|--|
| **Must pass before start?** | **YES if** AI/ML is used for credit/eligibility decisions, generative UX, or compliance monitoring |
| **Evidence artifact** | `Model Validation Report & AI Comprehension Gate` |
| **What “good” looks like** | Models tested for **procedural fairness** (no different reasoning pathways by demographic group). Comprehension gate: structural + semantic context checks before deploy; **no black-box logic** to production without human-reviewable rationale |
| **Examiner-facing language** | *“Under ECOA and Regulation B, lenders are prohibited from applying different underwriting standards to different demographic groups… At the model development stage, CEC [Counterfactual Explanation Consistency] regularization can be incorporated into training pipelines to prevent procedural bias from arising in the first place.”* |
| **CBA-Enterprise mapping** | **Default v1:** no AI in bank exam path or Gate underwriting. If Verify anomaly ML or any scoring is added → full G7 package. Local-compute law: no bank PII to public LLMs. Black-box theorem applies |
| **If no AI in phase** | Mark **N/A — no AI** with signed statement; re-open G7 before first model ships |
| **Stress** | Protected-class path divergence; unexplained score; undeclared model version |

**Artifact path:** `docs/compliance/artifacts/MODEL_VALIDATION_AND_AI_COMPREHENSION_GATE.md`

---

## G8 — Regulatory Reporting & Compliance Alignment Control (HMDA / CRA / 1071)  
*(Continuation §8 — NEW)*

| | |
|--|--|
| **Must pass before start?** | **YES** for features that track or extract data for regulatory submission or regulator-grade export |
| **Evidence artifact** | `Regulatory Edit Check Configuration & Mock Submission File` |
| **What “good” looks like** | Fields map to current FFIEC/CFPB specs as applicable (e.g. HMDA FIG editions, Section **1071** small business lending standards, CRA-relevant aggregates). Automated **syntactical, validity, and quality edits** run **before** data progresses; reduces rejection risk |
| **Examiner-facing language** | *“Data validations are a series of checks that run on a small business lending application register to ensure that the data entries are correct and ready to submit, meaning the data are both internally consistent and consistent with the syntax and logic specified…”* *“Quality: Edits that check whether entries in the individual data fields or combinations of data fields conform to expected values.”* |
| **CBA-Enterprise mapping** | Product is **CBA/consent-order reporting**, not a full HMDA LAR filer — but **taxonomy, geo, and edit-check discipline** must be examiner-grade. Where we claim alignment, pin **spec version + year** (e.g. 2026 FIG). Mock export in `data/samples/` must pass internal edit suite |
| **Stress** | Schema drift vs pinned FIG; quality edit failures auto-block file |

**Artifact path:** `docs/compliance/artifacts/REGULATORY_EDIT_CHECKS_AND_MOCK_SUBMISSION.md`

---

## Phase freeze rules

```
SYNTHETIC / DOCS ONLY (no real PII, no external vendors):
  → Design allowed; mark gates OPEN with plan dates

REGULATED DATA OR EXTERNAL API/CLOUD/MODEL:
  → G1, G2, G3, G4, G5, G6 GREEN required
  → G7 GREEN or signed N/A-no-AI
  → G8 GREEN if regulatory-style fields/export in scope

THEN Phase 1 (M1 + M3) may open on non-prod synthetic → stress → next
```

| Phase | Modules | Extra emphasis |
|-------|---------|----------------|
| 0 | Controls | Full scoreboard |
| 1 | M1 + M3 | G1, G2, G6, G8 (report schema) |
| 2 | M2 | G2 idempotency + G1 event lineage |
| 3 | M4 | G7 if ML; G4 for city data vendors |
| 4 | M5 | G5/G6 elevated PII; G7 if any scoring AI |

---

## Scoreboard (fill as evidence lands)

| Gate | Status | Evidence path | Owner | Date |
|------|--------|---------------|-------|------|
| G1 Lineage | ⬜ OPEN | | | |
| G2 Validation | ⬜ OPEN | | | |
| G3 SDLC/CI | ⬜ OPEN | | | |
| G4 Vendor DD | ⬜ OPEN | | | |
| G5 IAM/MFA | ⬜ OPEN | | | |
| G6 Audit/SIEM | ⬜ OPEN | | | |
| G7 Model/AI fairness | ⬜ OPEN or N/A | | | |
| G8 HMDA/CRA/1071 edits | ⬜ OPEN | | | |

**Phase-0 overall:** 🔴 **NOT GREEN**

---

## Numbering crosswalk (v1 → v2)

| v1 | v2 |
|----|-----|
| G1 Lineage | G1 |
| G2 Validation | G2 |
| G3 SDLC | G3 |
| G5 Vendor (was soft NO) | **G4 Vendor YES for external** |
| G4 IAM | **G5 IAM** |
| G7 Audit | **G6 Audit** |
| G6 Comprehension | Folded into **G7** (AI) + PRD still required for launch |
| — | **G8 Regulatory schemas** NEW |
