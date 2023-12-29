# instance/production.py
class Config:
    SECRET_KEY = 'your_production_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
