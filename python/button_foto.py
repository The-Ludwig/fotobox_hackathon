import RPi.GPIO as GPIO
import time as time 
import subprocess

BUTTON_PORT = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON_PORT, GPIO.RISING)

def capture():
    print("image taken")
    subprocess.run(["gphoto2", "--capture-image-and-download"])

GPIO.add_event_callback(BUTTON_PORT, capture)

while True:
    time.sleep(1)