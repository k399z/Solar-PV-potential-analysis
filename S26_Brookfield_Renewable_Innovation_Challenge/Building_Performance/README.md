# Building Performance 🏘
The building performance improvement section has been broken down into two sub-problems. Sub-problem 1a focuses on improving a pre-existing building's performance, while sub-problem 1b focuses on the next generation of sustainable building design. Read below for more detailed descriptions and challenges related to each sub-problem.

## 📌 Sub-problem 1a: Improving Building Performance 
Many buildings in the University of Waterloo campus were built in the 1950s –1990s and now struggle with inconsistent energy efficiency performance. To meet climate change action goals, UW must significantly reduce emissions by reducing the energy required to sustain the operations of campus buildings. Several buildings on campus, such as MC, DWE, and RCH, exhibit aging designs in multiple areas such as heating/cooling, building envelope, lighting, etc. Since these buildings were designed at a time when energy efficiency was not a primary concern, it is now apparent that the systems in these buildings need improvement. Although buildings such as E7 and QNC are relatively newly constructed, they also face challenges adapting to a climate that has more hot days and freezing nights. 

## Challenge
Choose one building at UW (any teaching, residence or plant operations building) and propose a building performance retrofit strategy that reduces the energy required to maintain its operations. After the modification, the building should still be maintained at a comfortable temperature, supply all appliance usage, and support full capacity operation for its intended usage. 

Your modification should focus on reducing the energy consumed by the building, but can also focus on other areas of improvement including human accessibility in the building or improving environmental interactions between the building and the surrounding environment. Your solution does not have to cover an entire building.  

While there are no strict budget requirements, consider whether your solution's impact can justify your project's spending. Also, consider why your solution is beneficial to the campus beyond saving energy usage and carbon emissions. 

The presentation of your solution can include a pitch deck for your solution, a small physical prototype of the new installation, or anything else that aids the demonstration. Please refer to the judging rubric and presentation instructions when planning your final presentation to the judges. 

## 📌 Sub-problem 1b: Next Generation Sustainable Building Design
As universities expand to accommodate growing student populations and evolving research needs, new campus buildings must be designed to meet higher standards of sustainability, resilience, and long-term performance. At the University of Waterloo, future development must align with institutional climate commitments while supporting modern teaching, research, and student life. 

Unlike older campus buildings constructed in the mid-to-late 20th century, new facilities have the opportunity to integrate high-performance systems from the ground up. However, designing a new building today presents its own challenges. It must anticipate a changing climate with more extreme heat and cold events, incorporate flexible learning environments, minimize operational carbon emissions, and remain adaptable for decades of evolving academic use. 

New construction decisions—such as building orientation, envelope performance, structural systems, material selection, HVAC design, lighting strategies, and renewable energy integration—have long-term implications for energy use, occupant comfort, embodied carbon, and lifecycle costs. Early-stage design choices are critical to ensuring that the building operates efficiently while maintaining comfort, accessibility, and full functional capacity. 

## Challenge
Design a new academic building for the University of Waterloo campus that demonstrates leadership in sustainable design and low-carbon construction. The building should minimize operational energy use through passive strategies and high-performance systems while reducing embodied carbon through responsible material and structural choices. It must maintain year-round thermal comfort and indoor air quality, support full academic functionality, and remain resilient to future climate conditions. 

Your solution should also consider long-term adaptability and lifecycle performance. Part of your solution will need to include site selection; this could be new greenfield development or could require the demolition of an existing structure. The first step of your research will require you to visit your chosen site/building to document the current state of the site and take measurements to inform your design. You can also visit other buildings on campus for inspiration. 

You need to communicate the details of your design to the judges. Your solution could include drawings, models, simulations, prototypes, or anything you think is useful for communicating your ideas. Please refer to the judging rubric and presentation instructions when planning your final presentation to the judges. 

## Potential Solutions
Before you begin, you should visit the sites/buildings that you are interested in improving and record/measure the site to better understand what you are seeking to improve. Make sure you take pictures to document the area(s). 

These aren’t the only solutions, but these are some of the ideas that you can take inspiration from. Feel free to mix and match any potential solutions if you feel that it is appropriate. 

