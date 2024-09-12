from flask import Blueprint, request, jsonify
from app.models import MarketPrice
from app import db
from app.auth.utils import admin_required

market_prices = Blueprint('market_prices', __name__)

@market_prices.route('/market_prices', methods=['GET'])
def get_market_prices():
    prices = MarketPrice.query.all()
    return jsonify([price.to_dict() for price in prices]), 200

@market_prices.route('/market_prices/<int:id>', methods=['POST'])
def get_market_price(id):
    price = MarketPrice.query.get_or_404(id)
    return jsonify(price.to_dict()), 200

@market_prices.route('/market_prices', methods=['POST'])
@admin_required
def create_market_price():
    data = request.get_json()
    #Add data validation and admin check

    new_price = MarketPrice(
            item_name=data['item_name'],
            price=data['price'],
            unit=data['unit'],
            location=data['location']
            )
    db.session.add(new_price)
    db.session.commit()
    return jsonify(new_price.to_dict()), 201
