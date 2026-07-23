# CBA-Enterprise

Bank Community Benefits Agreement (CBA) compliance reporting system.

**Status:** Pre-construction — regulatory framework phase.

## What

Banks with CBA consent orders (TD Bank $50B+, regional banks $2B–$25B) are legally required to report where settlement dollars go. Currently they have no system. CBA-Enterprise provides:

1. **Ingest** — Parse consent orders, extract commitments & deadlines
2. **Track** — Disbursement API → category mapping (small biz / housing / community dev / workforce)
3. **Report** — OCC-format auto-generated compliance reports
4. **Verify** — Triple-blind: bank data × municipal records × anomaly detection
5. **Gate** — Consumer eligibility verification (LMI, credit floor, lien screen, program match)

## Revenue

$2,500/yr per institution (recurring) + custom integration fees.

## Architecture

```
CBA-Enterprise/
├── docs/               # Regulatory, architecture, compliance docs
├── engine/             # Core processing (Python)
│   ├── ingest/         # Consent order & CBA contract parsing
│   ├── track/          # Disbursement tracking & categorization
│   ├── report/         # OCC-format report generation
│   ├── verify/         # Triple-blind outcome verification
│   └── gate/           # Consumer funding eligibility gate
├── dashboard/          # React/Vite compliance dashboard
├── scripts/            # Preflight, deploy, data ops
├── data/               # Sample data, test fixtures
├── .github/            # CI/CD, compliance checks
└── D-Obsidian/         # Hermes↔Grok bridge (Obsidian vault mirror)
    └── Bridge/
        ├── to-grok/    # Hermes → Grok task briefs
        └── from-grok/  # Grok → Hermes status reports
```

## Detroit Banks (Targets)

| Bank | Hook (see market doc) | CRA / CBA note |
|------|----------------------|----------------|
| Huntington | $1B Detroit/Wayne carve-out + micro-lending | National Community Plan scale |
| JPMorgan Chase | Flagship Detroit + EOCF/CDFI stack | Large holistic Detroit investment |
| Fifth Third | G7 hyper-local neighborhood model | Exceeded national NCRC CBA goal |
| Comerica | Hometown + Outstanding CRA PE | Historical Detroit Alliance CBA |
| Flagstar | Regional | Prior target list |

**Market gap:** Micro-loans **&lt;$100k** to LMI / majority-minority tracts under-indexed vs business share — product reports **micro band + tract**.  
Detail: `docs/market/DETROIT_CBA_CRA_COMPETITIVE_LANDSCAPE.md`

## Regulatory Foundation

- OCC Bulletin 2013-29 (Third-Party Relationships / Vendor Management)
- FFIEC IT Examination Handbook
- CRA Performance Evaluation framework
- HMDA data standards
- SOC 2 Type II (target certification)

## Build vs runtime (critical)

| Plane | Tooling | Data |
|-------|---------|------|
| **Build** | Grok Build, humans, CI | Synthetic / public / redacted only |
| **Runtime** | Our engine (no public LLM) | Bank data under Phase-0 controls |

See `docs/architecture/BUILD_PLANE_VS_RUNTIME_PLANE.md` and root **`AGENTS.md`**.

## Framework docs (Phase-0)

| Doc | Path |
|-----|------|
| Phase-0 gates G1–G10 | `docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md` |
| Data plane + stress | `docs/compliance/DATA_PLANE_SPEC.md` |
| OCC / vendor spine | `docs/regulatory/OCC-2013-29-vendor-management.md` |
| System architecture | `docs/architecture/system-architecture.md` |
| Data model | `docs/architecture/data-model.md` |
| Dashboard IA | `docs/architecture/dashboard-wireframe.md` |
| Evidence stubs | `docs/compliance/artifacts/` |

**Phase-0 scoreboard is NOT GREEN until evidence is filled.** No feature BUILD-ORDER until then.

## Bridge Protocol

Hermes (orchestrator) ↔ Grok (engineer) via `D-Obsidian/Bridge/`:
- `to-grok/` — task briefs, framework requests, decisions
- `from-grok/` — status, framework drafts, blockers
- `PROTOCOL.md` — naming and priorities

## See Also

- Skill registry: `cba-reporting-system`, `cba-enterprise`, `cba-enterprise-deployment`
- GitHub: https://github.com/Rubling66/CBA-Enterprise