from firebase import get_banned_words
from telegram.ext import MessageHandler, Filters
from constants import *
import logging
import unicodedata
from messages import *


def remove_accents(word):
    return "".join(
        (
            c
            for c in unicodedata.normalize("NFD", word)
            if unicodedata.category(c) != "Mn"
        )
    )


def clean_word(word):
    return remove_accents(word).lower()


def __watch(update, context):
    message = context[MESSAGE]
    chat = message[CHAT]
    text = message[TEXT]
    usr_id = context[MESSAGE].from_user.id
    sender = message.chat.get_member(usr_id).user

    banned_words = get_banned_words(str(chat.id))
    cleared_words = map(clean_word, banned_words)

    banned_words_dict = dict.fromkeys(cleared_words, True)

    textWords = text.split()

    for word in textWords:
        if banned_words_dict.get(clean_word(word)):
            censored_message(update, chat.id, sender, textWords, banned_words_dict)
            message.delete()
            break

    logging.info(chat)
    logging.info(text)

def text_handler():
    return MessageHandler(Filters.text, __watch)
