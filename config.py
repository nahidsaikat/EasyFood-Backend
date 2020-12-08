"""Flask config."""
from decouple import config


class Config:
    """Base config."""
    DEBUG = False
    TESTING = False
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = config('SECRET_KEY')
    SESSION_COOKIE_NAME = config('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
