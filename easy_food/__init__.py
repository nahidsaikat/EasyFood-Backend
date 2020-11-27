from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_assets import Environment

from easy_food.assets import compile_static_assets
from easy_food.urls import register_all_blueprints


csrf = CSRFProtect()
db = SQLAlchemy()
assets = Environment()


def create_app():
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder="templates",
                static_folder="static")
    if app.config['ENV'] == 'production':
        app.config.from_object('config.ProdConfig')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.DevConfig')

    csrf.init_app(app)
    db.init_app(app)
    assets.init_app(app)

    with app.app_context():
        register_all_blueprints(app)

        compile_static_assets(assets)
        return app
