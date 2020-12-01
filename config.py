"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
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
