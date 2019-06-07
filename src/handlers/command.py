import logging
import re

from telegram.ext import MessageHandler, Filters
from constants import *

from commands.ban_word import ban_word
from commands.get_banned_words import get_banned_words
from commands.free_word import free_word
from commands.free_all import free_all
from messages import user_unauthorized


def __watch(bot, update):
    
    message = update[MESSAGE]    
    usr_id = update[MESSAGE].from_user.id
    
    text = message[TEXT]
    splitedMsg = text.split()
    command = cut_command(splitedMsg[0][1:])
    args = splitedMsg[1:]

    # logging.info("UPDATE: " + str(update))
    # logging.info("idUser: " + str(usr_id))
    # logging.info("Command: " + command)
    # logging.info("Arguments: " + ", ".join(args))

    sender = message.chat.get_member(usr_id)
    logging.info(sender)
    logging.info(sender.status)
    if sender.status == "creator" or sender.status == "administrator":
        logging.info(command)
        
        if command == "ban":
            ban_word(update, args)
        elif command == "words":
            get_banned_words(update, args)
        elif command == "free":
            free_word(update, args)
        elif command == "freeall":
            free_all(update)

    else:
        user_unauthorized(update)

def command_handler():
    return MessageHandler(Filters.command, __watch)

def cut_command(command):
    return re.sub(r"@WordBlockBot", "", command)