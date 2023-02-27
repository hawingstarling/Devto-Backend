from datetime import datetime
from http import HTTPStatus
from flask import Blueprint, jsonify, make_response, request
from bson import json_util
from . import db

comment_api_v1  = Blueprint('comments_api_v1', __name__)

@comment_api_v1.route('/')
def index():
    return 'api/v1 routes comments'

@comment_api_v1.route('/comments', methods=['POST'])
def api_comments():
    """
    - Posts a comment about a article.
    - This endpoint allows the client to retrieve all comments belonging 
    to an article or podcast episode as threaded conversations.
    - It will return the all top level comments with their nested comments 
    as threads. See the format specification for further details.
    """

    # Receive request from a type json
    post_data = request.get_json()

    # Schema comment
    comments_schema = {
        'created_at': datetime.now(),
        'body_html': post_data.get('body_html'),
        'parent_post': {},
        'parent_id': {},
        'author': {},
        'likes': {}
    }

    # Insert comments_schema to MongoDB
    db.comment.insert_one(comments_schema)
    return make_response(json_util.dumps({
        'comment': comments_schema
    }), HTTPStatus.OK)

