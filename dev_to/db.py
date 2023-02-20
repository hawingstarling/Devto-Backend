from flask import current_app, g, Flask
from jupyter_client import client
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
from bson.objectid import ObjectId

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

# $match: Chọn document mong muốn (_id) để truy vấn
# aggregate: truy vấn nâng cao đưa vào pipeline
# pipeline: $match -> $group -> . . . -> tuần tự theo đường ống
def get_user(id):
    try:
        pipeline = [
            {
                "$match": {
                    "_id": ObjectId(id)
                }
            }
        ]

        user = db.user.aggregate(pipeline).next()
        print('user: ', user)
        return user
    except (StopIteration) as _:
        return None
    except Exception as e:
        return {}

def get_users():
    users = db.user.find({})
    return users

def update_user():
    response = db.user.update_one({
        "username": "username is updated"
    })
    return response
  
