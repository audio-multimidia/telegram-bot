import logging
import re

from constants import *
from firebase import ban_word as fb_ban_word
from firebase import get_banned_words as fb_get_banned_words

def remove_special_chars(word):
    return re.sub(r"[0-9!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?]", "", word)


def ban_word(update, args):
    message = update[MESSAGE]
    chatId = message[CHAT]["id"]

    word = args[0]

    cleanWord = remove_special_chars(word)

    logging.info("Banned word: " + cleanWord)

    if cleanWord is not "":
        fb_ban_word(str(chatId), cleanWord, update)
    else:
        message.reply_text("The word should have at least one letter.")
