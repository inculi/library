from dslib.views import (
    main,
    users
)

def register_views(flask_app):
    """ Attach the blueprints we have made to our flask application. """
    flask_app.register_blueprint(main.bp)
    flask_app.register_blueprint(users.bp)

    return flask_app