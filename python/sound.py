import RPi.GPIO as GPIO
import time

pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,1)

a=input("Do you want to quit?")
GPIO.output(pin,0)