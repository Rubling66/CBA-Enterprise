# Hermes Data Recon Directive — Detroit Voices + TechTown BAF
Generated: 2026-07-26 14:20 EDT
Source: dconsult Intelligence Engine (DeepSeek V4 Flash)

---

## 1. Gallup/Detroit Voices Dashboard — Data Access Model

**VERDICT: RESTRICTED INTERACTIVE (No Bulk Export)**

- **URL**: https://www.gallup.com/analytics/708758/gallup-detroit-chamber.aspx
- **Landing page**: https://www.detroitchamber.com/equity/detroit-voices-data-dashboard/
- **Platform**: Gallup proprietary "Gallup Access Platform" — interactive web map
- **Data delivery**: Browser-based interactive map only ("Explore the Map")
- **Export options**: ⛔ No CSV/API/JSON download found on public page
  - Press Release PDF available (not raw data)
  - Image screenshots of dashboard available
- **Access level**: Free + accessible (per Chamber copy: "free and accessible to better understand and inform decisions")
- **Underlying survey**: Detroit Resident Voices Survey (DRVS23) — 11,000+ respondents, Gallup Center on Black Voices
- **Chamber contact**: Krishaun Burns (page author)
- **Funding/Support**: Ballmer Group, Gilbert Family Foundation, Kresge Foundation, Skillman Foundation
- **Partners**: Gallup Center on Black Voices

**STRATEGIC IMPLICATION**: No raw API/CSV pipeline exists. Product data would need to be:
  (a) Screenshot-scraped from the interactive map
  (b) Inferred from the published DRVS23 survey report
  (c) Requested via direct data-sharing agreement with Gallup/Chamber

---

## 2. Top 20 Neighborhood Metrics — 5 Verticals

Extracted from DRVS23 Survey Report (detroitchamber.com/drvs23/) + Gallup Analytics page.

### VERTICAL 1: EDUCATION & ECONOMIC OPPORTUNITY
| # | Metric | City | Suburbs | National |
|---|--------|------|---------|----------|
| 1 | % Thriving (Life Evaluation) | 40% | 52% | 51% |
| 2 | % Struggling | 54% | 38% | 45% |
| 3 | % Satisfied with schools | 30% | 58% | 68% |
| 4 | % Say kids better off at diff school | 44% | 20% | — |
| 5 | % Satisfied with job availability | 39% | 72% | 66% |
| 6 | Black residents — job satisfaction (suburbs) | — | 57% | — |
| 7 | Access to car as employment barrier | 51% | — | — |
| 8 | Public transit/education as barrier | 44% | — | — |

### VERTICAL 2: HEALTH & HEALTHCARE
| # | Metric | City | Suburbs | National |
|---|--------|------|---------|----------|
| 9 | % Satisfied with healthcare availability | 51% | 72% | 76% |
| 10 | % Very easy to access mental health services | 14% | 30% | 20% |
| 11 | % Easy to get exercise | 66% | — | — |
| 12 | % Easy to get healthy food | 59% | — | — |
| 13 | Depression — thrivers (diagnosed) | 26% | — | — |

### VERTICAL 3: HOUSING & FOOD SECURITY
| # | Metric | City | Suburbs |
|---|--------|------|---------|
| 14 | % Couldn't afford food (past year) | 43% | 18% |
| 15 | % Couldn't afford shelter/housing | 23% | 10% |
| 16 | Black residents — couldn't afford food | 45% | — |
| 17 | Hispanic residents — couldn't afford food | 40% | — |
| 18 | White residents — couldn't afford food | 27% | — |

### VERTICAL 4: NEIGHBORHOOD SATISFACTION & MOBILITY
| # | Metric | Value |
|---|--------|-------|
| 19 | % Would move permanently | 57% |
| 20 | % Would stay in metro area (of movers) | 47% |
| 21 | % Would recommend city as good place to live | 55% |
| 22 | Black residents — would recommend | 53% |
| 23 | Hispanic residents — would recommend | 66% |
| 24 | White residents — would recommend | 66% |

### VERTICAL 5: SOCIAL CAPITAL & PUBLIC SAFETY
| # | Metric | Value |
|---|--------|-------|
| 25 | Police/community getting better | 26% |
| 26 | Police/community staying the same | 57% |
| 27 | Police/community getting worse | 17% |
| 28 | Regional recommendation rate | 80% |

