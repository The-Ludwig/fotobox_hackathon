import RPi.GPIO as GPIO
import time as time 
import subprocess
import datetime
import os

BUTTON_PORT = 3
IMG_NAME = "capt0000.jpg"
DIR_NAME = ".images"
FNULL = open(os.devnull, 'w')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def save_img():
    cwd = os.getcwd()
    filename = cwd+"/"+DIR_NAME+"/"+datetime.datetime.now().strftime("%d.%m.%Y_%H_%M_%S")+".jpg"

    if not os.path.exists(cwd+"/"+DIR_NAME):
        os.makedirs(cwd+"/"+DIR_NAME)
    os.rename(cwd+"/"+IMG_NAME, filename)

    return filename

def capture(channel):
    subprocess.call(["gphoto2", "--capture-image-and-download"], stdout=FNULL, stderr=subprocess.STDOUT)
    filename = save_img()
    print("Image saved as {}".format(filename))
    del_img()
    return filename

def del_img():
    if os.path.isfile(os.getcwd()+"/"+IMG_NAME):
        os.remove(os.getcwd()+"/"+IMG_NAME)

GPIO.add_event_detect(BUTTON_PORT, GPIO.FALLING, callback=capture, bouncetime=5000)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    FNULL.close()
    GPIO.cleanup()