import os
import json
import firebase_admin
from email import message
from .. import db
from typing import Any
from bson.objectid import ObjectId
from firebase_admin import credentials, messaging

# Import json serviceAccountKey
# D:/SAVE.VSCODE/Learn Language Programming/Dev.to/backend/serviceAccountKey.json
with open(os.path.abspath(os.path.join('serviceAccountKey.json')), 'r') as f:
    serviceAccount = json.load(f)    

class Notification:
    def __init__(self):
        firebaseCred = credentials.Certificate(serviceAccount)
        firebaseApp = firebase_admin.initialize_app(firebaseCred)

    def SendToToken(self, registrationToken, title, body, data=None) -> Any:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            data=data,
            token=registrationToken
        )
        response = messaging.send(message)
        print(response)

        return response
    
    def SendToTokenMulticast(self, registrationToken, title, body, data=None) -> Any:
        assert isinstance(registrationToken, list)

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            data=data,
            token=registrationToken
        )
        response = messaging.send_multicast(message)
        print(response)

        return response

    def SendToTopic(self, topic, title, body, data=None) -> Any:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            topic=topic
        )
        response = messaging.send(message)
        print(response)
        
        return response

    def UpdateTokenAccount(AccountId, Token, action="INSERT"):
        if action == "INSERT":
            db.Token.find_one_and_update(
                { "_id": ObjectId(AccountId) },
                { "$addToSet": { "Token": Token } },
                { "new": True }
            )
            return "DONE"
        else:
            db.Token.find_one_and_update(
                { "_id": ObjectId(AccountId) },
                { "$pull": { "Token": Token } },
                { "new": True }
            )
            return "DONE"
