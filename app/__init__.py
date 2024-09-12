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
    
    return app
