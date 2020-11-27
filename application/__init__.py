from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from flask_assets import Environment


# Globally accessible libraries
csrf = CsrfProtect()
db = SQLAlchemy()
f_assets = Environment()


def create_app():
    """Initialize the core application."""
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
    print(f'The ENV is set to {app.config["ENV"]}')

    # Initialize Plugins
    csrf.init_app(app)
    db.init_app(app)
    f_assets.init_app(app)

    with app.app_context():
        from application.core.views import core_bp
        from application.assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(core_bp)

        compile_static_assets(f_assets)
        return app
