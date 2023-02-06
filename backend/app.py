from routes import mainRoute
from flask import Flask, request, jsonify
app = Flask(__name__)
PORT =8080 

app.register_blueprint(mainRoute.bp, url_prefix="/api") 

@app.route('/')
def index():
    return 'Welcome to the CRUD APIs'
if __name__ == '__main__':
    app.run(port=PORT,debug=True) 