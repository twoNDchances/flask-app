from flask import Blueprint, request, abort
from flask_login import login_required
from source.controllers.functions.visit.user.function import _process_visit_user
from source.controllers.processor.queries import _query_object_user_by_query

visit_user = Blueprint(name='user', import_name=__name__)

@visit_user.route('/user/<username>', methods=['POST', 'GET'])
@login_required
def visituser(username):
    get_show = request.args.get('show')
    if get_show not in ['card', 'library', 'table', 'list']:
        abort(404)
    elif username not in [user.username for user in _query_object_user_by_query()]:
        abort(404)
    else:
        return _process_visit_user(username=username, show=get_show)