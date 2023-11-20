from flask import Blueprint

list = Blueprint(name='list', import_name=__name__, url_prefix='/list', static_folder='../../../static')

from source.controllers.functions.list.book import list_path

list.register_blueprint(list_path)
