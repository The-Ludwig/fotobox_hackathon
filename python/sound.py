import RPi.GPIO as GPIO
import time

pin = 40
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,1)