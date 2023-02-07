from routes import mainRoute
from flask import Flask, request, jsonify
# Import lib to load variable env 
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.register_blueprint(mainRoute.bp, url_prefix="/api") 

@app.route('/')
def index():
    return 'Welcome to the CRUD APIs'
if __name__ == '__main__':
    app.run(port=os.environ.get("APP_PORT"),debug=True) 