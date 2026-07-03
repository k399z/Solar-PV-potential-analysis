# Sustainable Energy⚡
Around the world, institutions are working to transition toward more sustainable energy systems in response to the growing impacts of climate change, habitat loss, and resource depletion. As non-renewable energy sources become increasingly scarce and costly, the urgency to adopt cleaner, more reliable alternatives continues to grow. Universities, as centres of research and innovation, play a critical role in leading this transition.

University campuses rely on a range of energy sources—including electricity, natural gas, and other fossil fuels—to power lighting, heating, and cooling systems, laboratories, computing infrastructure, and daily operations. At the University of Waterloo, campus energy consumption has steadily increased alongside expansion and rising demand. To align with institutional sustainability commitments, the university seeks to advance its goal of implementing cost-effective and practical strategies to reduce or minimize growth in campus energy use while transitioning to cleaner energy sources.

## Challenge 
Develop a feasible strategy to improve the sustainability of energy systems at the University of Waterloo. Teams will analyze how campus energy use varies with weather and assess opportunities to integrate renewable energy sources. The challenge evaluates how these systems can reduce emissions, manage peak demand, and improve energy efficiency within existing campus infrastructure. 

You need to communicate the details of your design to the judges. Your solution could include drawings, models, simulations, prototypes, or anything you think is useful for communicating your ideas. Please refer to the judging rubric and presentation instructions when planning your final presentation to the judges. 

## Potential Solutions
These aren’t the only solutions, but these are some of the ideas that you can take inspiration from. Feel free to mix and match any potential solutions if you feel that it is appropriate.

| Potential Solutions | Description | Resources |
|:---------|:------------|:----------|
| **Energy forecasting & load prediction** | Build models to predict campus electricity and heating demand based on weather, academic calendar, and historical usage. | <ul><li>Historical energy consumption data</li><li>Weather data</li><li>Academic Calendar Archives</li><li>Dashboard frameworks (Plotly Dash, Streamlit, or HTML/CSS/JS)</li></ul> |
| **Solar PV potential analysis** | Assess the technical and economic feasibility of installing solar PV on campus rooftops, parking lots, or open land. | <ul><li>Map of Shade</li><li>PVWatts / pvlib / PyPSA</li><li>System Advisor Model</li><li>Site suitability mapping (ArcGIS Pro or QGIS)</li></ul> |
| **Geothermal & alternative heating** | Evaluate the potential for ground-source heat pumps or other renewable heating/cooling technologies to replace or supplement the existing district energy system. | <ul><li>Geothermal infrastructure tour</li><li>Weather data</li><li>GHEDesigner / FEFLOW</li><li>Historical energy consumption data</li></ul> |
| **Energy scavenging** | Reuse waste heat from wastewater, data servers, or other campus processes to supplement heating needs. | <ul><li>Facility infrastructure information</li><li>Historical energy consumption data</li><li>Case studies on waste heat recovery</li><li>Thermodynamic analysis tools</li></ul> |

## Resources
- [Energy data | Sustainability | University of Waterloo](https://uwaterloo.ca/sustainability/our-progress/energy-data)
- [Eric D. Soulis Weather Station Value Archive](https://www.civil.uwaterloo.ca/weatherstation/data-archives/?utm_source=chatgpt.com)
- [Generator Output and Capability](https://reports-public.ieso.ca/public/GenOutputCapability/)
- [MATLAB and Simulink for Renewable Energy and Energy Storage](https://www.mathworks.com/solutions/electrification/renewable-energy-energy-storage.html)
- [ArcGIS Pro](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview)
- [Map of Shade](https://shademap.app/@43.47173,-80.54087,15.84043z,1770822733107t,0b,0p,0m)
- [Pvlib python](https://github.com/pvlib/pvlib-python)
- [PyPSA - Python for Power System Analysis](https://github.com/PyPSA/PyPSA)
- [System Advisor Model](https://sam.nlr.gov/)
- [The Building Data Genome 2 Dataset](https://github.com/buds-lab/building-data-genome-project-2/tree/master?tab=readme-ov-file)
- [Machine Learning Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Machine_Learning/Getting_Started_with_Machine_Learning.md)

## Datasets
The following datasets, covering the years 2015–2024, are provided in the [data folder](https://github.com/IdeasClinicUWaterloo/S26_Brookfield_Renewable_Innovation_Challenge/tree/main/Sustainable_Energy_Systems/data) and may be useful for sustainability studies.

### Academic Calendar
This dataset contains daily academic calendar indicators used to model campus occupancy and energy demand patterns.

| Columns | Definition |
|:----------|:------------|
| Date | Calendar date of the observation (YYYY-MM-DD) |
| Weekend | Indicates whether the date falls on a weekend |
| Holiday | Indicates whether the date is a university recognized holiday |
| Lecture Day | Indicates whether lectures are scheduled on this date |
| Lecture Days in Month | Total number of lecture days in the corresponding month |

### Electricity Consumption Monthly
This dataset provides monthly electricity consumption for the following campus buildings:
- School of Architecture (ARC)
- Bauer Warehouse (BAU)
- Columbia Icefield (CIF)
- Columbia Lake Village South (CLV)
- Columbia Greenhouses (COG)
- Central Services Building (CSB)
- Digital Media Stratford (DMS)
- East Campus 1 (EC1)
- East Campus 2 (EC2)
- East Campus 3 (EC3)
- East Campus 4 (EC4)
- East Campus 5 (EC5)
- East Campus Hall (ECH)
- General Services Complex (GC)
- Research Advancement Centre 2 (RA2)
- Research Advancement Centre (RAC)
- Toby Jenkins Applied Health Research Building (TJB)
- UW Place (UWP)

The data may represent meter level electricity consumption rather than strictly whole building usage.

| Column | Definition |
|:-------|:-----------|
| Start Date | First day of the month for the consumption record (YYYY-MM-DD) |
| End Date | Last day of the month for the consumption record (YYYY-MM-DD) |
| Building Code | Identifier for the building (e.g., CIF, EC1, RA2) |
| Consumption | Total electricity consumption in kWh |

### Eric D. Soulis Weather Station
This dataset contains hourly weather observations from the Eric D. Soulis Weather Station.

| Column | Definition |
|:-------|:-----------|
| Year | Year of the observation |
| Month | Month of the observation |
| Day | Day of the observation |
| Hour | Hour of the observation (0–23) |
| Temperature | Air temperature in °C |
| Solar - Incoming | Incoming solar radiation in W/m² |
| Wind Speed - Average 2.0 | Average wind speed at 2 m height in m/s |
| Wind Speed - Gust 2.0 | Wind gust at 2 m height in m/s |
| Wind Direction | Wind direction in degrees |
| RH | Relative humidity in % |
