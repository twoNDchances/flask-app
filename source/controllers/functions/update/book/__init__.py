from flask import Blueprint, request
from flask_login import login_required
from source.controllers.functions.update.book.function import _process_update_book


update_book = Blueprint(name='updatebook', import_name=__name__)


@update_book.route('/book/<key>', methods=['GET', 'POST'])
@login_required
def update_for_book(key):
    get_keyword = request.args.get('keyword')
    get_filter = request.args.get('filter')
    get_sort = request.args.get('sort')
    get_show = request.args.get('show')
    return _process_update_book(key=key, keyword=get_keyword, filter=get_filter, sort=get_sort, show=get_show)
