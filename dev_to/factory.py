from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
##from flask_bcrypt import Bcrypt
##from flask_jwt_extended import JWTManager

from bson import json_util, ObjectId
from datetime import datetime, timedelta

from dev_to.api import articles, users, comments, notifications
class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    # Register blueprint to seperate module
    app.register_blueprint(users.users_api_v1, url_prefix="/api/v1") 
    app.register_blueprint(articles.articles_api_v1, url_prefix="/api/v1/articles")
    app.register_blueprint(comments.comment_api_v1, url_prefix="/api/v1")
    app.register_blueprint(notifications.notification_api_v1, url_prefix="/api/v1")

    @app.route('/')
    def index():
        return 'Welcome to the CRUD APIs'

    return app