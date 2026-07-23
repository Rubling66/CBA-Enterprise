---
type: phase-0-acceptance
product: CBA-Enterprise
status: LOCKED_DRAFT — Commander research absorbed
date: 2026-07-23
agent: engineer-grok
source: Commander Phase-0 checklist (NotebookLM / research repo)
---

# PHASE-0 ACCEPTANCE CHECKLIST  
## Core Compliance & Architecture Gates

**Law:** No feature phase (M1–M5) may **process bank or consumer regulated data in a shared/prod-like environment** until every control marked **MUST PASS BEFORE START = YES** is green with evidence.

**Build order remains:** Phase 0 → **M1 Ingest + M3 Report** → M2 Track → M4 Verify → M5 Gate.

**Related:**  
- `docs/regulatory/OCC-2013-29-vendor-management.md`  
- `docs/architecture/system-architecture.md`  
- `docs/architecture/data-model.md`

---

## Gate summary

| # | Control | Must pass before start? | Evidence artifact | Blocks |
|---|---------|-------------------------|-------------------|--------|
| **G1** | Data lineage & source mapping | **YES** | Data Lineage Document / Mapping Matrix | Any **Ingest** of real/bank feeds |
| **G2** | Front-end validation & quality sentinel | **YES** | Validation Rules Config Record & Test Log | **Track** + **Report** on live data |
| **G3** | Change management & secure SDLC | **YES** | CI/CD Deployment Audit Trail | Any push to envs holding financial/consumer data |
| **G4** | IAM & MFA | **YES** | IAM Configuration & Access Control Policy | Systems **holding** regulated data |
| **G5** | Third-party vendor risk & due diligence | **NO*** | Vendor Risk Register & Executed Contracts | *External data exchanges / subprocessors in path* |
| **G6** | Comprehension gate & design rationale | **YES** | PRD Decision Graph / Launch Readiness Gate | Ship of complex logic / AI-assisted UX |
| **G7** | Audit logging & SIEM | **YES** | SIEM Config & Audit Log Export | Features that process inputs/outputs for examiners |

\*G5: Internal scaffold/docs may proceed; **no vendor integration or bank data exchange** until register + contract clauses are in place.

---

## G1 — Data Lineage and Source Mapping Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no ingestion until origin and transformation rules are mapped |
| **Evidence artifact** | `Data Lineage Document / Mapping Matrix` |
| **What “good” looks like** | Every reported data element traces to exact source system and collection point; all field transformations between source and regulatory reporting formats are documented to prevent downstream integrity failures |
| **Examiner-facing language** | *“The Monitor will assess the Bank’s data governance framework for accuracy, completeness, consistency, effectiveness, and timeliness of TD Bank’s AML data processing… including the identification and flow of relevant data sources and associated systems.”* |
| **CBA-Enterprise mapping** | Obligation/Disbursement/ReportLine fields in `data-model.md`; bank feed → taxonomy map versioned; `AuditEvent` on remap |
| **Stress before M1 green** | Unknown source field rejected; silent drop of required lineage field = FAIL |

**Repo path (to create when filled):** `docs/compliance/artifacts/DATA_LINEAGE_MAPPING_MATRIX.md`

---

## G2 — Front-End Validation & Quality Sentinel Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no tracking/reporting without automated gates against GIGO |
| **Evidence artifact** | `Validation Rules Configuration Record & Test Log` |
| **What “good” looks like** | Multi-layer validation: format (e.g. ZIP rules), range, logical relationships, regulatory business rules (HMDA/ECOA-adjacent constraints where applicable). Incomplete/inconsistent rows **flagged before** workflow progress |
| **Examiner-facing language** | *“Data testing and validation are ongoing processes. Before LAR submission, compliance teams should perform audits, or sample tests, on the data… Systemic data integrity reviews of your CRA and HMDA LARs can also be very helpful in identifying data trends and outlier values that require closer scrutiny and potential correction before filing.”* |
| **CBA-Enterprise mapping** | Track quarantine queue; Report cannot file with open critical validation fails; category ∈ taxonomy invariant |
| **Stress before M2/M3 green** | Bad ZIP, negative $, unmapped category, duplicate idempotency key |

**Repo path:** `docs/compliance/artifacts/VALIDATION_RULES_AND_TEST_LOG.md`

---

## G3 — Change Management & Secure Development Lifecycle (SDLC)

| | |
|--|--|
| **Must pass before start?** | **YES** — no prod/financial-data env deploys without auditable review |
| **Evidence artifact** | `CI/CD Deployment Audit Trail` |
| **What “good” looks like** | Formal change request/approval; **minimum two-person** production approval; segregation of duties (author ≠ sole prod approver); automated test gates in CI/CD |
| **Examiner-facing language** | *“An audit is an independent assessment and validation of an institution’s system of internal controls…”* *“Assess the third party’s change management processes to ensure that clear roles, responsibilities, and segregation of duties are in place.”* |
| **CBA-Enterprise mapping** | `.github/workflows` + protected `master`/`main`; PR required; no force-push prod; eng ≠ solo release for bank-facing env |
| **Stress** | Deploy without PR = blocked; tests red = blocked |

**Repo path:** `docs/compliance/artifacts/CICD_DEPLOYMENT_AUDIT_TRAIL.md` (+ live GitHub Actions evidence)

---

## G4 — Identity, Access Management (IAM) & MFA

