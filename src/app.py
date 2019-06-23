import logging

from telegram.ext import Updater
from telegram import Bot

from handlers.text import text_handler
from handlers.audio import audio_handler
from handlers.command import command_handler

from logger import config_logger
from constants import *

import config
import firebase

def init():
    config_logger()

    updater = Updater(token=config.get(TELEGRAM_TOKEN))
    dispatcher = updater.dispatcher

    # add handlers
    dispatcher.add_handler(command_handler())
    dispatcher.add_handler(text_handler())
    dispatcher.add_handler(audio_handler())

    updater.start_polling()
    logging.info("Bot is listening for messages...")
    

init()
