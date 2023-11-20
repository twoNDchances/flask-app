from flask import Blueprint, request
from flask_login import login_required
from source.controllers.functions.visit.book.function import _process_visit_book
from source.controllers.processor.queries import _query_object_user_by_query


visit_book = Blueprint(name='book', import_name=__name__)


@visit_book.route('/book', methods=['POST', 'GET'])
@login_required
def visitbook():
    get_username = request.args.get('username')
    get_key = request.args.get('key')
    if get_username not in [user.username for user in _query_object_user_by_query()]:
        return 'Not found'
    else:
        return _process_visit_book(username=get_username, key=get_key)
