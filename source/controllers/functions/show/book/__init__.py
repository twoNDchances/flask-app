from flask import Blueprint
from flask_login import login_required
from source.controllers.functions.show.book.function import _process_view


view_path = Blueprint(name='showbook', import_name=__name__)


@view_path.route('/book/<key>', methods=['POST', 'GET'])
@login_required
def view(key):
    return _process_view(key)
