from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Register Blueprints

        return app
