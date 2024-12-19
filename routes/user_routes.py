from flask import Blueprint, request, jsonify
from models.user import User
from db import db
from werkzeug.security import generate_password_hash
from middlewares import console_data

user_bp = Blueprint("user_bp", __name__)

# Crear usuario
@user_bp.route("/users", methods=["POST"])
@console_data
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"])
    new_user = User(name=data["name"], email=data["email"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!", "user": new_user.to_dict()}), 201

# Obtener todos los usuarios
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Obtener un usuario por ID
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200