**NOTE**: Neighborhood-level granularity exists in the interactive dashboard on Gallup's platform. The survey report only publishes city-vs-suburb aggregates. To drill to individual Detroit neighborhood level (e.g., North End, East English Village, Warrendale), the interactive Gallup map must be used.

---

## 3. TechTown BAF Discovery Session — Research

**What is BAF?**
- **Business Accelerator Fund** — Michigan SmartZone network program
- **Purpose**: Deliver specialized services to advanced tech companies
- **Mechanism**: TechTown as participating administrator; third-party specialists engaged for commercialization support
- **Award process**: Competitive — "reviewed and awarded through a competitive process"
- **What they provide**: Customized, one-on-one professional guidance

**Discovery Session (Tomorrow 11AM @ 440 Burroughs St)**
- Format likely: Initial intake/qualification meeting
- TechTown staff: "Incredible staff" referenced on site — specific team unknown
- Programs under TechTown umbrella:
  - Small Business Support (Wayne County — one-on-one guidance)
  - BAF (advanced tech/commercialization)
  - Mobility Accelerator Innovation Network (MAIN)
  - Coaching Up program
  - Monthly casual entrepreneur meetups

**BAF Submission Requirements (Inferred)**
- Must be an advanced technology company
- Must demonstrate commercialization pathway
- TechTown acts as sponsor/administrator
- Funds go to third-party specialist services, not direct cash to company
- Likely requires: Business plan, technology description, market analysis, team background

---

## 4. Competitive Landscape Scan

### Data Dashboard / Civic Intelligence Competitors

| Organization | Product | Relevance |
|-------------|---------|-----------|
| **Data Driven Detroit (D3)** | Detroit Open Data Portal, neighborhood indicators | HIGH — Most direct competitor for civic data products |
| **University of Michigan — Detroit Metro Area Communities Study** | Neighborhood survey data, biennial reports | HIGH — Academic rigor, peer-reviewed methodology |
| **Detroit Future City (DFC)** | Data platform, neighborhood typologies | MEDIUM — Policy-oriented, less technical |
| **Quicken Loans Community Fund / Rocket Companies** | Detroit Neighborhood Dashboard | MEDIUM — Corporate-backed, limited scope |
| **Urban Institute** | Detroit-specific data products (criminal justice, housing) | MEDIUM — National org, periodic reports |
| **City of Detroit — OCIO** | Open Data Portal (data.detroitmi.gov) | MEDIUM — Raw city datasets, not survey-based |
| **Gallup (national)** | Gallup Access Platform (proprietary) | LOW — National org, Detroit is one client |
| **Brookings Institution** | Metro Monitor, Detroit-specific research | LOW — National think tank, not a product |

### Grant/Funding Competitors for TechTown Position

| Organization | Program | Amount | Notes |
|-------------|---------|--------|-------|
| **TechTown BAF** | Business Accelerator Fund | Unclear | Tomorrow's target |
| **Motor City Match** | Business plan + space grants | Up to $100K | Cash + real estate assistance |
| **New Economy Initiative (NEI)** | Entrepreneur support | Varies | Southeast Michigan focus |
| **Michigan Economic Development Corp (MEDC)** | Various innovation funds | Varies | State-level, competitive |
| **Hudson-Webber Foundation** | Economic development grants | Varies | Detroit-specific |
| **Kresge Foundation** | FreshLo, other programs | Varies | Large foundation, Detroit focus |

---

## 5. Action Items

1. **Gallup Dashboard Access**: Try loading gallup.com/analytics/708758/gallup-detroit-chamber.aspx in browser to explore the interactive map and check for hidden export/data download features. May need JavaScript execution.

2. **Gallup Contact**: Submit inquiry via Gallup Center on Black Voices page asking about data partnership / raw data access for product development.

3. **TechTown Prep**: Prepare 1-pager positioning dconsult as advanced technology company (AI-driven diagnostic engine for urban systems), emphasizing:
   - Commercialization pathway (CBA Enterprise → neighborhood decision-support)
   - Technology readiness (Hermes agent infrastructure)
   - Market validation (Gallup data alignment)

4. **Competitive Edge**: dconsult's unique differentiator = multi-agent architecture (Hermes orchestration) + automated compliance pipeline (CBA Enterprise). No competitor combines civic data with automated regulatory compliance.

---

*End of Recon Directive — Commander ready for review*