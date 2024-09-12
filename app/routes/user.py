from flask import Blueprint, request, jsonify, session
from app.models import User
from app import db

user = Blueprint('user', __name__)

@user.route('/users/', methods=['GET'])
def get_user_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "unauthorized"}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "location": user.location,
        "created_at": user.created_at
        })

@user.route('/users/', methods=['PUT'])
def update_user_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email =data.get('email', user.email)
    user.location = data.get('location', user.location)
    db.session.commit()
    return jsonify({"message": "User profile updated successfully"})
