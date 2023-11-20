from flask import Blueprint

create = Blueprint(name='create', import_name=__name__, url_prefix='/create', static_folder='../../../static')

from source.controllers.functions.create.book import add_path

create.register_blueprint(blueprint=add_path)
