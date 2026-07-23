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

| Bank | CBA Commitment | CRA Rating |
|------|---------------|------------|
| Huntington | ~$25B | Outstanding |
| JPMorgan Chase | ~$32B | Outstanding |
| Fifth Third | ~$12B | Outstanding |
| Flagstar | ~$2B | Satisfactory |
| Comerica | ~$5B | Satisfactory |

## Regulatory Foundation

- OCC Bulletin 2013-29 (Third-Party Relationships / Vendor Management)
- FFIEC IT Examination Handbook
- CRA Performance Evaluation framework
- HMDA data standards
- SOC 2 Type II (target certification)

## Bridge Protocol

Hermes (orchestrator) ↔ Grok (engineer) communication via `D-Obsidian/Bridge/`:
- `to-grok/` — task briefs, framework requests, architecture decisions
- `from-grok/` — status reports, build evidence, blockers

## See Also

- `dconsult/cba-reporting-system` — Full product specification (skill registry)
- `dconsult/cba-enterprise` — CBA methodology & deployment framework
- `dconsult/cba-enterprise-deployment` — Bank deployment playbook