| | |
|--|--|
| **Must pass before start?** | **YES** — no regulated data store without zero-trust boundaries |
| **Evidence artifact** | `IAM Configuration & Access Control Policy` |
| **What “good” looks like** | RBAC + least privilege; no standing god-admin; JIT for privileged ops; **MFA** on production systems, cloud consoles, and internal dashboards |
| **Examiner-facing language** | *“Evaluate whether the third party has sufficient physical and environmental controls…”* *“Ensure management takes appropriate actions to remedy significant deterioration in performance or address changing risks…”* |
| **CBA-Enterprise mapping** | Roles: `bank_admin`, `bank_analyst`, `auditor_ro`, `vendor_operator`; tenant filter on every query; MFA required before prod secrets |
| **Stress** | Cross-tenant IDOR → 0 rows/403; access without MFA → denied |

**Repo path:** `docs/compliance/artifacts/IAM_ACCESS_CONTROL_POLICY.md`

---

## G5 — Third-Party Vendor Risk & Due Diligence Control

| | |
|--|--|
| **Must pass before start?** | **NO** (internal feature **design/scaffold** may run in parallel) |
| **Still gates** | Any **external integration**, subprocessor processing bank/consumer data, or bank data exchange |
| **Evidence artifact** | `Vendor Risk Register & Executed Contracts` |
| **What “good” looks like** | Full registry of in-scope vendors (service, risk class); templates with security terms; executed agreements + security annex; **incident notification ≤ 72 hours**; bank right-to-audit / remediation clauses |
| **Examiner-facing language** | *“Ensure that the contract establishes the bank’s right to audit, monitor performance, and require remediation… periodic independent internal or external audits of the third party, and relevant subcontractors…”* |
| **CBA-Enterprise mapping** | Host, DNS, email, any AI API = subprocessors; Hostinger/Render/IONOS listed; no silent fourth party |

**Repo path:** `docs/compliance/artifacts/VENDOR_RISK_REGISTER.md`

---

## G6 — Comprehension Gate & Design Rationale Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no ship of AI-generated UX or opaque complex logic without org understanding |
| **Evidence artifact** | `PRD Decision Graph / Launch Readiness Gate` |
| **What “good” looks like** | Multi-function go/no-go: evidence present, thresholds met, role approvals recorded; **rationale chain** for trade-offs; no artifact crosses a functional boundary without comprehension context attached |
| **Examiner-facing language** | *“Proper documentation and reporting facilitates oversight, accountability, monitoring, and risk management associated with third-party relationships.”* *“Review of a potential third party before signing a contract helps ensure… risks… consistent with the bank’s risk appetite.”* |
| **CBA-Enterprise mapping** | Bridge DECISION files; phase gate tables; black-box rule on Verify ML; no “AI insights” on bank exam path in v1 |
| **Stress** | Launch without signed Decision Graph = NO-GO |

**Repo path:** `docs/compliance/artifacts/PRD_DECISION_GRAPH_AND_LAUNCH_GATE.md`

---

## G7 — Audit Logging & SIEM Control

| | |
|--|--|
| **Must pass before start?** | **YES** — no process of inputs/outputs without immutable examiner trail |
| **Evidence artifact** | `SIEM Configuration & Audit Log Export` |
| **What “good” looks like** | Immutable, searchable logging/alerting across apps and infra; captures auth, data transformations, model prediction/changes; **retain ≥ 12 months** |
| **Examiner-facing language** | *“Ensure that the contract requires the third party to provide and retain timely, accurate, and comprehensive information such as records and reports that allow bank management to monitor performance, service levels, and risks.”* |
| **CBA-Enterprise mapping** | `AuditEvent` append-only; filed report hashes; export of audit log for bank/auditor; SIEM or equivalent export path |
| **Stress** | Missing auth log on admin action = FAIL; log tamper attempt detectable |

**Repo path:** `docs/compliance/artifacts/SIEM_AND_AUDIT_LOG_EXPORT.md`

---

## Phase freeze rules (construction methodology)

```
IF G1 AND G2 AND G3 AND G4 AND G6 AND G7 are GREEN:
    MAY open Phase 1 (M1 Ingest + M3 Report) on non-prod with synthetic data
ELSE:
    FREEZE feature work that touches regulated data paths

IF Phase 1 stress suite PASS:
    MAY open Phase 2 (M2 Track)
...
G5 GREEN required before first bank feed or production subprocessor data path
```

| Phase | Modules | Extra gates |
|-------|---------|-------------|
| 0 | Controls only | G1–G4, G6–G7 YES; G5 tracking started |
| 1 | M1 + M3 | G1, G2, G7 proven on synthetic → filed package immutability |
| 2 | M2 | G2 idempotency + lineage for disbursement events |
| 3 | M4 | G6 methods comprehension; G5 for city data vendors |
| 4 | M5 | G4+G7 elevated PII; privacy retention |

---

## Scoreboard (fill as artifacts land)

| Gate | Status | Evidence path | Owner | Date |
|------|--------|---------------|-------|------|
| G1 Lineage | ⬜ OPEN | | | |
| G2 Validation | ⬜ OPEN | | | |
| G3 SDLC/CI | ⬜ OPEN | | | |
| G4 IAM/MFA | ⬜ OPEN | | | |
| G5 Vendor DD | ⬜ OPEN (parallel OK) | | | |
| G6 Comprehension | ⬜ OPEN | | | |
| G7 Audit/SIEM | ⬜ OPEN | | | |

**Phase-0 overall:** 🔴 **NOT GREEN** until scoreboard shows required YES gates green.

---

## Next construction actions (still pre-code OK)

1. Create empty stubs under `docs/compliance/artifacts/` for each evidence artifact.  
2. Hermes: wire CI skeleton so G3 has a real audit trail path.  
3. Grok: no engine feature code until Phase-0 scoreboard policy is accepted by Commander/Hermes DECISION.  
4. NotebookLM: continue Q2/Q3 against this checklist as the freeze law.
