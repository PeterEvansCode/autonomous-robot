import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motors = [
    {"dir": 20, "en": 21},
    {"dir": 26, "en": 19},
    {"dir": 13, "en": 6},
]

# Setup pins
for m in motors:
    GPIO.setup(m["dir"], GPIO.OUT)
    GPIO.setup(m["en"], GPIO.OUT)
    GPIO.output(m["en"], GPIO.LOW)

def run_motor(motor, direction, duration=2):
    GPIO.output(motor["dir"], direction)
    GPIO.output(motor["en"], GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(motor["en"], GPIO.LOW)

try:
    for i, m in enumerate(motors, start=1):
        print(f"Motor {i} forward")
        run_motor(m, GPIO.HIGH)

        print(f"Motor {i} reverse")
        run_motor(m, GPIO.LOW)

finally:
    GPIO.cleanup()
    print("GPIO cleaned up")
