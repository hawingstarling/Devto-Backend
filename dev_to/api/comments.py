from datetime import datetime
from http import HTTPStatus
from flask import Blueprint, jsonify, make_response, request
from bson import json_util
from . import db, get_comment, get_comments, update_comment, delete_comment
from bson.objectid import ObjectId

comment_api_v1  = Blueprint('comments_api_v1', __name__)

@comment_api_v1.route('/')
def index():
    return 'api/v1 routes comments'

@comment_api_v1.route('/createComment', methods=['POST'])
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
    # Article match id pipeline
    pipeline = [
        {
            "$match": { 
                "_id": ObjectId(post_data.get('_idPost'))
             }
        }
    ]

    # Schema comment
    comments_schema = {
        'date': datetime.now(),
        'body': post_data.get('body'),
        'parent_post': ObjectId(post_data.get('_idPost')),
        'parent_id': ObjectId(post_data.get('_idParent')) if post_data.get('_idParent') != "" else "",
        'author': ObjectId(post_data.get('userId')),
        'isPositive': True,
        'likes': [],
        'replies': []
    }

    # Insert comments_schema to MongoDB
    commentId = db.comment.insert(comments_schema)

    if (post_data.get('_idParent') != ""):
        db.comment.find_one_and_update(
            { "_id": ObjectId(post_data.get('_idParent')) },
            { "$addToSet": { "replies": ObjectId(commentId) } },
            { "new": True }
        )

    return str(commentId)

@comment_api_v1.route('/getCommentById/<id>', methods=['GET'])
def getCommentById(id):
    comment = get_comment(id)
    if comment is None:
        return jsonify({
            'error': 'Not found'
        }), 400
    elif comment == {}:
        return jsonify({
            'error': 'Uncaught general exception'
        }), 400
    else: 
        return make_response(json_util.dumps({
            'comment': comment
        }), HTTPStatus.OK)

@comment_api_v1.route('/updateComment/<id>', methods=['PUT'])
def api_update_comment(id):
    # Receive request from a type json
    post_data = request.get_json()

    update_comment(id, post_data.get('body'))
    return {
        'status': 'successfull'
    }

@comment_api_v1.route('/deleteComment/<id>', methods=['DELETE'])
def api_delete_comment(id):
    delete_comment(id)
    return {
        'status': 'successfull'
    }
