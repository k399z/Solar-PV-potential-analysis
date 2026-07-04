# Financial Data Sources — CLV Solar PV Study

Parameters used in `solar_energy_simulation.ipynb` (Section 7) and recommended for the SAM
financial model. Researched 2026-07-04. Sources are graded by tier so citations can be made
honestly on slides.

## Tier 1 — Government / regulatory (cite freely)

| Parameter | Value | Source |
|---|---|---|
| Net metering system size cap | **500 kW per meter** (still in force — the liberalizing O. Reg. 273/18 was *revoked* before effect, per [ERO 013-1913 decision](https://ero.ontario.ca/notice/013-1913); the 2022 amendment added third-party ownership only). Earlier 'cap removed' claims trace to installer SEO pages. Capacity beyond 500 kW: load displacement or PPA. Enova Power (local LDC) requires a generation meter >50 kW. | [O. Reg. 541/05](https://www.ontario.ca/laws/regulation/050541), [OEB](https://www.oeb.ca/consumer-information-and-protection/net-metering), deep_research_report_gemini.md |
| Net metering credit treatment | Monthly excess rolls over, 12-month credit expiry | O. Reg. 541/05 |
| Clean Technology ITC | 30%, **taxable Canadian corporations only** — UW (tax-exempt) cannot claim directly; reachable via third-party/PPA ownership | [CRA Clean Technology ITC](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/business-tax-credits/clean-economy-itc/clean-technology-itc.html) |
| Clean Electricity ITC | 15%, refundable, broader public-sector claimant base — UW *may* qualify depending on legal structure (unconfirmed) | CRA (above); analysis: [Fasken CE-ITC guide](https://www.fasken.com/en/knowledge/2026/05/canadas-clean-electricity-investment-tax-credit-a-comprehensive-guide), [BLG clean-economy ITCs](https://www.blg.com/en/insights/2024/ri/canadas-2024-green-itcs) |

## Tier 2 — Challenge-provided (use as given, cite "challenge rate structure")

| Parameter | Value | Source |
|---|---|---|
| Energy rate | C$0.145/kWh flat | `Sustainable_Energy_Systems/NREL_SAM.md` step 9 |
| Fixed charge | C$125.96/month | NREL_SAM.md step 9 |
| Demand charge | C$11.68/kW | NREL_SAM.md step 9 |
| Real discount rate | 5%/yr | NREL_SAM.md step 8 |
| Sales tax (HST) | 13% | NREL_SAM.md step 8 |
| O&M escalation | 2.5%/yr | NREL_SAM.md step 7 |
| Snow loss factors | Jan/Feb 30%, Mar 15%, Apr–Oct 5%, Nov 10%, Dec 25% | NREL_SAM.md step 6 |

## Tier 3 — Industry guides (label as "industry guide pricing, 2026"; use as ranges)

| Parameter | Value | Source |
|---|---|---|
| Installed cost, commercial rooftop | C$1.90–2.80/W typical; C$1.30–1.50/W for large single roofs. Study uses **C$2.10 / 2.35 / 2.60 scenarios** (deep research: bulk procurement floors ~C$2.10; dispersed pitched-roof labour rules out C$1.70) | [greenbuildingcanada.ca commercial guide](https://greenbuildingcanada.ca/cost-commercial-solar-panels-canada/), [magsolar.ca](https://magsolar.ca/cost-of-commercial-solar-panels-in-canada/) |
| O&M | Single-site Canadian commercial C$20–30/kW/yr; physical portfolio is **~50 block roofs (~39 kW each)**; block-aggregated estimates: deep research C$15–22, Canadian commercial C$20–30. Study uses **C$22/kW/yr** (spread C$15–30). US guides quoting US$12–18 are unconverted USD, single-site. | [ppm.solar](https://ppm.solar/commercial-solar-om-guide/) (US$, single-site); two-round Gemini+Search verification 2026-07-04, see verification_report.md |
| Degradation | 0.5%/yr | Standard module warranty figure |

## Other assumptions (state explicitly when used)

| Parameter | Value | Note |
|---|---|---|
| Ontario grid emission factor (average) | **81 g CO2e/kWh** (range 81–124; rising with nuclear refurbishments) | Deep-research verification (TAF/IESO-cited), see deep_research_report_gemini.md |
| Marginal (displaced) emission factor | **320 g CO2e/kWh** (range 280–320; gas blended with imports) | Power Advisory via deep-research verification |
| Panel rating in Google Solar API counts | 400 W DC | Google's default panel assumption |

## Upgrades if time allows

Real installer quote for an Ontario institutional rooftop portfolio; CanREA market data;
recent public tender pricing; UW Finance confirmation of Clean Electricity ITC eligibility.

## Independent verification trail

- `verification_report.md` — 12 parallel Gemini+Search adversarial checks (round 1)
- `deep_research_report_gemini.md` — Gemini Deep Research agent report (round 2); corrected the net-metering cap error, emission factors, capex floor, and O&M for block aggregation. ITC labour requirements (10-point reduction if unmet) flagged.
