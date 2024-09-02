from flask import Flask
from .routes import main_routes
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

   db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    app.register_blueprint(main_routes)
    return app
