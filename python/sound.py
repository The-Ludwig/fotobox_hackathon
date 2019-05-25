import RPi.GPIO as GPIO
import time

pin = 40
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,1)