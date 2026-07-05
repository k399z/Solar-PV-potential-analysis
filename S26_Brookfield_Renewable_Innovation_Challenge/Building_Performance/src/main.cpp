// --- INTEGRATED CODE: OLED + DHT SENSOR ---
#include <Arduino.h>
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1351.h>
#include "Grove_Temperature_And_Humidity_Sensor.h"

// Display Pins
#define OLED_CS   10
#define OLED_DC    9
#define OLED_RST   8
Adafruit_SSD1351 display(128, 128, &SPI, OLED_CS, OLED_DC, OLED_RST);

const int button_pin = 4;
const int uv_pin = A1;
const int light_pin = A2;

float lightValue = 0;
float uvIndex = 0.0;
float dhtHumidity = 0.0;
float dhtTemperature = 0.0;

// DHT Sensor Setup
#define DHTTYPE DHT11   // DHT 11
#define DHTPIN 2        // what pin we're connected to
DHT dht(DHTPIN, DHTTYPE);

struct SensorPage {
  const char* label;
  // For DHT, valuePtr is ignored and custom display logic is used
  float* valuePtr;
};

SensorPage mySensors[] = {
  {"Temp & Humidity", NULL}, // DHT sensor page (custom display)
  {"Ambient Light", &lightValue},
  {"UV Index", &uvIndex},
};

const int totalPages = sizeof(mySensors) / sizeof(mySensors[0]);
int currentChannel = 0;
bool lastButtonState = LOW;

// --- NEW VARIABLES FOR TIMING ---
unsigned long lastUpdate = 0;      // Stores the last time we read sensors
const long interval = 1000;        // Interval at which to refresh (1 second)

void setup() {
  pinMode(button_pin, INPUT);
  display.begin();
  display.fillScreen(0x0000);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - lastUpdate >= interval) {
    lastUpdate = currentMillis;

    // Read Sensors
    lightValue = analogRead(light_pin);
    int uv_val = analogRead(uv_pin);
    Serial.println(uv_val);
    /*float voltage = (uv_val * 5.0) / 1024.0;
    float intensity = 307.0 * voltage;
    uvIndex = (uv_val*1000/4.3-83)/21;*/
    float voltage = (uv_val * 5.0) / 1024.0;
    float intensity = 307.0 * voltage;
    uvIndex = intensity / 200.0;

    // Read DHT sensor
    float temp_hum_val[2] = {0};
    if (!dht.readTempAndHumidity(temp_hum_val)) {
      dhtHumidity = temp_hum_val[0];
      dhtTemperature = temp_hum_val[1];
    } else {
      dhtHumidity = -1;
      dhtTemperature = -1;
    }

    // Refresh Display
    display.fillScreen(0x0000);
    display.setTextColor(0xFFFF);

    if (currentChannel == 0) {
      // DHT sensor page: show both temp and humidity
      display.setCursor(5, 40);
      display.setTextSize(1);
      display.println("Temp & Humidity");
      display.setCursor(10, 70);
      display.setTextSize(2);
      if (dhtTemperature >= 0 && dhtHumidity >= 0) {
        display.print(dhtTemperature, 1);
        display.println(" C  ");
        display.print(dhtHumidity, 1);
        display.println(" %");
      } else {
        display.print("Sensor Err");
      }
    } else {
      // Other pages: use valuePtr
      display.setCursor(5, 50);
      display.setTextSize(1);
      display.println(mySensors[currentChannel].label);
      display.setCursor(20, 80);
      display.setTextSize(2);
      if (mySensors[currentChannel].valuePtr != NULL) {
        display.print(*(mySensors[currentChannel].valuePtr));
      }
    }
  }

  // BUTTON LOGIC
  bool buttonReading = digitalRead(button_pin);
  if (buttonReading == HIGH && lastButtonState == LOW) {
    currentChannel = (currentChannel + 1) % totalPages;
    lastUpdate = currentMillis - interval;
     // debounce
  }
  lastButtonState = buttonReading;
}

