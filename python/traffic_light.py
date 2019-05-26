import RPi.GPIO as GPIO
import time

pins = { "red":36 , "yellow":38 , "green":40 }

GPIO.setmode(GPIO.BOARD)

for colour in pins:
    GPIO.setup(pins[colour],GPIO.OUT)

# GPIO.output(36,1)
# GPIO.output(38,1)
# GPIO.output(40,1)
# time.sleep(100)

while True:
    time.sleep(20)
    GPIO.output(pins["green"],0)
    GPIO.output(pins["yellow"],1)
    time.sleep(3.6)
    GPIO.output(pins["yellow"],0)
    GPIO.output(pins["red"],1)
    time.sleep(35)
    GPIO.output(pins["yellow"],1)
    time.sleep(1.4)
    GPIO.output(pins["red"],0)
    GPIO.output(pins["yellow"],0)
    GPIO.output(pins["green"],1)
