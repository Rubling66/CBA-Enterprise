# Hermes Data Recon Directive — Detroit Voices + TechTown BAF
Generated: 2026-07-26 14:20 EDT (Updated: 2026-07-26 with DRVS23 PDF full extraction)
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
  - Full DRVS23 Report PDF obtained: 11.9MB, extracted to 1,658 lines of text
  - Image screenshots of dashboard available
- **Access level**: Free + accessible (per Chamber copy: "free and accessible to better understand and inform decisions")
- **Underlying survey**: Detroit Resident Voices Survey (DRVS23) — **11,470 respondents** (6,243 city + 5,227 suburban)
- **Methodology**: Mail + online survey, 150,000+ households contacted, 2022-2023 fielding
- **Chamber contact**: Krishaun Burns (page author)
- **Funding/Support**: Ballmer Group, Gilbert Family Foundation, Kresge Foundation, Skillman Foundation
- **Partners**: Gallup Center on Black Voices

**STRATEGIC IMPLICATION**: No raw API/CSV pipeline exists. However, the full DRVS23 PDF (obtained) contains neighborhood-level stratum data, regression model parameters, and prevalence tables that the interactive dashboard does NOT expose. Product data would need to be:
  (a) Screenshot-scraped from the interactive map for drill-down visuals
  (b) Extracted from the published DRVS23 survey report (DONE — see Section 2)
  (c) Requested via direct data-sharing agreement with Gallup/Chamber for raw microdata

---

## 2. DRVS23 Full Data Extraction — 6 Vertical Framework

**Source**: Full PDF extracted via pdftotext — `/tmp/drvs23.txt` (1,658 lines)
**Survey**: Detroit Resident Voices Survey, Gallup 2023. N=11,470 (city=6,243, suburban=5,227)
**Method**: Mail + online, 150K households, controlled for age/marital status/race/income/home ownership

### VERTICAL 1: WELLBEING & LIFE EVALUATION

**Life Evaluation (Cantril Ladder — 0-10 scale)**

| Segment | Thriving | Struggling | Suffering |
|---------|----------|------------|-----------|
| **Detroit City** | **40%** | 54% | 6% |
| Black (city) | 40% | 55% | 6% |
| Hispanic (city) | 43% | 53% | 9% |
| White (city) | 46% | 45% | — |
| **Suburbs** | **52%** | 43% | 5% |
| Black (suburbs) | 51% | 46% | — |
| **Region** | **50%** | 45% | 5% |
| **U.S. National** | **51%** | 45% | — |
| U.S. Black | 52% | 44% | — |

**Neighborhood-Level Thriving Rates (highest & lowest of 45+ neighborhoods)**

| Highest | Rate | Lowest | Rate |
|---------|------|--------|------|
| Indian Village | **57%** | Cody | **28%** |
| Durfee | **54%** | Greenfield | **29%** |
| Lower East Central | **50%** | Conner | **29%** |

Full neighborhood sample sizes in Appendix 2 (N=9 to N=293). Neighborhoods with N<100 have reduced reliability.

**Regression Model — Determinants of Wellbeing (City Residents)**

| Factor | Beta Estimate | CI | p |
|--------|-------------|----|---|
| Education & employment opportunities | **2.28** | 1.84–2.73 | <0.001 |
| Physical & mental health | 1.12 | 0.63–1.61 | <0.001 |
| Social capital & social opportunities | 0.94 | 0.58–1.31 | <0.001 |
| Neighborhood qualities & aesthetics | 0.55 | 0.14–0.95 | 0.008 |
| Neighborhood services/amenities | -0.31 | -0.70–0.09 | 0.127 (NS) |
| Law enforcement satisfaction | -0.06 | -0.36–0.24 | 0.709 (NS) |

**Model R² = 0.301** (city), **0.374** (suburbs). Education & employment has ~2x the explanatory power of health.

### VERTICAL 2: EDUCATION & EMPLOYMENT OPPORTUNITIES

