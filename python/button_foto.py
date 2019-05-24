import RPi.GPIO as GPIO
import time as time 
import subprocess
import datetime
import os

BUTTON_PORT = 3
IMG_NAME = "capt0000.jpg"
DIR_NAME = "fotobox"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def save_img():
    cwd = os.getcwd()
    filename = cwd+"/"+datetime.datetime.now().strftime("%d.%m.%Y_%H:%M:%S")

    if not os.path.exists(cwd+"/"+DIR_NAME):
        os.makedirs(cwd+"/"+DIR_NAME)
    os.rename(cwd+"/"+IMG_NAME, filename)

def capture(channel):
    print("image taken")
    subprocess.call(["gphoto2", "--capture-image-and-download"])
    save_img()

GPIO.add_event_detect(BUTTON_PORT, GPIO.FALLING, callback=capture, bouncetime=2000)

while True:
    time.sleep(1)