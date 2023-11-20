from flask import Blueprint, request, abort
from flask_login import login_required
from source.controllers.functions.list.book.function import _process_library, _process_list

list_path = Blueprint(name='list', import_name=__name__)

@list_path.route('/cards', methods=['POST', 'GET'])
@login_required
def library():
    get_page = request.args.get(key='page', type=int)
    if get_page:
        return _process_library(page=get_page)
    else:
        return abort(404)

@list_path.route('/table', methods=['POST', 'GET'])
@login_required
def list():
    return _process_list()
