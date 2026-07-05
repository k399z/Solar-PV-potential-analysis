# SAM study (PV-study-vf) — review status, 2026-07-05

`PV-study-vf.pdf/.sam/.xlsx` is an independent NREL SAM cash-flow model of a **314 kW pilot
configuration** (bifacial modules, block-style subarrays, Ontario rate structure with demand
charges and monthly net-metering rollover).

**Corrected in the vf revision:** the US 30% federal ITC was removed (not claimable by a
tax-exempt Canadian university). Result: payback 10.5 yr, NPV $61.5k, LCOE 18.5 ¢/kWh nominal.

**Known remaining gaps** (would move results toward the notebook's 14–20 yr payback range):
- Weather file is the SAM default location (38.89, −77.02 — Washington, DC; GHI 4.28 kWh/m²/day)
  rather than Waterloo (~3.5) — inflates generation ~15–18%.
- Snow losses set to 0% (challenge guide prescribes 5–30% monthly for Waterloo).
- Load profile is CLV's 2024 metered year (1.58 GWh), which the analysis identifies as a probable
  metering/billing artifact; the fully-occupied baseline is 2.69 GWh (2022–23).
- 314 kW sizing predates the corrected roof measurement (1.96 MW max; ~500 kW net-metered phase 1).

**Role in the study:** the SAM model demonstrates the full cash-flow methodology (financing,
demand-charge savings, rollover credits) and independently confirms the direction of the
economics. Headline economic figures are taken from the notebook's sourced scenario grid
(`solar_energy_simulation.ipynb` §7); a SAM re-run with Waterloo TMY + snow + corrected sizing
is the planned follow-up.
