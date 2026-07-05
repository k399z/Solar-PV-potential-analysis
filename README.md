# Solar PV Potential Analysis — Columbia Lake Village, University of Waterloo

Technical and economic feasibility of rooftop solar PV on campus, developed for the
Sustainable Energy Systems challenge. Site: **Columbia Lake Village (CLV South)** —
50 townhouse blocks / 269 dwelling units of student and family housing.

## Why CLV

We scanned **every building in the challenge dataset** with the same measurement pipeline
(Google Solar API over hand-verified boundary polygons). CLV has the **largest verified
usable roof inventory on campus (18,617 m²)** and the **highest solar self-coverage of any
meaningful load (76% of its fully-occupied annual demand)**. The two residence complexes
(CLV + UW Place) hold more usable roof than all other measured campus buildings combined —
residential low-rise housing is where campus solar lives.

## Key results

| Metric | Value |
|---|---|
| Max rooftop capacity | **1.96 MW DC** (4,897 panels across 50 block roofs) |
| Annual generation | **~2.0 GWh/yr** (after system + snow losses) |
| Self-coverage | **76%** of 2022–23 baseline demand (2.69 GWh/yr) |
| Emissions avoided | 164 t CO₂e/yr (grid-average) – 649 t/yr (marginal gas) |
| Levelized cost | **C$0.10–0.13/kWh vs C$0.145 grid rate** — below grid in all scenarios |
| Simple payback | 14–20 years on 25+ year assets (central: 15.6 yr with 15% ITC) |
| Deployment | Phase 1: 500 kW net-metered (O. Reg. 541/05 caps net metering per meter); expansion via load displacement or third-party PPA (which unlocks the 30% Clean Tech ITC for tax-exempt UW) |

Yield validated three independent ways: pvlib on local weather-station data vs Google's
aerial flux model (agree within 5%), and QGIS roof tracing vs Solar API areas (within 6%).
Financial parameters survived two rounds of adversarial AI fact-checking plus a deep-research
pass — including corrections that *worsened* our numbers, which we kept
(see [docs/](docs/)).

## Repository guide

| Path | What it is |
|---|---|
| [solar_energy_simulation.ipynb](solar_energy_simulation.ipynb) | Main analysis: data cleaning, demand baseline, pvlib yield model, sizing, load matching, emissions, scenario economics, campus site comparison |
| [solar_api_clv.py](solar_api_clv.py) / [solar_api_responses/](solar_api_responses/) | Google Solar API measurement of all 269 CLV roofs (reproducible) |
| [PV-study.sam / .pdf / .xlsx](PV-study.pdf) | NREL SAM financial model |
| [Shademap/](Shademap/) | Sun-exposure GeoTIFF + visuals (independent shade check) |
| [docs/financial_data_sources.md](docs/financial_data_sources.md) | Every financial parameter with source and quality tier |
| [docs/verification_report.md](docs/verification_report.md), [docs/deep_research_report_gemini.md](docs/deep_research_report_gemini.md) | Independent verification trail |
| [Sustainable_Energy_Systems/](Sustainable_Energy_Systems/) | Challenge brief, datasets (2015–2024), SAM guide |

## Data caveats handled in the analysis

- Weather station uses inconsistent missing-data sentinels; 2019 & 2022 had months-long
  logger outages → any negative irradiance treated as invalid; only ≥98%-complete years used
- CLV billed bimonthly until 2017 → normalized to per-month rates
- COVID (Mar 2020 – late 2021) and an unexplained ~40% consumption drop in 2024 → demand
  baselined on 2022–23; results reported against both occupancy scenarios

## Reproduce

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab solar_energy_simulation.ipynb   # select the .venv kernel, Run All
export GOOGLE_MAPS_API_KEY=...              # only needed to re-run the Solar API sweeps
```
