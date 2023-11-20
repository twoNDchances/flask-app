from flask import Blueprint
from source.controllers.functions.search.book import search_book
from source.controllers.functions.search.user import search_user


search = Blueprint(name='search', import_name=__name__, url_prefix='/search', static_folder='../../../static')


search.register_blueprint(blueprint=search_book)
search.register_blueprint(blueprint=search_user)