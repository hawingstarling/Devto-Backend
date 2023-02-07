from flask_mysqldb import MySQL
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os

load_dotenv()
app = Flask(__name__)
mysqlVal = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database_name'
app.config['MYSQL_DATABASE_HOST'] = 'host'
mysqlVal.init_app(app)