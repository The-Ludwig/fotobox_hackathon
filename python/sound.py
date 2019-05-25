import RPi.GPIO as GPIO
import time

pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)

# while True:
#     a = str(input("Do you want to change brightness? >> "))
#     if a in ["N","n","NO","No","no"]:
#         break
#     elif a in ["brighter","Brighter","up","Up","+"]:
#         GPIO.output(pin,1)
#     elif a in ["darker","Darker","down","Down","-"]:
#         GPIO.output(pin,0)
#     else:
#         print("Invalid input, please try up/down or no to exit.")

while True:
    a = input("Please enter a brightness level in floating-point format between 0.0 and 1.0: ")
    while True:
        time.sleep((1-a)/440)
        GPIO.output(pin,1)
        time.sleep(a/440)
        GPIO.output(pin,0)
