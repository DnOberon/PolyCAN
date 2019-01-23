splash = ("   ___       __     ________   _  __\n"
          +"  / _ \___  / /_ __/ ___/ _ | / |/ /\n"
          +" / ___/ _ \/ / // / /__/ __ |/    / \n"
          +"/_/   \___/_/\_, /\___/_/ |_/_/|_/  \n"
          +"            /___/                   \n")
print(splash)

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import google.cloud.exceptions

# Use the application default credentials
try:
    cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'secret.json'))
    firebase_admin.initialize_app(cred)
except FileNotFoundError:
    options = {
        'serviceAccountId' : 'firebase-adminsdk-izlwr@polycan-222600.iam.gserviceaccount.com',
        }
    firebase_admin.initialize_app(options=options)

db = firestore.client()
input_prompt = ""