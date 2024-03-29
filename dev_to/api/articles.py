from datetime import datetime
from http import HTTPStatus
from flask import Blueprint, jsonify, make_response, request
from . import db, get_acticles, get_article, update_article, delete_article
from bson import json_util
from bson.objectid import ObjectId
from .utils.obj_dict import obj_dict

articles_api_v1 = Blueprint("articles_api_v1", __name__)

@articles_api_v1.route("/")
def index():
    return "api/v1 routes articles"

@articles_api_v1.route("/createArticle", methods=['POST'])
def api_articles():
    post_article = request.get_json()
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(post_article.get('userId'))
            }
        }
    ]
    article_schema = {
        "title": post_article.get('title'),
        "published": True,
        "body": post_article.get('body'),
        "comments_count": 0,
        "likes": [],
        "bookmarks": [],
        "created_at": datetime.now(),
        "edited_at": None,
        "cover_image": post_article.get('cover_image'),
        "user": db.user.aggregate(pipeline).next(),
    }
    db.article.insert_one(article_schema)
    return make_response(json_util.dumps({
        'articles': article_schema
    }), HTTPStatus.OK)

@articles_api_v1.route('/getAllArticles', methods=['GET'])
def get_articles():
    return make_response(json_util.dumps({
        'articles': get_acticles()
    }, default=obj_dict), HTTPStatus.OK)

@articles_api_v1.route('/getArticle/<id>', methods=['GET'])
def get_article(id):
    article = get_article(id)
    if article is None:
        return jsonify({
            'error': 'Not found'
        }), 400
    elif article == {}:
        return jsonify({
            'error': 'Uncaught general exception'
        }), 400
    else: 
        return make_response(json_util.dumps({
            'article': article
        }), HTTPStatus.OK)

@articles_api_v1.route('/updateArticle/<id>', methods=['PUT'])
def api_update_article(id):
    post_data = request.get_json()

    update_article(id, post_data.get('title'), post_data.get('body'), post_data.get('cover_image'), datetime.now())
    return {
        'status': 'successfull'
    }

@articles_api_v1.route('/deleteArticle/<id>', methods=['DELETE'])
def api_delete_article(id):
    delete_article(id)
    return {
        'status': 'successfull'
    }

@articles_api_v1.route('/likeArticle/<id>', methods=['PUT'])
def likeArticle(id):
    post_data = request.json()
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(post_data.get('userId'))
            }
        }
    ]
    db.article.find_one_and_update(
        { "_id": ObjectId(id) },
        { "$addToSet": { "likes": db.user.aggregate(pipeline).next() } },
        { "new": True }
    )
    return "ok"

@articles_api_v1.route('/unlikeArticle/<id>', methods=['PUT'])
def unlikeArticle(id):
    post_data = request.json()
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(post_data.get('userId'))
            }
        }
    ]
    db.article.find_one_and_update(
        { "_id": ObjectId(id) },
        { "$pull": { "likes": db.user.aggregate(pipeline).next() } },
        { "new": True }
    )
    return "ok"

@articles_api_v1.route('/bookmarkArticle/<id>', methods=['PUT'])
def bookmarkArticle(id):
    post_data = request.json()
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(post_data.get('userId'))
            }
        }
    ]
    db.article.find_one_and_update(
        { "_id": ObjectId(id) },
        { "$addToSet": { "bookmarks": db.user.aggregate(pipeline).next() } },
        { "new": True }
    )
    return "ok"

@articles_api_v1.route('/unbookmarkArticle/<id>', methods=['PUT'])
def unbookmarkArticle(id):
    post_data = request.json()
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(post_data.get('userId'))
            }
        }
    ]
    db.article.find_one_and_update(
        { "_id": ObjectId(id) },
        { "$pull": { "bookmarks": db.user.aggregate(pipeline).next() } },
        { "new": True }
    )
    return "ok"

@articles_api_v1.route('/getBookmark', methods=['GET'])
def getBookmark(userId):

    articlesBookmark = db.article.find({ "bookmarks": userId })
    return make_response(json_util.dumps({
        'articlesBookmark': articlesBookmark
    }), HTTPStatus.OK)
