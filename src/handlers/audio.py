from telegram.ext import MessageHandler, Filters
from telegram import File
from constants import *
from util.convert_audio import ogg_to_wav
from core.audio import word_block_audio
from firebase import get_banned_words

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
        
        convertedPath = ogg_to_wav(file_id + OGG_EXTENSION)
        
        chat = message[CHAT]
        banned_words = get_banned_words(str(chat.id))
        banned_words_dict = dict.fromkeys(banned_words, True)

        newPath = word_block_audio(convertedPath, banned_words_dict)

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