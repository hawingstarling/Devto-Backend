import os
import configparser
from dotenv import load_dotenv
from flask_cors import CORS
from flask_pymongo import PyMongo
from dev_to.db import get_user
from flask import Flask, request, jsonify
from dev_to.api import articles, users, comments, notifications

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

# Register blueprint to seperate module
app.register_blueprint(users.users_api_v1, url_prefix="/api/v1") 
app.register_blueprint(articles.articles_api_v1, url_prefix="/api/v1")
app.register_blueprint(comments.comment_api_v1, url_prefix="/api/v1")
app.register_blueprint(notifications.notification_api_v1, url_prefix="/api/v1")

load_dotenv()

@app.route('/')
def index():
    return 'Welcome to the CRUD APIs'

config = configparser.ConfigParser()

# path -> ...\Library_Manage\backend\.ini
config.read(os.path.abspath(os.path.join('.ini')))

if __name__ == "__main__":
    app.config['DEBUG'] = True
    # app.config['MONGO_URI'] = "mongodb+srv://devto:YOI7852j4JgvQmS9@cluster0.w8qa7p4.mongodb.net/devto?retryWrites=true&w=majority"
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    # app.config['MONGO_URI'] = config['PROD']['DB_URI']
    app.run()
