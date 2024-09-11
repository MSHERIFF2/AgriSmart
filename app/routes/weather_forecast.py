from flask import Blueprint, request, jsonify
from app.models import WeatherForecast
from app import db
from datetime import date

query_date = date(2024, 9, 11)

weather_forecast = Blueprint('weather_forecast', __name__)

@weather_forecast.route('/weather_forecast', methods=['GET'])
def get_weather_forecast():
    forecast = WeatherForecast.query.filter_by(date=query_date).first()
    if forecast:
        return jsonify(forecast.to_dict())
    else:
        return jsonify({"message": "Forecast not found"}), 202
