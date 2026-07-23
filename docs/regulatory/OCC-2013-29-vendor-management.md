---
type: regulatory-architecture
product: CBA-Enterprise
status: pre-construction
date: 2026-07-23
agent: engineer-grok
---

# Regulatory Architecture — Vendor Management Spine

**Thesis:** Banks do not buy a dashboard first. They buy a **third party that already fits OCC 2013-29, FFIEC IT, and SOC 2 examination language**. That spine **is** the architecture.

**Code status:** None. Framework only.

---

## 1. OCC Bulletin 2013-29 — Third-Party Relationships

Lifecycle every bank must run for CBA-Enterprise:

| Phase | Bank duty | CBA-Enterprise posture (v1 must show) |
|-------|-----------|----------------------------------------|
| **Planning** | Define activity, risk, alternatives | Written purpose: *CBA obligation tracking + regulator-ready reporting only*. No core banking, no payments rail. |
| **Due diligence** | Assess vendor before contract | Due-diligence packet: security program, data flows, subprocessors, BCP, insurance placeholders, sample report, audit rights language |
| **Contract** | Rights, SLAs, data ownership, audit, exit | Bank owns bank data; we process under DPA; right-to-audit; termination assistance + certified wipe |
| **Ongoing monitoring** | Continuous risk oversight | Access reviews, change log, backup/restore proof, incident notify window, annual attest |
| **Termination** | Exit without stranding bank | Full export of obligations/disbursements/reports + wipe cert within contracted days |

### Concentration / fourth parties
- Declare **every** subprocessor (host, DNS, email, analytics, AI).
- **Rule:** No public LLM on raw bank or consumer PII. Local/redacted analysis only unless bank-approved sandbox.
- Prefer minimal stack for v1 (host + DB + auth).

### Confidentiality
| Class | Examples | Controls |
|-------|----------|----------|
| Public | Filed sample methodology (synthetic) | Open |
| Bank confidential | Commitments, disbursements, internal IDs | Encrypt transit/rest; bank-scoped roles |
| Restricted | Consumer PII in Gate | Minimize; retention schedule; separate access |

---

## 2. FFIEC IT Examination Handbook (alignment)

Use examiner vocabulary in runbooks and architecture:

| Theme | Architecture requirement |
|-------|---------------------------|
| Information security | Asset inventory, annual risk assessment, MFA, least privilege |
| Outsourcing / third-party | Same lifecycle as OCC 2013-29; we supply artifacts banks file |
| Development / acquisition | Dev / stage / prod; change control log before prod promote |
| Operations | Job monitoring (ingest/track/report), alert classes |
| Business continuity | RTO/RPO stated; dependency map; restore test cadence |
| Audit | Immutable audit trail store; auditor read-only role |

---

## 3. SOC 2 readiness (Type I design → Type II later)

| TSC | Product shape |
|-----|----------------|
| **Security** | Roles: `bank_admin`, `bank_analyst`, `vendor_operator`, `auditor_ro`. No shared creds. Separate prod. |
| **Availability** | Hosted SLA; daily backup; documented restore drill |
| **Processing integrity** | **Immutable report packages** once “filed”; versioned templates; no silent rewrite |
| **Confidentiality** | Classification + encryption + tenant isolation |
| **Privacy** (if Gate live) | Purpose limitation, retention, DSAR path |

**Moat language for sales:** “Vendor-management controls are product requirements, not a later cert bolt-on.”  
**Honesty:** Readiness plan ≠ certified. Do not claim SOC 2 certified until auditor issues report.

---

## 4. HMDA-adjacent handling (PII, retention, logging)

CBA reporting is **not** HMDA filing software, but banks and examiners will analogize.

| Topic | Requirement |
|-------|-------------|
| Purpose limitation | Collect only fields needed for obligation/disbursement/report/eligibility |
| Access logging | Who viewed/exported restricted rows; retain logs per policy |
| Retention | Obligation/report retention ≥ bank/consent-order need; PII shorter where lawful |
| Aggregation | Prefer tract/MSA aggregates in reports; parcel/consumer only when Gate + legal basis |
| Quality | Document mapping rules for categories (avoid silent HMDA-like miscoded fields) |

---

## 5. Module × regulation heat

| Module | Regulatory heat | Gate before build |
|--------|-----------------|-------------------|
| M1 Ingest | Medium | Data classes + contract scope |
| M2 Track | Medium–high | Idempotent events + bank feed agreement |
| M3 Report | High (examiner-facing) | Immutability + audit trail store |
| M4 Verify | High (method risk) | Methods paper + fourth-party list |
| M5 Gate | **Highest** (PII) | DPA + retention + privacy TSC |

**Build order:** Phase 0 controls → **M1+M3** → M2 → M4 → **M5 last**.

---

## 6. Phase-0 acceptance checklist (binary)

| # | Control | Pass evidence |
|---|---------|---------------|
| 1 | Purpose statement limited to CBA reporting | README + contract exhibit |
| 2 | Data classification doc | This file §1 + `data-model.md` |
| 3 | Role model defined | `system-architecture.md` |
| 4 | Subprocessor list v1 | Table in due-diligence packet |
| 5 | Incident notify window stated | Runbook stub |
| 6 | Exit/export path described | Termination section |
| 7 | No public LLM on bank data | Token/local-compute policy cite |
| 8 | Audit trail required for filed reports | Data model AuditEvent |

**Rule:** No feature phase starts until 1–8 are green on paper.

---

## 7. Cross-links

- System context: `docs/architecture/system-architecture.md`
- Entities: `docs/architecture/data-model.md`
- UI surfaces: `docs/architecture/dashboard-wireframe.md`
- Prior map: `DCONSULT/05_Deliverables/CBA_Enterprise/2026-07-23_CBA_REGULATORY_ARCHITECTURE_MAP.md`
