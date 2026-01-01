import RPi.GPIO as GPIO

IN1 = 20  # example pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)

# Set high, then read back
GPIO.output(IN1, GPIO.HIGH)
print(GPIO.input(IN1))  # Should print 1
