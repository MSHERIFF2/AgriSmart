from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_session import Session

#initialize extensions
db = SQLAlchemy()
migrate = Migrate()
session = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    app.config['SESSION_SQLALCHEMY'] = db
    session.init_app(app)

    #Register Blueprints
    from app.routes.market_prices import market_prices
    from app.routes.weather_forecast import weather_forecast
    from app.routes.farming_tips import farming_tips
    from app.routes.auth import auth
    from app.routes.user import user
    from app.routes.marketplace import marketplace
    from app.routes.dashboard import dashboard

    app.register_blueprint(market_prices)
    app.register_blueprint(weather_forecast)
    app.register_blueprint(farming_tips)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(marketplace)
    app.register_blueprint(dashboard)

    return app
