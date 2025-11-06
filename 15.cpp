#include "DHT.h"

#define DHT11PIN 4
DHT dht(DHT11PIN, DHT11);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float humi = dht.readHumidity();
  float temp = dht.readTemperature();

  // Print the readings
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" ºC");

  Serial.print("Humidity: ");
  Serial.print(humi);
  Serial.println(" %");

  delay(1000);
}

