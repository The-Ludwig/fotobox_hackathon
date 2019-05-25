import camera
import photobox_bot
import time 

with open("telegramkey.txt", "r") as file:
    token = file.read()

photobox_bot.startBot(camera.trigger, token)

while(True):
    time.sleep(1)