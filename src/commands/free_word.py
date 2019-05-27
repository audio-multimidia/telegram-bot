import logging

from constants import *
from firebase import free_word as fb_free_word

def free_word(update, args):
    message = update[MESSAGE]
    chatId = message[CHAT]["id"]

    word = args[0]

    logging.info("Free word: " + word)
    
    fb_free_word(str(chatId), word, update)