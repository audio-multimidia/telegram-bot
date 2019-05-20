import logging

from telegram.ext import Updater
from telegram import Bot

from handlers.text import text_handler
from handlers.audio import audio_handler

from logger import config_logger
from constants import *
import config

def init():
    config_logger()
    

    # bot = Bot(token=config.get(TELEGRAM_TOKEN))
    # bot.getFile

    updater = Updater(token=config.get(TELEGRAM_TOKEN))
    dispatcher = updater.dispatcher
    
    # add handlers
    dispatcher.add_handler(text_handler())
    dispatcher.add_handler(audio_handler())

    updater.start_polling()

    logging.info("Bot is listening for messages...")

init()