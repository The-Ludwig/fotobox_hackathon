import sys
import time
import telepot 
from telepot.loop import MessageLoop
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup
from functools import partial

PICTURE_COMMAND = "Take picture"
KEYBOARD = ReplyKeyboardMarkup(keyboard=[
                   [KeyboardButton(text=PICTURE_COMMAND)]
               ])

def handle(take_picture_callback, bot, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print("\t", msg)
    if content_type == 'text':
        if("/start" == msg["text"]):
            
            bot.sendMessage(chat_id, "Welcome to our photobox! Press \""+PICTURE_COMMAND+"\" to take a photo!", 
                reply_markup=KEYBOARD)
        elif(PICTURE_COMMAND == msg["text"]):
            print("Trying to send foto.")
            bot.sendMessage(chat_id, 'Your photo is being processed, please wait a second!', reply_markup=KEYBOARD)
            filepath = take_picture_callback()
            with open(filepath, "rb") as file:
                bot.sendPhoto(chat_id, file)   
        else:
            print("No photo will be send")


def startBot(take_picture_callback, token="892994258:AAGN5uZ6qrhbolC1YKg-Po9YUam3zU827ZA"  ):
    bot = telepot.Bot(token)
    bound_handle = partial(handle, take_picture_callback, bot)
    MessageLoop(bot, bound_handle).run_as_thread()
    print ('Bot startet, listening...')