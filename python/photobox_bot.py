import sys
import time
import telepot 
from telepot.loop import MessageLoop
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup
from functools import partial

from PIL import Image
import numpy as np

CHARS = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

PICTURE_COMMAND = "Take picture"
KEYBOARD = ReplyKeyboardMarkup(keyboard=[
                   [KeyboardButton(text=PICTURE_COMMAND)]
               ])

def getAsciiArt(filename):
    SC, GCF, WCF = 0.09, 1.5, 7/4
    img = Image.open(filename)
    S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
    img = np.sum( np.asarray( img.resize(S) ), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(CHARS.size-1)

    return "\n".join(("".join(r) for r in CHARS[img.astype(int)])) 

def handle(take_picture_callback, bot, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print("\t", msg)
    if content_type == 'text':
        if("/start" == msg["text"]):
            bot.sendMessage(chat_id, "Welcome to our photobox! Press \""+PICTURE_COMMAND+"\" to take a photo!", 
                reply_markup=KEYBOARD)
        elif(PICTURE_COMMAND == msg["text"]):
            print("Trying to take foto.")
            bot.sendMessage(chat_id, "Photo will be taken in", reply_markup=KEYBOARD)
            for i in range(5):
                bot.sendMessage(chat_id, str(5-i)+"...", reply_markup=KEYBOARD)
                time.sleep(1)
            bot.sendMessage(chat_id, 'Your photo is being processed, please wait for about a minute!', reply_markup=KEYBOARD)
            # try:
            filepath = take_picture_callback()
            print("sending {}".format(filepath))
            with open(filepath, "rb") as file:

                bot.sendPhoto(chat_id, file) 
            print("Foto was send!")
            # except FileNotFoundError:
            #     bot.sendMessage(chat_id, 'Camera not connected', reply_markup=KEYBOARD)
            #     print("Camera does not seem to be reachable")
        else:
            print("No photo will be send")


def startBot(take_picture_callback, token):
    bot = telepot.Bot(token)
    bound_handle = partial(handle, take_picture_callback, bot)
    MessageLoop(bot, bound_handle).run_as_thread()
    print ('Bot startet, listening...')