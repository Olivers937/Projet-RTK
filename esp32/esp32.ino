#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <LiquidCrystal.h>

// WiFi Credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Target Server for JSON Transmission
const char* serverName = "http://192.168.1.100/distance"; // Replace with your server IP

// Pin Definitions (ESP32-WROOM)
const int trigPin = 0;   // D3
const int echoPin = 26;  // External GPIO
LiquidCrystal lcd(5, 4, 23, 18, 19, 17); // D1, D2, D4, D5, D6, D7

#define SOUND_SPEED 0.034

long duration;
float distanceCm;

void setup() {
  Serial.begin(115200);
  
  // LCD Initialization
  lcd.begin(16, 2);
  lcd.print("Distance Sensor");
  
  // WiFi Connection
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  // Ultrasonic Sensor Setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Measure Distance
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * SOUND_SPEED / 2;
  
  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Distance:");
  lcd.setCursor(0, 1);
  lcd.print(distanceCm);
  lcd.print(" cm");
  
  // Send JSON via HTTP POST
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");
    
    // Create JSON payload
    StaticJsonDocument<200> jsonDoc;
    jsonDoc["distance"] = distanceCm;
    jsonDoc["unit"] = "cm";
    
    char jsonBuffer[256];
    serializeJson(jsonDoc, jsonBuffer);
    
    int httpResponseCode = http.POST(jsonBuffer);
    Serial.print("HTTP Response: ");
    Serial.println(httpResponseCode);
    
    http.end();
  }
  
  delay(5000); // Wait 5 seconds between transmissions
}