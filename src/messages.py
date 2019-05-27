from constants import *

def word_exists(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" is already on the black list.")

def word_doesnt_exists(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" is already free.")

def success_ban(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" has been added to the black list.")

def success_free(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" has been removed from the black list.")

def format_words(words, key):
    if key:
        return "\n▪".join(words) 
    return ", ".join(words)

def get_words(words, update):
    size = len(words)
    if size == 0:
        update[MESSAGE].reply_text("There is no banned words yet")
    elif size <=30:
        update[MESSAGE].reply_text("Current banned words: \n▪" + format_words(words, True))
    else:
        update[MESSAGE].reply_text("Current banned words:\n" + format_words(words, False))
