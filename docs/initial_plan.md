# Initial project plan (original README, preserved 2026-07-04)

> Kept as a scratchpad record of the day-one plan. Superseded by the results-oriented
> README; note the original justification ("high monthly electricity consumption") was
> later corrected by the data — CLV ranks mid-pack on consumption, and the defensible
> case became roof inventory + self-coverage. PyPSA was not ultimately used.

---

# Solar-PV-potential-analysis
Assess the technical and economic feasibility of installing solar PV on campus rooftops, parking lots, or open land.

Specific Sites: Columbia Lake Villages

Why is this problem worth solving?

Since CLV has quite a high monthly electricity consumption rate and is spread out over a large area, installing solar panels would provide a significant reduction in the use of non-renewable energy on campus and greenhouse gas emissions in the region.

Technical feasibility
- Shade Map (How long are the CLV rooftops exposed to sunlight on average?)
- Site suitability mapping (What is the total area of all the rooftops combined?)
- Power System Analysis with PyPSA
- Simulate the performance of Solar-PV system with pvlib
- Build photovoltaic model with System Advisor Model (SAM)

Economic Feasibility
- Build Economic Dispatch model with PyPSA or Financial model with SAM
