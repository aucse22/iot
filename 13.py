import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 17  # GPIO17 (Pin 11)
LED_PIN = 3     # GPIO3 (Pin 5)

GPIO.setup(SOUND_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Sound Sensor with LED Indicator (Press Ctrl+C to stop)\n")

try:
    while True:
        if GPIO.input(SOUND_PIN) == 1:
            print("Sound Detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn ON LED
        else:
            print("No Sound")
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn OFF LED
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped and GPIO cleaned up.")

