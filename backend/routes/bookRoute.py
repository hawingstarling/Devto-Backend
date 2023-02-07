from flask import Blueprint,request

bookbp = Blueprint('book', __name__)


@bookbp.route('/getall', methods=['GET'])
def index():
    return "Book api"

@bookbp.route("/insert_new_book", methods=['POST'])
def insertNew():
    return "Insert New book"
