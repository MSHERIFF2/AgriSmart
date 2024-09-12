from flask import Blueprint, request, jsonify, session
from app.models import Listing
from app import db

marketplace = Blueprint('marketplace', __name__)

@marketplace.route('/marketplace', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    results = [{
        "id": listing.id,
        "user_id": listing.user_id,
        "item_name": listing.item_name,
        "price": listing.price,
        "description": listing.description,
        "location": listing.location,
        "image_url": listing.image_url,
        "created_at": listing.created_at
        } for listing in listings]
    return jsonify(results)

@marketplace.route('/marketplace', methods=['POST'])
def create_listing():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
    
    data = request.get_json()
    new_listing = Listing(
            user_id =data['user_id'],
            item_name=data['item_name'],
            price=data['price'],
            description=data['description'],
            location=data['location'],
            image_url=data.get('image_url', '')
            )
    db.session.add(new_listing)
    db.session.commit()
    return jsonify({"message": "Listing created successfully"}), 201
