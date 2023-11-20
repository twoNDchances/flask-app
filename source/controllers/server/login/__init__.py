from flask import Blueprint

from source.controllers.server.login.function import _process_login

login_path = Blueprint(name='login', import_name=__name__, static_folder='../../../static')

@login_path.route('/login', methods=['GET', 'POST'])
def login():
    return _process_login()
