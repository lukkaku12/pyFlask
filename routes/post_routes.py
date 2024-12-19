from flask import Blueprint, jsonify, request
from db import db
from models import Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.get('/post/<int:user_id>')
def get_posts(userId):
    posts = Post.query.filter_by(user_id=userId).all()
    return jsonify([post.to_dict() for post in posts]), 200

@post_bp.post('/post/<int:user_id>')
def create_post(userId):
    postData = request.get_json()
    post = Post(title=postData['title'], content=postData['content'], user_id=userId)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@post_bp.delete('/post/<int:post_id>')
def delete_post(postId):
    post = Post.query.get_or_404(postId)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"}), 204