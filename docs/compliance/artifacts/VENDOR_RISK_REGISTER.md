---
type: phase-0-evidence-stub
gate: G4
status: OPEN
---

# G4 — Vendor Risk Assessment & Executed Contracts

**Status:** ⬜ OPEN

| Vendor | Service | Risk class | Data classes touched | Contract / DPA | Right to audit | Incident notify | Status |
|--------|---------|------------|----------------------|----------------|----------------|-----------------|--------|
| Hostinger | Hosting | Medium | Site assets | | | | Planned |
| IONOS | DNS/domains | Low | Public DNS | | | | Active registrar |
| Render | App host (if used) | Medium | App runtime | | | | Optional |
| xAI / Grok Build | Dev agent | Medium | **Build plane only** — no bank PII | | | | Build only |
| Ollama (local) | Local LLM | Low | On-box redacted/synthetic | N/A local | | | Preferred for local AI |

**Rule:** No production bank data to vendors without assessment + contract terms (audit, confidentiality, return/destruction).
