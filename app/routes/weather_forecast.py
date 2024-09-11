from flask import Blueprint, request, jsonify
from app.models import WeatherForecast
from app import db

weather_forecast = Blueprint('weather_forecast', __name__)

@weather_forecast.route('/weather_forecast', methods=['GET'])
def get_weather_forecast():
    forecast = WeatherForecast.query.filter_by(date=date).first()
    if forecast:
        return jsonify(forecast.to_dict())
    else:
        return jsonify({"message": "Forecast not found"}), 202
