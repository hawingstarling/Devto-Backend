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
        return user
    except (StopIteration) as _:
        return None
    except Exception as e:
        return {}

def get_users():
    users = db.user.find({})
    return users

def update_user(id, username):
    response = db.user.update_one(
        { "_id": ObjectId(id) },
        { "$set": { "username": username } }
    )

    return response
  
def delete_user(id):
    response = db.user.delete_one({ "_id": ObjectId(id) })
    return response

def get_acticles():
    articles = db.article.find({})
    return articles

def get_article(id):
    try:
        pipeline = [
            {
                "$match": {
                    "_id": ObjectId(id)
                }
            }
        ]

        article = db.article.aggregate(pipeline).next()
        return article
    except (StopIteration) as _:
        return None
    except Exception as e:
        return {}

def update_article(id, title, body_markdown, cover_image):
    response = db.article.update_one(
        { "_id": ObjectId(id) },
        { "$set": { 
                "title": title, 
                "body_markdown": body_markdown ,
                "cover_image": cover_image
            } 
        }
    )

    return response
  
def delete_article(id):
    response = db.article.delete_one({ "_id": ObjectId(id) })
    return response