| # | Metric | City | Suburbs | National |
|---|--------|------|---------|----------|
| 1 | % Satisfied with schools | 30% | 58% | 68% |
| 2 | % Agree children have high-quality public schools access | **18%** | 58% | — |
| 3 | % Say kids better off at diff school | 44% | — | — |
| 4 | % Satisfied with job availability | 39% | 72% | 66% |
| 5 | Black residents — job satisfaction (suburbs) | — | 57% | — |
| 6 | % Unemployed & looking | 12% | 4% | — |
| 7 | % With bachelor's degree+ | **18%** | — | — |
| 8 | % Interested in finding new job (employed) | 45% | — | — |

**Employment Barriers (among those currently looking for work)**

| Barrier | City | Suburbs |
|---------|------|---------|
| Access to a car | **51%** | 28% |
| Level of education/training | 44% | 42% |
| Convenient public transportation | 44% | 26% |
| Past work experience | 45% | 31% |
| Credit history/financial problems | 35% | 24% |
| Criminal background | 19% | 4% |
| Access to childcare | 16% | 11% |

**Why employed workers want new jobs (city, % "major reason")**

| Reason | All | Black | Hispanic | White |
|--------|-----|-------|----------|-------|
| Higher salary/wages | 86% | 86% | 83% | 85% |
| Better benefits | 63% | 65% | 59% | 58% |
| More promotion opportunities | 62% | 64% | 59% | 50% |
| Less harassment/discrimination | 35% | **43%** | 33% | 19% |

**Housing & Homeownership**

| # | Metric | City | Suburbs |
|---|--------|------|---------|
| 9 | % Satisfied with affordable housing | 29% | 55% |
| 10 | % Own primary residence | 48% | 76% |
| 11 | Black — homeownership rate | 45% | 47% |
| 12 | Hispanic — homeownership rate | 61% | 71% |
| 13 | White — homeownership rate | 59% | 81% |
| 14 | Households spending >50% income on housing | ~39K | — |

### VERTICAL 3: HEALTH & HEALTHCARE

| # | Metric | City | Suburbs | National |
|---|--------|------|---------|----------|
| 9 | % Satisfied with healthcare availability | 51% | 78% | 76% |
| 10 | % Easy to access mental health services | **28%** | 46% | 45% |
| 11 | % Easy to get exercise | 66% | — | — |
| 12 | % Easy to get healthy food | 59% | — | — |
| 13 | % Easy to find doctor sharing race/ethnicity | 52% | — | — |
| 14 | Black — easy to find matching doctor | **48%** | — | — |
| 15 | White — easy to find matching doctor | 67% | — | — |

**Health Condition Prevalence (Table 2 from DRVS23)**

| Condition | City - All | City - Black | City - Hispanic | City - White | Suburbs - All |
|-----------|-----------|-------------|----------------|-------------|---------------|
| High blood pressure | **50%** | 53% | 38% | 37% | 39% |
| High cholesterol | 39% | 41% | 38% | 33% | 40% |
| Depression | **31%** | 30% | 26% | 39% | 27% |
| Asthma | **22%** | 22% | 14% | 23% | 14% |
| Diabetes | **21%** | 23% | 16% | 12% | 13% |
| COPD/chronic lung | 9% | 9% | 10% | 9% | 7% |
| Cancer | 7% | 8% | 7% | 7% | 10% |
| Heart attack | 5% | 5% | 4% | 4% | 5% |

**NEIGHBORHOOD HEALTH HOTSPOTS** (worst quartile):
- Food access "very difficult": Mt. Olivet (31%), Rosa Parks (27%), Conner (25%)
- Exercise "very difficult": Conner (17%), Mt. Olivet (16%)
- Doctor matching "very difficult": Nolan (34%), Conner (27%), Rosa Parks (26%), Pershing (25%)

### VERTICAL 4: FOOD & HOUSING SECURITY

| # | Metric | City | Suburbs |
|---|--------|------|---------|
| 14 | % Couldn't afford food (past year) | 43% | 18% |
| 15 | Black — couldn't afford food | **45%** | 38% |
| 16 | Hispanic — couldn't afford food | 40% | 31% |
| 17 | White — couldn't afford food | 27% | 14% |
| 18 | % Couldn't afford shelter/housing | 23% | 10% |
| 19 | Black — couldn't afford shelter | 24% | — |
| 20 | Hispanic — couldn't afford shelter | 23% | — |
| 21 | White — couldn't afford shelter | 11% | — |

