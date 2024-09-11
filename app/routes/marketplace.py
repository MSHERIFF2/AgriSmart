from flask import Blueprint, request, jsonify
from app.models import Listing
from app import db

marketplace = Blueprint('marketplace', __name__)

@marketplace.route('/marketplace', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    return jsonify([list.to_dict() for listing in listings])

@marketplace.route('/marketplace', methods=['POST'])
def create_listing():
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
    return jsonify(new_listing.to_dict()), 201
