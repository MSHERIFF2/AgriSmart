from flask import Blueprint, jsonify, session
from app.models import MarketPrice, WeatherForecast, FarmingTips
from app import db

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
    market_prices = MarketPrice.query.limit(5).all()
    weather_forecast = WeatherForecast.query.order_by(WeatherForecast.date.desc()).first()

    return jsonify({
        "market_prices": [price.to_dict() for price in market_prices],
        "weather_forecast": weather_forecast.to_dict() if weather_fore else {},
        "farming_tips": [tip.to_dict() for tip in farming_tips]
        })
