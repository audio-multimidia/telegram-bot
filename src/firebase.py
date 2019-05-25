import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config
import logging

# Use a service account
cred = credentials.Certificate(config.get("google_application_credentials"))
firebase_admin.initialize_app(cred)

db = firestore.client()
transaction = db.transaction()


@firestore.transactional
def banWordTransaction(transaction, chatId, word):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get(transaction=transaction)

    transaction.update(doc_ref, {"words": list(set(snapshot.get("words") + [word]))})


def ban_word(chatId, word):
    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get()

    if not snapshot.exists:
        doc_ref.set({"words": [word]})
    else:
        banWordTransaction(transaction, chatId, word)


def get_banned_words(chatId):

    doc_ref = db.collection("servers").document(chatId)
    snapshot = doc_ref.get()

    words = []

    if snapshot.exists:
        words = snapshot.get("words")

    return words
