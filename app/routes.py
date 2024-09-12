from flask import Flask, render_template, redirect, url_for, session
from app.models import MarketPrice, WeatherForecast, FarmingTip, User, Listing

app = Flask(__name__)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the market prices feature
@app.route('/market_prices')
def market_prices():
    prices = MarketPrice.query.all()
    return render_template('market_prices.html', prices=prices)

# Route for the weather forecast feature
@app.route('/weather_forecast')
def weather_forecast():
    forecasts = WeatherForecast.query.all()
    return render_template('weather_forecast.html', forecasts=forecasts)

# Route for the farming tips feature
@app.route('/farming_tips')
def farming_tips():
    tips = FarmingTip.query.all()
    return render_template('farming_tips.html', tips=tips)

# Route for the user profile
@app.route('/users/profile')
def user_profile():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))

# Route for the marketplace
@app.route('/marketplace')
def marketplace():
    listings = Listing.query.all()
    return render_template('marketplace.html', listings=listings)

# Route for the dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        # Compile data specific to the user, e.g., their listings, tips, etc.
        user_data = {
            "listings": Listing.query.filter_by(user_id=user.id).all(),
            # Add other user-specific data here as needed
        }
        return render_template('dashboard.html', user=user, data=user_data)
    return redirect(url_for('login'))

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')
