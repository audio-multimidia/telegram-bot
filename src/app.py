import logging

from telegram.ext import Updater
from handlers.text import text_handler
from logger import config_logger
from constants import *
import config

def init():
    config_logger()
    
    updater = Updater(token=config.get(TELEGRAM_TOKEN))
    dispatcher = updater.dispatcher
    
    # add handlers
    dispatcher.add_handler(text_handler())

    updater.start_polling()
    logging.info("Bot is listening for messages...")

init()