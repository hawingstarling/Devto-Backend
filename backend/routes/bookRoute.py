from flask import Blueprint

bookbp = Blueprint('book', __name__)


@bookbp.route('/', methods=['POST'])
def index():
    return "Book api"
