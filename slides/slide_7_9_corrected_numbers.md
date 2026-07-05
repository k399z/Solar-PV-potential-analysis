# Corrected replacement numbers for slides 7–9 (full 1.96 MW build-out)

All figures from solar_energy_simulation.ipynb (committed, re-executed 2026-07-05).
Problem being fixed: slides 7–9 currently use the 314 kW SAM pilot config against the
2024 artifact-year load (23% coverage), contradicting the deck's 76% headline.

## Slide 7 — Electricity Sources
Replace pie with `electricity_sources_donut.png` (this folder), or re-make the pie as:
- **PV 76% / Grid 24%** (annual, 2022–23 baseline: generation 2.03 GWh vs demand 2.69 GWh)
- Optional caption: "Summer surplus (0.42 GWh) banks as net-metering credits, consumed in winter — nothing wasted."

## Slide 8 — Impact
- 2030: **76% less grid electricity for CLV** (full build-out operating)
- 2040: **cash-flow positive** (payback 14–20 yr from 2026 build; central 15.6 yr with 15% ITC)
- 2050: **~45 GWh generated · ~C$6.5M grid purchases avoided** (24 yr @ 0.5%/yr degradation)
- GHG: **79 t CO2e/yr** (39 g location-based factor, per Brookfield session) —
  **164 t/yr** at 2026 grid intensity, **649 t/yr** marginal displacement.
  Lifetime at location-based factor: **~1,860 t CO2e**.

## Slide 9 — Economic Snapshot
| | |
|---|---|
| Initial cost | **C$4.1–5.1M** (C$2.10–2.60/W scenarios; central C$4.6M) |
| Annual energy value | **~C$294k** (plus demand-charge savings — SAM methodology) |
| O&M | C$43k/yr (C$22/kW/yr, block-aggregated) |
| Simple payback | **14–20 yr** (central 15.6 yr with 15% refundable Clean Electricity ITC) |
| LCOE | **C$0.096–0.129/kWh vs grid C$0.145** — use `lcoe_vs_grid.png` |

## If keeping William's SAM pages instead (Option B)
Retitle them: "Pilot configuration — 314 kW (SAM cash-flow model)" and add:
"Full build-out economics: see previous slide. SAM model demonstrates financing/demand-charge
methodology; its weather file and snow settings are being localized (docs/sam_study_status.md)."
