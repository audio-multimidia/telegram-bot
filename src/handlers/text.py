from telegram.ext import MessageHandler, Filters
from constants import *
import logging

def __watch(update, context):
    message = context[MESSAGE]
    chat = message[CHAT]
    text = message[TEXT]
    logging.info (chat)
    logging.info (text)

def text_handler():
    return MessageHandler(Filters.text, __watch)
