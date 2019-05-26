import sys
import time
import telepot 
from telepot.loop import MessageLoop
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup
from functools import partial

from .model import Image 

PICTURE_COMMAND = "Take picture"
LAST_SEND_COMMAND = "Send last photo"
KEYBOARD = ReplyKeyboardMarkup(keyboard=[
                   [KeyboardButton(text=PICTURE_COMMAND)],
                   [KeyboardButton(text=LAST_SEND_COMMAND)]
               ])

def handle(take_picture_callback, bot, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print("\t", msg)
    if content_type == 'text':
        if(LAST_SEND_COMMAND == msg["text"]):
            bot.sendMessage(chat_id, "Trying to send the last photo, please stand by.", 
                reply_markup=KEYBOARD)
            try:
                fileinfo = Image.select().order_by("datetime")[-1]
                filepath = fileinfo.loc
                timestamp = fileinfo.datetime.strftime("%H:%M:%S")
                print("sending last foto ({}) via telegram".format(filepath))
                with open(filepath, "rb") as file:
                    # bot.sendMessage(chat_id, 'Ascii-Art:\n'+getAsciiArt(filepath))
                    bot.sendPhoto(chat_id, file) 
                bot.sendMessage(chat_id, "This photo was taken at time "+timestamp, reply_markup=KEYBOARD)
                print("Foto was send!")
            except Exception as e:
                bot.sendMessage(chat_id, 'Some error occurred...', reply_markup=KEYBOARD)
                print("Error while sending last photo.")
                print(f'Error code: {e}')
        elif(PICTURE_COMMAND == msg["text"]):
            print("Trying to take foto for telegram bot.")
            bot.sendMessage(chat_id, "Photo will be taken in", reply_markup=KEYBOARD)
            for i in range(5):
                bot.sendMessage(chat_id, str(5-i)+"...", reply_markup=KEYBOARD)
                time.sleep(1)
            bot.sendMessage(chat_id, 'Your photo is being processed, please wait for about a minute!', reply_markup=KEYBOARD)
            try:
                filepath = take_picture_callback()
                print("sending {} via telegram".format(filepath))
                with open(filepath, "rb") as file:
                    # bot.sendMessage(chat_id, 'Ascii-Art:\n'+getAsciiArt(filepath))
                    bot.sendPhoto(chat_id, file) 
                bot.sendMessage(chat_id, 'Photo was taken and sent.', reply_markup=KEYBOARD)
                print("Foto was send!")
            except FileNotFoundError:
                bot.sendMessage(chat_id, 'Camera not connected', reply_markup=KEYBOARD)
                print("Camera does not seem to be reachable")
        else:
            bot.sendMessage(chat_id, "Welcome to our photobox! Press \""+PICTURE_COMMAND+"\" to take a photo or\""+LAST_SEND_COMMAND+"\" to send the last picture taken.", 
                reply_markup=KEYBOARD)


def startBot(take_picture_callback, token):
    bot = telepot.Bot(token)
    bound_handle = partial(handle, take_picture_callback, bot)
    MessageLoop(bot, bound_handle).run_as_thread()
    print ('Bot startet, listening...')