import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17  # GPIO17 (Pin 11)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Motion Sensor Test (Press Ctrl+C to stop)\n")

try:
    while True:
        if GPIO.input(PIR_PIN) == 1:
            print("Motion Detected!")
        else:
            print("No Motion")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped and GPIO cleaned up.")

