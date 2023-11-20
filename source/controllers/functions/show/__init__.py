from flask import Blueprint

show = Blueprint(name='show', import_name=__name__, url_prefix='/view', static_folder='../../../static')

from source.controllers.functions.show.book import view_path
from source.controllers.functions.show.user import show_path

show.register_blueprint(view_path)
show.register_blueprint(show_path)
