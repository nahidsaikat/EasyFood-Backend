"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets.auto_build = True
    assets.debug = False
    # common_less_bundle = Bundle(
    #     'src/less/*.less',
    #     filters='less,cssmin',
    #     output='dist/css/style.css',
    #     extra={'rel': 'stylesheet/less'}
    # )
    # core_less_bundle = Bundle(
    #     'home_bp/less/home.less',
    #     filters='less,cssmin',
    #     output='dist/css/core.css',
    #     extra={'rel': 'stylesheet/less'}
    # )
    # assets.register('common_less_bundle', common_less_bundle)
    # assets.register('core_less_bundle', core_less_bundle)
    # if app.config['FLASK_ENV'] == 'development':
    #     common_less_bundle.build()
    #     core_less_bundle.build()
    return assets
