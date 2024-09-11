from flask import Blueprint, request, jsonify, session
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], methods='sha256')
    new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            location=data.get('location', '')
            )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"mesage": "User registered successfully"}), 201

@auth.route('/auth/login', methods=['GET'])
def login():
    data=request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@auth.route('/auth/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"})

