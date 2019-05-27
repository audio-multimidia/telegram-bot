import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config
import logging
from messages import *

# Use a service account
cred = credentials.Certificate(config.get("google_application_credentials"))
firebase_admin.initialize_app(cred)

db = firestore.client()
transaction = db.transaction()

@firestore.transactional
def banWordTransaction(transaction, chatId, word, update):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get(transaction=transaction)
    words = snapshot.get("words")

    if(word in words):
        word_exists(word, update)
    else:
        transaction.update(doc_ref, {"words": words + [word]})
        success_ban(word, update)

@firestore.transactional
def freeWordTransaction(transaction, chatId, word, update):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get(transaction=transaction)
    words = snapshot.get("words")

    if(word not in words):
        word_doesnt_exists(word, update)
    else:
        #TODO
        new_words = words.remove(word)
        logging.info(new_words)
        transaction.update(doc_ref, {"words": new_words})
        success_free(word, update)

def ban_word(chatId, word, update):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get()

    if not snapshot.exists:
        doc_ref.list({"words": [word]})
    else:
        banWordTransaction(transaction, chatId, word, update)

def free_word(chatId, word, update):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get()

    if snapshot.exists:
        freeWordTransaction(transaction, chatId, word, update)
    else:
        word_doesnt_exists(word, update)


def get_banned_words(chatId):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get()

    words = []

    if snapshot.exists:
        words = snapshot.get("words")

    return words