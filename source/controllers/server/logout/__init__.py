from flask import Blueprint
from flask_login import login_required
from source.controllers.server.logout.function import _process_logout

logout_path = Blueprint(name='logout', import_name=__name__)

@logout_path.route('/logout')
@login_required
def logout():
    return _process_logout()
