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

        file_id = audioObj[FILE_ID]
        audioFile = bot.get_file(file_id)
        audioFile.download(PATH + file_id + AUDIO_EXTENSION)

    
def audio_handler():
    path = "tmp/audios"
    if (not os.path.exists(path)):
        os.makedirs(path)
    return MessageHandler(Filters.all, __watch)
