from easy_food.core.views import core_bp
from easy_food.core.auth import auth_bp


def register_all_blueprints(app):
    app.register_blueprint(core_bp)
    app.register_blueprint(auth_bp)
