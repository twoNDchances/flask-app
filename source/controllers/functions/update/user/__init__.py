from flask import  Blueprint
from flask_login import login_required, current_user
from source.controllers.functions.update.user.function import _process_update


update_user = Blueprint(name='updateuser', import_name=__name__)


@update_user.route('/user', methods=['GET', 'POST'])
@login_required
def update_for_user():
    return _process_update()