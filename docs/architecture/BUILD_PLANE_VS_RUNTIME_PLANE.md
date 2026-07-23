---
type: architecture
product: CBA-Enterprise
status: pre-construction
date: 2026-07-23
agent: engineer-grok
---

# Build Plane vs Runtime Plane

**Problem this solves:** Brochure stacks that put “Grok / cloud AI” in the same box as CRA/HMDA/1071 **production data** fail Phase-0 **G10** and OCC third-party confidentiality.

**Rule:** Grok Build **builds** the product. The product **enforces** compliance. Bank PII **never** enters Grok (or any public LLM).

---

## 1. Diagram

```text
┌─────────────────────────────────────────────────────────┐
│  BUILD PLANE (developers + Grok Build)                  │
│  • Repo: Rubling66/CBA-Enterprise                       │
│  • AGENTS.md Phase-0 / G10                              │
│  • Plan Mode → human approve large changes              │
│  • Data: synthetic, public regs, redacted docs          │
│  • NEVER: .env, SAR, raw LAR, real customer files       │
└───────────────────────────┬─────────────────────────────┘
                            │ git PR only
                            ▼
┌─────────────────────────────────────────────────────────┐
│  CI PLANE (G3 SDLC)                                     │
│  • Tests, secret scan, optional headless code review    │
│  • ≥2-person approval to bank-facing env                │
└───────────────────────────┬─────────────────────────────┘
                            │ deploy versioned artifacts
                            ▼
┌─────────────────────────────────────────────────────────┐
│  RUNTIME PLANE (bank data) — NO public LLM              │
│  • M1 Ingest → validate → register → M3 Report          │
│  • G9 human review queue · G6 immutable audit            │
│  • Optional LOCAL model only on redacted/aggregate text │
│  • MCP tools may return TOKENIZED or AGGREGATE only     │
└───────────────────────────┬─────────────────────────────┘
                            │ G4 green later
                            ▼
┌─────────────────────────────────────────────────────────┐
│  INTEGRATIONS                                           │
│  v1: SFTP/CSV + checksum                                │
│  later: Jack Henry / Fiserv / FIS under contract + DPA  │
└─────────────────────────────────────────────────────────┘
```

---

## 2. What each plane may hold

| Data class | Build plane | Runtime plane | Public LLM / Grok |
|------------|-------------|---------------|-------------------|
| Synthetic samples | Yes | Yes (demo) | Yes |
| Public regulations | Yes | Yes | Yes |
| Bank commitments / disbursements (live) | **No** | Yes | **Never** |
| Consumer PII | **No** | Yes (minimized, Gate) | **Never** |
| Secrets / `.env` | Local secret mgr only | Secret mgr | **Never** |
| SAR / BSA | **No** | Statutory only | **Never** |

---

## 3. Grok Build — allowed uses

| Use | Allowed? |
|-----|----------|
| Write docs, schemas, tests on synthetic | **Yes** |
| Implement engine modules per BUILD-ORDER | **Yes** (after Phase-0 policy) |
| PR review of **code** for drift/secrets patterns | **Yes** (headless CI optional) |
| Plan Mode for multi-file changes | **Yes** + human approve |
| Query production DB / raw bank files | **No** |
| “Analyze lending disparities” on real assessment areas | **No** unless pre-aggregated/tokenized **outside** Grok |
| Act as compliance decision of record | **No** — deterministic engine is SoR |

---

## 4. MCP (if used)

MCP is a **transport**, not a magic air gap.

| Rule | |
|------|--|
| MCP tools return | Aggregates, tokens, pass/fail of edits — **not** raw PII rows |
| If a tool returns raw SSN | Architecture **fails G10** regardless of protocol name |
| Core banking MCP | Only after **G4** vendor diligence + contract |

---

## 5. Memory / audit trail

| Need | System of record |
|------|------------------|
| Filed report packages | Runtime store + content hash (immutable) |
| Who filed / who reviewed | `AuditEvent` append-only (G6/G9) |
| Agent chat history | **Not** examiner evidence unless exported under control |
| Optional vector memory (e.g. “OB1”) | Only if listed in **G4** vendor register and under our DPA — never sole audit trail |

---

## 6. Construction sequence

1. Phase-0 scoreboard evidence (fill `docs/compliance/artifacts/`)  
2. Phase 1: M1 + M3 on **synthetic**  
3. Stress per `DATA_PLANE_SPEC.md`  
4. Phase 2+: M2 → M4 → M5  
5. Core banking APIs only after G4 green  

---

## 7. Cross-links

- Phase-0: `docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md`  
- G10 matrix: `docs/compliance/artifacts/DATA_CLASSIFICATION_AND_AI_GUARDRAILS_MATRIX.md`  
- Data plane: `docs/compliance/DATA_PLANE_SPEC.md`  
- System: `docs/architecture/system-architecture.md`  
- Agent rules: `AGENTS.md` (repo root)
