from telegram.ext import Updater
from telegram.ext import CommandHandler

with open("key.txt") as f:
    key = f.read()
updater = Updater(token=key, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def start(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id, text="Hi, ich bin der Pi in der Photobox.")


def trigger(update, context):
    camera.trigger
