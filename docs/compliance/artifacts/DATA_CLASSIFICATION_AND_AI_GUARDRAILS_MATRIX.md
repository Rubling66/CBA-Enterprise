---
type: phase-0-evidence
gate: G10
product: CBA-Enterprise
status: DRAFT — NEVER list + bank redaction playbook absorbed; technical blockers still OPEN
date: 2026-07-23
agent: engineer-grok
source: Regulatory TPRM + bank PII/LLM boundary patterns + AI security incidents (Commander research)
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

## 4. How banks keep PII out of LLMs (implementation playbook)

Multi-layered technical boundaries — **not** “trust the user to be careful.” CBA-Enterprise adopts the same stack for any future model path (and for agent sessions today).

### 4.1 Tokenization and data masking (application level)

| Technique | Behavior |
|-----------|----------|
| **Mask** | Show only last 3–4 digits (or partial EIN); AI never sees full SSN/PAN/EIN |
| **Tokenize** | Replace identifier with irreversible or vault-backed token; model runs logic on token only |
| **Scope** | Applied **at application layer** before any prompt/context assembly |

**Rule:** If the model needs “customer context,” it gets **masked/tokenized** fields only — never raw identifiers.

### 4.2 Redaction gateways and hashing (edge / agent framework)

| Control | Behavior |
|---------|----------|
| **Gateway between internal system and LLM** | All egress prompts pass a redaction layer |
| **Hash user IDs** | Session context carries hashes, not clear IDs |
| **Strip** | Phone, email, free-text PII patterns removed before model receive |

**Architecture pin:** No direct app → public LLM wire. Always: `App → Redaction Gateway → (local or approved) model`.

### 4.3 Automated secret scanners

| Surface scanned | Action |
|-----------------|--------|
| Tool outputs, terminal logs, agent context | Detect API keys, tokens, passwords |
| Redaction pass | Replace with placeholders **before** conversation context |

Blocks accidental leak of credentials and internal infra strings (pairs with G10 NEVER secrets list and known cloud-agent `.env` incident patterns).

### 4.4 Sanitization and synthetic data (training / fine-tune)

| Environment | Rule |
|-------------|------|
| Sandbox model training | Training set **sanitized**; privacy review before use |
| Prefer **fake / synthetic** data | Learn patterns without real customer records |
| Production bank data | **Not** used to train public or uncontrolled models |

Aligns with `data/samples/` synthetic-only demos for CBA-Enterprise.

### 4.5 Application-level and observability redaction

| Tool class | Rule |
|------------|------|
| Session replay / APM / error trackers | Configure **auto-hide** SSN, account, password fields |
| Logs and diagnostics | Developers and tools must not retain raw PII in cleartext |

Even third-party **build/monitor** software is in scope — observability is a fourth-party risk (G4).

### 4.6 Sanitized regulatory identifiers (e.g. Section 1071)

| Requirement | Behavior |
|-------------|----------|
| External regulatory / reporting UIDs | Generated so they **exclude** underlying data that could **directly identify** applicant or borrower |
| Transmission | No embedded name, SSN, account, or address in the UID string |

Cross-link: `DATA_PLANE_SPEC.md` (`uid` begins with LEI, no consumer PII).

---

## 5. Technical blockers (required for G10 GREEN)

| Control | Maps to §4 | Status |
|---------|------------|--------|
| PII redaction / tokenization gateway before any egress | 4.1, 4.2 | ⬜ OPEN |
| Secret scanning on tool/log/context before agent/LLM | 4.3 | ⬜ OPEN |
| `.gitignore` + pre-commit for `.env` | 4.3 | ⬜ OPEN |
| Synthetic-only training/demo samples | 4.4 | 🟡 Policy + `data/samples/` path |
| Observability / session tools PII hide config (when tools exist) | 4.5 | ⬜ OPEN |
| UID generation rules (LEI + no applicant identity) | 4.6 | 🟡 Spec’d in DATA_PLANE_SPEC |
| Documented local-only AI path (Ollama) | Local compute law | ⬜ OPEN (prove in runbook) |
| Subprocessor list excludes public LLM training on bank data | G4 | ⬜ OPEN |
| Agent instructions: refuse SAR/PII/secrets paste | Human+agent | ✅ This matrix |

**G10 GREEN only when technical blockers are implemented or formally waived for synthetic-only phase with Commander sign-off.**

---

## 6. Allowed patterns (safe)

| Pattern | Rule |
|---------|------|
| Synthetic sample data under `data/samples/` | Fabricated; no real people/banks |
| Public OCC/FFIEC text | Already public |
| Redacted architecture diagrams | No secrets/URLs |
| Local Ollama on **redacted** or synthetic text | On-box only |
| Masked last-4 / tokens for internal tooling demos | Never full identifier |
| Discussing control *names* (e.g. “we need MFA”) | No customer payloads |

---

## 7. Examiner-facing language (cite pack)

- *Prohibit the third party and its subcontractors from using or disclosing the bank’s information, except as necessary to provide the contracted activities or comply with legal requirements.*  
- *AI assistants should access strictly controlled information; regulated use cases require authorized environments (e.g. FedRAMP-scoped patterns), not public consumer chatbots.*  
- Aligns with OCC 2013-29 confidentiality and ongoing monitoring of fourth parties.
- Regulatory UIDs must not embed direct applicant/borrower identifiers (1071 / reporting discipline).

---

## 8. Scoreboard link

| Gate | This artifact | Status |
|------|---------------|--------|
| **G10** | This file | 🟡 **POLICY + PLAYBOOK** — technical blockers OPEN |

When blockers land, update status → 🟢 GREEN and date the scoreboard in `PHASE-0_ACCEPTANCE_CHECKLIST.md`.
