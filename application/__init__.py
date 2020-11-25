from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect


# Globally accessible libraries
csrf = CsrfProtect()
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder="templates",
                static_folder="static")
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        from .core import routes
        # Register Blueprints

        return app
