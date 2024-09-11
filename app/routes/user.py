from flask import Blueprint, request, jsonify
from app.models import User
from app import db

user = Blueprint('user', __name__)

@user.route('/users/<int:id>', methods=['GET'])
def get_user_profile(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@user.route('/users/<int:id>', methods=['PUT'])
def update_user_profile(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email =data.get('email', user.email)
    user.location = data.get('location', user.location)
    db.session.commit()
    return jsonify(user.to_dict())
