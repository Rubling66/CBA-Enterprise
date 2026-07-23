---
type: phase-0-evidence
gate: G10
product: CBA-Enterprise
status: DRAFT — Commander research absorbed; technical blockers still OPEN
date: 2026-07-23
agent: engineer-grok
source: Regulatory TPRM + AI security incident patterns (Commander research)
---

# G10 — Data Classification & AI Guardrails Matrix

**Gate:** Public LLM & Uncontrolled Third-Party Boundary Control  
**Must pass before start?** **YES**  
**Parent law:** `docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md` (v3)  
**Related:** Token / local-compute law · OCC 2013-29 confidentiality · `DATA_PLANE_SPEC.md`

---

## 1. Purpose

Establish **strict data classification guardrails** so bank, consumer, and agency confidential information **never** enters:

- Public LLMs  
- Cloud-based coding agents  
- Uncontrolled third-party systems  

This artifact is examiner-facing evidence for **G10** and a binding ops rule for Hermes, Grok, and all builders.

---

## 2. NEVER list (absolute)

The following **must NEVER** be entered into a public LLM, cloud-based coding agent, or uncontrolled third party:

### 2.1 Personally Identifiable Information (PII) & sensitive consumer data

Includes (not exhaustive):

| Class | Examples |
|-------|----------|
| Identity | SSN, PAN, driver’s license, passport |
| Banking | Account numbers, routing where linked to person, cards |
| KYC/AML | Exact KYC/AML payloads, biometric data |
| Credit | Unredacted credit files / full credit reports |
| Regulatory IDs | Application/borrower UIDs that embed or reveal applicant identity |

**If a model needs transaction/user context:** rigorously **tokenize, mask, or redact** so the model **never** sees the real identifier.  
**Small business / 1071-style UIDs:** scrub any element that could **directly identify** applicant or borrower before any transmission outside the controlled plane.

### 2.2 Live credentials & security secrets

| Never paste / upload |
|----------------------|
| API keys |
| Database passwords |
| SSH private keys |
| `.env` / env dumps |
| Cloud access tokens |
| Webhook secrets |

**Incident pattern (ops awareness):** Cloud AI coding agents have been involved in cases where **unredacted `.env` files and SSH keys** were captured or uploaded to uncontrolled cloud storage. Treat every cloud agent as **hostile to secrets by default**.

**Rule:** Secrets live in secret managers / local env **not** in chat, not in agent context, not in committed sample payloads with real values.

### 2.3 Proprietary source code & infrastructure configurations

| Never feed to public LLMs without redaction policy |
|-----------------------------------------------------|
| Internal repos with proprietary bank/CBA logic |
| Internal network URLs, IPs, VPN configs |
| Customer-bearing code paths with live data hooks |
| Infra-as-code with real account IDs / keys |

**Preference for CBA-Enterprise and bank work:**

| Tool class | Allowed? |
|------------|----------|
| **Local** models (Ollama, LM Studio, air-gapped) | **Preferred** — data stays on machine |
| Public Copilot / cloud Claude Code / cloud Grok Build on **restricted** trees | **Avoid** for bank/PII/secret paths |
| Public chatbots on **already-public** text only | OK |

### 2.4 Sensitive federal & pre-decisional information

| Never |
|-------|
| Non-public federal information requiring strict access control |
| Pre-decisional / deliberative material not cleared for public |
| FedRAMP-scoped operational detail inappropriate for public AI |
| Internal emails/databases with non-public federal content |

Public AI chatbots/search: **only** information that is **already public** or **strictly non-sensitive**.

### 2.5 Confidential banking & risk operations data

| Never |
|-------|
| **SARs** (Suspicious Activity Reports) and related BSA materials |
| Internal risk assessments (bank or vendor) |
| Compliance **vulnerability** reports |
| Exam confidential / Matters Requiring Attention detail |
| Live bank disbursement files with customer identifiers |

**Contract rule (G4 link):** Any third-party tech provider must be **prohibited** from using or disclosing confidential banking and customer information except as necessary to perform contracted services or as required by law — **no training reuse, no resale, no public model fine-tune on bank data**.

---

## 3. Classification matrix (quick ops)

| Class | Examples | Public LLM | Local LLM | Cloud coding agent | External vendor (contracted) |
|-------|----------|------------|-----------|--------------------|------------------------------|
| **Public** | Marketing copy, published regs, synthetic samples | OK | OK | OK | OK |
| **Internal** | Non-secret process docs, redacted architecture | Prefer local | OK | Case-by-case redaction | Under DPA |
| **Bank confidential** | Commitments, disbursements, reports | **NEVER** | Redacted only | **NEVER** | Contract + encryption |
| **Restricted PII** | SSN, accounts, KYC, credit | **NEVER** | **NEVER** raw | **NEVER** | Minimize + legal basis |
| **Secrets** | Keys, `.env`, SSH | **NEVER** | **NEVER** in prompts | **NEVER** | Secret manager only |
| **BSA / SAR / exam** | SARs, vuln reports | **NEVER** | **NEVER** | **NEVER** | Statutory channels only |

---

## 4. Technical blockers (required for G10 GREEN)

| Control | Intent | Status |
|---------|--------|--------|
| PII redaction / tokenization gateway before any egress | Model never sees real IDs | ⬜ OPEN |
| Secret scanning in CI (block key patterns) | Stop commit/leak of secrets | ⬜ OPEN |
| `.gitignore` + pre-commit for `.env` | No env in git | ⬜ OPEN (repo hygiene) |
| Documented local-only AI path (Ollama) for CBA work | Data never leaves machine | ⬜ OPEN (policy written; prove in runbook) |
| Subprocessor list excludes “public LLM training” | G4 contracts | ⬜ OPEN |
| Agent instructions: refuse paste of SAR/PII/secrets | Human+agent discipline | ✅ This matrix |

**G10 GREEN only when technical blockers are implemented or formally waived for synthetic-only phase with Commander sign-off.**

---

## 5. Allowed patterns (safe)

| Pattern | Rule |
|---------|------|
| Synthetic sample data under `data/samples/` | Fabricated; no real people/banks |
| Public OCC/FFIEC text | Already public |
| Redacted architecture diagrams | No secrets/URLs |
| Local Ollama on **redacted** or synthetic text | On-box only |
| Discussing control *names* (e.g. “we need MFA”) | No customer payloads |

---

## 6. Examiner-facing language (cite pack)

- *Prohibit the third party and its subcontractors from using or disclosing the bank’s information, except as necessary to provide the contracted activities or comply with legal requirements.*  
- *AI assistants should access strictly controlled information; regulated use cases require authorized environments (e.g. FedRAMP-scoped patterns), not public consumer chatbots.*  
- Aligns with OCC 2013-29 confidentiality and ongoing monitoring of fourth parties.

---

## 7. Scoreboard link

| Gate | This artifact | Status |
|------|---------------|--------|
| **G10** | This file | 🟡 **POLICY DRAFT** — technical blockers OPEN |

When blockers land, update status → 🟢 GREEN and date the scoreboard in `PHASE-0_ACCEPTANCE_CHECKLIST.md`.
