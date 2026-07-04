# Financial Data Sources — CLV Solar PV Study

Parameters used in `solar_energy_simulation.ipynb` (Section 7) and recommended for the SAM
financial model. Researched 2026-07-04. Sources are graded by tier so citations can be made
honestly on slides.

## Tier 1 — Government / regulatory (cite freely)

| Parameter | Value | Source |
|---|---|---|
| Net metering system size cap | **None** (cap removed; size to load) | [O. Reg. 541/05](https://www.ontario.ca/laws/regulation/050541), [OEB net metering](https://www.oeb.ca/consumer-information-and-protection/net-metering), [ERO notice 019-2370](https://ero.ontario.ca/notice/019-2370) |
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
| Installed cost, commercial rooftop | C$1.90–2.80/W typical; C$1.30–1.50/W for large single roofs. Study uses **C$1.70 / 2.10 / 2.60 scenarios** (269 small distributed roofs → small-commercial pricing) | [greenbuildingcanada.ca commercial guide](https://greenbuildingcanada.ca/cost-commercial-solar-panels-canada/), [magsolar.ca](https://magsolar.ca/cost-of-commercial-solar-panels-in-canada/) |
| O&M | C$12–18/kW/yr commercial; study uses **C$18** (snow region, distributed sites) | [ppm.solar O&M guide](https://ppm.solar/commercial-solar-om-guide/); cross-checked vs [NREL ATB commercial PV](https://atb.nrel.gov/electricity/2024/commercial_pv) (US$) |
| Degradation | 0.5%/yr | Standard module warranty figure |

## Other assumptions (state explicitly when used)

| Parameter | Value | Note |
|---|---|---|
| Ontario grid emission factor (average) | ~51 g CO2e/kWh | Order-of-magnitude; verify against latest IESO/NIR before publishing |
| Marginal (gas) emission factor | ~400 g CO2e/kWh | CCGT on the margin; assumption |
| Panel rating in Google Solar API counts | 400 W DC | Google's default panel assumption |

## Upgrades if time allows

Real installer quote for an Ontario institutional rooftop portfolio; CanREA market data;
recent public tender pricing; UW Finance confirmation of Clean Electricity ITC eligibility.
