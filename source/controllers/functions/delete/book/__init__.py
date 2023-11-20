from flask import Blueprint, request
from flask_login import login_required
from source.controllers.functions.delete.book.function import _process_delete_for_card, _process_delete_for_list, _process_delete_for_search


delete_path = Blueprint(name='delete', import_name=__name__)


@delete_path.route('/card/<key>')
@login_required
def delete_card(key):
    get_keyword = request.args.get('keyword')
    get_filter = request.args.get('filter')
    get_sort = request.args.get('sort')
    get_show = request.args.get('show')
    if (get_keyword and get_filter and get_sort and get_show) is not None:
        return _process_delete_for_search(key=key, keyword=get_keyword, filter=get_filter, sort=get_sort, show=get_show)
    else:
        return _process_delete_for_card(key)


@delete_path.route('/list/<key>')
@login_required
def delete_list(key):
    get_keyword = request.args.get('keyword')
    get_filter = request.args.get('filter')
    get_sort = request.args.get('sort')
    get_show = request.args.get('show')
    if (get_keyword and get_filter and get_sort and get_show) is not None:
        return _process_delete_for_search(key=key, keyword=get_keyword, filter=get_filter, sort=get_sort, show=get_show)
    else:
        return _process_delete_for_list(key)

