from flask import Flask
from flask_sqlalchemy import SQLAlchemy


''' This is an entry point to the project'''
app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from app import routes, models


