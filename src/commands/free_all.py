import logging

from constants import *
from firebase import free_all as fb_free_all

def free_all(update):
    message = update[MESSAGE]
    chatId = message[CHAT]["id"]
    
    fb_free_all(str(chatId), update)