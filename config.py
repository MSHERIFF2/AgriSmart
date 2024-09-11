import os

class Config:
    #Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///agrismart.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    #secret key for session management and other security related operations
    SECRET_KEY = os.environ.get('SECRET_KEY', 'M08170205738$s')

    #session configuration
    SESSION_TYPE = 'sqlalchemy'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True


