import configparser
from flask_cors import CORS
from flask import Flask, request, jsonify
import os
from dev_to.api import articles, users, comments
from flask_pymongo import PyMongo
from dev_to.db import get_user

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"])

app.register_blueprint(users.users_api_v1, url_prefix="/api/v1") 
app.register_blueprint(articles.articles_api_v1, url_prefix="/api/v1")
app.register_blueprint(comments.comment_api_v1, url_prefix="/api/v1")

@app.route('/')
def index():
    return 'Welcome to the CRUD APIs'

config = configparser.ConfigParser()

# path -> ...\Library_Manage\backend\.ini
config.read(os.path.abspath(os.path.join('.ini')))

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = "mongodb+srv://devto:YOI7852j4JgvQmS9@cluster0.w8qa7p4.mongodb.net/devto?retryWrites=true&w=majority"
    # config['PROD']['DB_URI']
    app.run()