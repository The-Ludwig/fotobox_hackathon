import subprocess
from datetime import datetime
import os
BUTTON_PORT = 3
IMG_NAME = "capt0000.jpg"
DIR_NAME = "images"


def rename_img():
    output = os.path.join(
        DIR_NAME, "{:%Y-%m-%dT%H:%M:%S}.jpg".format(datetime.now()))
    os.makedirs(DIR_NAME, exist_ok=True)
    os.rename(IMG_NAME, output)
    print(output)
    return output

def trigger(channel=0):
    del_img()
    subprocess.call(["gphoto2", "--capture-image-and-download"])
    filename = rename_img()
    print("Image saved as {}".format(filename))
    return filename

def del_img():
    if os.path.isfile(os.getcwd()+"/"+IMG_NAME):
        os.remove(os.getcwd()+"/"+IMG_NAME)


# def trigger():
#    print("Test")
#    return "test_pfad"
