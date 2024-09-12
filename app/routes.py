from app import app
from flask import render_template, request, redirect, url_for
from app.models import Crop, Livestock, MarketPrice, FarmingTip, WeatherForecast

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crops')
def show_crops():
    crops = Crop.query.all()
    marketprice = MarketPrice.query.all()
    crop_prices = {price.crop_id: price.price for price in marketprice}
    return render_template('crops.html', crops=crops, crop_prices=crop_prices)

@app.route('/livestock')
def show_livestock():
    livestocks = Livestock.query.all()
    marketprice = MarketPrice.query.all()
    livestock_prices = {price.livestock_id: price.price for price in marketprice}
    return render_template('livestock.html', livestocks=livestocks, livestock_prices=livestock_prices)


@app.route('/farming-tips')
def show_farming_tips():
    tips = FarmingTip.query.order_by(FarmingTip.date.desc()).all()
    return render_template('farming_tips.html', tips=tips)

@app.route('/weather-forecast')
def show_weather_forecast():
    forecasts = WeatherForecast.query.order_by(WeatherForecast.forecast_date.desc()).all()
    return render_template('weather_forecast.html', forecasts=forecasts)
