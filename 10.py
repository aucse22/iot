import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO4 (Pin 7)

print("Reading DHT11 Sensor... Press Ctrl+C to stop.\n")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.1f}°C | Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from DHT11 sensor")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nProgram stopped.")

