import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17  # GPIO17 (Pin 11)
GPIO.setup(SENSOR_PIN, GPIO.IN)

print("Reading Soil Moisture Sensor... Press Ctrl+C to stop.\n")

try:
    while True:
        if GPIO.input(SENSOR_PIN) == 0:
            print("Soil is Wet")
        else:
            print("Soil is Dry")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped and GPIO cleaned up.")

