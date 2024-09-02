from flask import Flask
from .routes import main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

    app.register_blueprint(main_routes)

    return app
