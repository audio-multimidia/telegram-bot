import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config

# Use a service account
cred = credentials.Certificate(config.get("google_application_credentials"))
firebase_admin.initialize_app(cred)

db = firestore.client()
