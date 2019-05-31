from telegram.ext import MessageHandler, Filters
from telegram import File
from constants import *
from util.convert_audio import ogg_to_mp3

import os
import logging


def __watch(bot, update):
    message  = update[MESSAGE]

    audioObj = message[VOICE]

    if audioObj:
        logging.info("[audio_handler]")
        logging.info(audioObj)

        file_id = audioObj[FILE_ID]
        audioFile = bot.get_file(file_id)
        fileName = PATH + file_id + OGG_EXTENSION
        audioFile.download(fileName)
        newPath = ogg_to_mp3(file_id + OGG_EXTENSION)

        usr_id = message.from_user.id
        sender = message.chat.get_member(usr_id).user
        username = sender.username

        message.reply_audio(open(newPath, RB), title="Audio from @" + username)
        message.delete()

def audio_handler():
    path = "tmp/audios"
    if not os.path.exists(path):
        os.makedirs(path)
    return MessageHandler(Filters.all, __watch)