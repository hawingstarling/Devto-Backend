from routes import bookRoute

from flask import Blueprint
bp = Blueprint('api', __name__)



bp.register_blueprint(bookRoute.bookbp,url_prefix="/book")
