''' we import app and db in this file. this file is use to create the db structure'''
from app import app, db
with app.app_context():
    db.create_all()
