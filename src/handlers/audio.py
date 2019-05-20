from telegram.ext import MessageHandler, Filters
from telegram import File
from constants import *

import os
import logging

def __watch( bot, update):
    audioObj = update[MESSAGE][VOICE]
    if audioObj:
        logging.info ("[audio_handler]")
        logging.info (audioObj)

        file_id = audioObj["file_id"]
        audioFile = bot.get_file(file_id)
        audioFile.download("tmp/audios/" + file_id + ".oga")

    
def audio_handler():
    path = "tmp/audios"
    if (not os.path.exists(path)):
        os.makedirs(path)
    return MessageHandler(Filters.all, __watch)
