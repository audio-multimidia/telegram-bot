from constants import *
import logging
from firebase import get_banned_words as fb_get_banned_words
from messages import get_words

def get_banned_words(update, args):
    message = update[MESSAGE]
    chatId = str(message[CHAT].id)
    words = fb_get_banned_words(chatId)
    logging.info(chatId)
    get_words(words, update)

