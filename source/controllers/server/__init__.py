from flask import Blueprint

system = Blueprint(name='system', import_name=__name__, static_folder='../../../static')

from source.controllers.server.home import home_path
from source.controllers.server.login import login_path
from source.controllers.server.logout import logout_path
from source.controllers.server.errors import errors


system.register_blueprint(blueprint=home_path)
system.register_blueprint(blueprint=login_path)
system.register_blueprint(blueprint=logout_path)
system.register_blueprint(blueprint=errors)