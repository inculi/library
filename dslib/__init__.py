import flask
import logging
import uuid

from dslib.extensions import assets
from dslib.views import register_views

def create_app(config):
    """ Sue app factory. """
    app = flask.Flask(__name__)
    app.config.from_object(config)

    # Debugging
    if app.config['DEBUG']:
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.WARNING)

    # Logging
    if 'LOG_FILE' in app.config:
        from logging.handlers import RotatingFileHandler
        app.log_handler = RotatingFileHandler(
            app.config['LOG_FILE'], maxBytes=10000, backupCount=1)
        app.logger.addHandler(app.log_handler)

    if not app.config['DEBUG']:
        @app.errorhandler(500)
        def internal_error(exception):
            random_id = uuid.uuid4()
            app.logger.error('Exception occurred. ID: %s' % random_id,
                             exc_info=exception)

    # Database
    # TODO: Add boilerplate code for setting up a database.

    assets.init_app(app)
    register_views(app)

    return app