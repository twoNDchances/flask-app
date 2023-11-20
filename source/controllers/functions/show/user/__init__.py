from flask import Blueprint
from flask_login import login_required, current_user
from source.controllers.functions.show.user.function import _process_profile


show_path = Blueprint(name='showuser', import_name=__name__)


@show_path.route('/profile/<username>', methods=['POST', 'GET'])
@login_required
def profile(username):
    if current_user.username == username:
        return _process_profile(username)
    else:
        return '<h1>Not found!</h1>'
