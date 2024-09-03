from flask import Flask
from .routes import main_routes
from flask_login import LoginManager
from app.models import db, User
from config import Config
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main_routes)
    return app
