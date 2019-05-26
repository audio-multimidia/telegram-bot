from constants import *

from firebase import get_banned_words as fb_get_banned_words


def format_words(words):
    return ", ".join(words)


def get_banned_words(update, args):
    message = update[MESSAGE]
    chatId = str(message[CHAT].id)
    words = fb_get_banned_words(chatId)

    update[MESSAGE].reply_text("Current banned words: " + format_words(words))