| Potential Solutions | Description | Resources |
| :--- | :--- | :--- |
| **Retrofitting plans to increase thermal retention of buildings** | Improvements to the building insulation, or designs of entrance/exit doorways. | • FLIR camera to examine building heat loss<br>• Environmental quality logger to log air quality<br>• Database on energy consumption for buildings |
| **Improving energy usage due to lighting** | Energy consumed from lighting the building can be reduced through methods such as improved light scheduling/automation, or retrofitting with more efficient lighting system. | • Light sensor to measure brightness<br>• Microcontroller + sensors to prototype control systems |
| **Improving energy usage due to heating** | Investigate how each building is heated and explore more efficient solutions. | • Microcontroller-based sensor package |
| **Shading infrastructure** | Automated shading for glass windows to mitigate summer heat gain and reduce cooling costs. | • Microcontroller + light sensors<br>• Craft papers for prototyping |
| **Passive improvements to buildings** | Using natural elements (like plants) to shade buildings in summer or redirect snow in winter. | • Craft papers + cardboard for building models<br>• Heliodons for building evaluation |
| **Building monitoring + adaptation to climate** | Use a system to adjust the building to a changing climate and usage demand, or create a system to monitor building usage/performance. | • Sensor packet<br>• AI prototyping tools for dashboards<br>• Data analytics Models |
| **New infrastructure recommendation** | Proposal of a new building and a series of protocols for that building to ensure minimal increase of carbon emissions. | • Building modelling tools<br>• Crafting equipment |




## 💡 How to use this source code
An Arduino-based environmental sensor package is provided as a part of this challenge. This package has a click button, where you can switch the screen to display different sensor readings. This package can be used to collect data to support building your solution, or you can modify it to be a part of your solution! 
To switch sensor to display: hold until screen changes, then release. 

Below are the current environmental data provided: 
- ambient temperature
- air humidity
- ambient light (output range: 0-800, brighter light = larger output)
- UV index

### Setup: 
1. Download [Arduino IDE](https://docs.arduino.cc/software/ide/).
2. Navigate to the src folder, copy and paste main.cpp into a new Arduino project.
3. Use the book icon at the left of the IDE page to navigate to library manager, search and download the following: Adafruit GFX Library, Adafruit SSD1351 library, Adafruit BusIO，Grove Temperature And Humidity Sensor.
    - make sure each library is at the newest version. You can select versions from the dropdown menu below each library
4. Click upload (right-pointing arrow) on the IDE to run the code on the sensor package.


## Additional Resources: 
Several additional sensor modules are provided if you need more sensor measurements to support your project. Some potentially useful links are provided below. Please don't hesitate to reach out to the support team if there's any troubles during sensor setup. 
### FLIR One Camera Instructions
A thermal camera is provided as part of the challenge resource to help you obtain better thermal data around the building. 
1. Download the Flir One app from your app store.
2. Launch the application, then plug the camera into your phone's charging port.
3. Press the power button at the bottom of the camera and wait. The module should first display an orange light, then flashing green when functioning.
4. If the module has no response while powering or connecting, use the charging wire inside the case to charge the module, then retry.

   For more information, navigate to FLIR Cameras.pdf
### Sensors and resources
- general resource: [a comprehensive introduction to sensors](https://wiki.seeedstudio.com/Grove_Starter_Kit_v3/) 
- [electric current sensor]( https://wiki.seeedstudio.com/Grove-Electricity_Sensor/)
- [barometer sensor](https://wiki.seeedstudio.com/grove_barometer_sensor_spa06_003/)
       - You MUST unplug all other sensors, and toggle the black switch on the shield to 3.3V before plugging this sensor in
### General Information
- [UW Building Floor Plans](https://uwaterloo.ca/plant-operations/floor-plans)
- [Energy data | Sustainability |  University of Waterloo](https://uwaterloo.ca/sustainability/our-progress/energy-data)
- [Environmental Office's Ongoing Projects](https://uwaterloo.ca/sustainability-living-lab/catalogs/categories/climate-change-and-energy?page=0)
- [LEED Attributes in EV3](https://uwaterloo.ca/environment/about/ev3-leedr-platinum-certified)
- [Campus Plan](https://uwaterloo.ca/campus-plan/university-waterloo-campus-plan)
- [Campus Progression Through Imagery](https://storymaps.arcgis.com/stories/7a05e37300114e0ca33d7b3cfc860dd8)

  

---


