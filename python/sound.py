import RPi.GPIO as GPIO
import time

pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)

while True:
    a = input("Do you want to continue? ")
    if a in ["N","n","NO","No","no"]:
        break
    elif a:
        GPIO.output(pin,1)
    else:
        GPIO.output(pin,0)