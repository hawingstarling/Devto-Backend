import configparser
from flask import Flask, request, jsonify
# Import lib to load variable env 
# from dotenv import load_dotenv
import os
from dev_to.api import users

from flask_pymongo import PyMongo

from dev_to.db import get_user
# load_dotenv()

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb+srv://devto:YOI7852j4JgvQmS9@cluster0.w8qa7p4.mongodb.net/devto?retryWrites=true&w=majority"
# mongo = PyMongo(app)
# db = mongo.db
app.register_blueprint(users.users_api_v1, url_prefix="/api/v1") 

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