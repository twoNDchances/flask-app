from flask import Blueprint
from flask_login import login_required
from source.controllers.functions.create.book.function import _process_add


add_path = Blueprint(name='add', import_name=__name__)


@add_path.route('/book', methods=['GET', 'POST'])
@login_required
def add():
    return _process_add()
