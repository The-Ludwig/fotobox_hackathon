import RPi.GPIO as GPIO
import time as time 
import subprocess

BUTTON_PORT = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def capture(wat):
    print(wat)
    print("image taken")
    subprocess.run(["gphoto2", "--capture-image-and-download"])

GPIO.add_event_detect(BUTTON_PORT, GPIO.FALLING, callback=capture, bouncetime=2000)

while True:
    time.sleep(1)