from flask import Blueprint

visit = Blueprint(name='visit', import_name=__name__, url_prefix='/visit', static_folder='../../../static')

from source.controllers.functions.visit.book import visit_book
from source.controllers.functions.visit.user import visit_user

visit.register_blueprint(blueprint=visit_book)
visit.register_blueprint(blueprint=visit_user)
