from flask import Blueprint

delete = Blueprint(name='delete', import_name=__name__, url_prefix='/delete', static_folder='../../../static')

from source.controllers.functions.delete.book import delete_path

delete.register_blueprint(delete_path)
