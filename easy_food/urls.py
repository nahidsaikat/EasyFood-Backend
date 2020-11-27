from easy_food.core.views import core_bp


def register_all_blueprints(app):
    app.register_blueprint(core_bp)
