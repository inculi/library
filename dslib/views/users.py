import flask

from dslib.models import User

app = flask.current_app
bp = flask.Blueprint('users', __name__)

@bp.route('/user/<username>')
def greet_user(username):
    currentUser = User(username)

    # 'Hello, %s!' % self.username
    return currentUser.greeting()