**Worst neighborhoods for food insecurity**: Rouge (57%), Winterhalter (57%), Rosa Parks (53%), Mackenzie (51%)
**Worst neighborhoods for housing insecurity**: Nolan (52%), Redford (37%), Conner (35%)

### VERTICAL 5: NEIGHBORHOOD SATISFACTION & MOBILITY

| # | Metric | Value |
|---|--------|-------|
| 22 | % Would move permanently if could | **57%** |
| 23 | Of movers — % would stay in metro area | 47% |
| 24 | % Would recommend city as good place to live | 55% |
| 25 | Black — would recommend | 53% |
| 26 | Hispanic — would recommend | 66% |
| 27 | White — would recommend | 66% |
| 28 | Would recommend (if neighborhood clean — good/very good) | 78% |
| 29 | Would recommend (if neighborhood cleanliness bad/very bad) | 30% |

**Why residents want to move (top reasons, % "major reason")**:
- Crime is too high: **62%**
- Better place to raise children: 52%
- Better job/business opportunities: 42%
- Cost of living too high: 37%

### VERTICAL 6: SOCIAL CAPITAL & PUBLIC SAFETY

**Social Cohesion**

| Metric | City | Black | Hispanic | White |
|--------|------|-------|----------|-------|
| Agree "Detroiters care about each other" | 34% | 32% | 33% | **51%** |
| Agree "people in community care" | 35% | 34% | 29% | 48% |
| Easy to access social/community events | 36% | 34% | 36% | 49% |
| Have relatives/friends to count on | 68% | 68% | 62% | 75% |

**Key insight**: Black residents who CAN access social events are 3x more likely to feel community care (59% vs 19%).

**Crime & Policing**

| Metric | City | Suburbs |
|--------|------|---------|
| % Agree community is safe | **26%** | 71% |
| % Feel safe walking alone at night | 32% | 76% |
| Female — feel safe walking alone | 23% | 67% |
| Male — feel safe walking alone | 42% | 85% |
| Black city — feel safe walking alone | 30% | — |
| Black suburbs — feel safe | — | 62% |
| White suburbs — feel safe | — | 80% |
| % Would like more police time | **59%** | 24% |
| % Satisfied with police-community relationship | 51% | — |
| % Say police treat fairly | **64%** | — |
| Black city — police treat fairly | 62% | — |
| Black city aged 18-29 — police treat fairly | 53% | — |
| % Say police would treat with courtesy/respect | 71% | — |
| Black city — courtesy/respect | 71% | — |

**Neighborhood safety (lowest — % feel safe walking alone at night)**:
Mt. Olivet (16%), Denby (19%), Brooks (19%)
**Highest**: Central Business District (76%), Lower Woodward (53%)

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

1. **DRVS23 PDF**: Full extracted text saved at `/tmp/drvs23.txt`. Source for all neighborhood-level data.
   - ✅ Neighborhood appendix (45+ neighborhoods, sample sizes N=9 to N=293)
   - ✅ Regression model parameters (beta weights, CI, p-values)
   - ✅ Health prevalence tables (8 conditions x 4 city segments)
   - ✅ Employment barrier breakdown (7 categories x city/suburbs)
   - ✅ Police/community perception tables (5 metrics x race/age)

2. **Gallup Dashboard Access**: Try loading gallup.com/analytics/708758/gallup-detroit-chamber.aspx in browser to explore the interactive map and check for hidden export/data download features. May need JavaScript execution.

3. **Gallup Contact**: Submit inquiry via Gallup Center on Black Voices page asking about data partnership / raw data access for product development.

4. **TechTown Prep**: Prepare 1-pager positioning dconsult as advanced technology company (AI-driven diagnostic engine for urban systems), emphasizing:
   - Commercialization pathway (CBA Enterprise → neighborhood decision-support)
   - Technology readiness (Hermes agent infrastructure)
   - Market validation (DRVS23 data alignment — 11,470 respondents validate the problem)
   - NOTE: DRVS23 PDF confirms city thriving is 40% (not 50% regional avg). Use 40% for accuracy.

5. **Competitive Edge**: dconsult's unique differentiator = multi-agent architecture (Hermes orchestration) + automated compliance pipeline (CBA Enterprise). No competitor combines civic data with automated regulatory compliance.