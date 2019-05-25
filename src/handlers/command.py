import logging

from telegram.ext import MessageHandler, Filters
from constants import *

from commands.ban_word import ban_word
from commands.get_banned_words import get_banned_words


def __watch(bot, update):

    logging.info(update[MESSAGE])
    message = update[MESSAGE]
    text = message[TEXT]
    splitedMsg = text.split()
    command = splitedMsg[0][1:]
    args = splitedMsg[1:]

    logging.info("Command: " + command)
    logging.info("Arguments: " + ", ".join(args))

    if command == "ban":
        ban_word(update, args)
    elif command == "words":
        get_banned_words(update, args)


def command_handler():
    return MessageHandler(Filters.command, __watch)
