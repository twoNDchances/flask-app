from flask import Blueprint

update = Blueprint(name='update', import_name=__name__, url_prefix='/update', static_folder='../../../static')

from source.controllers.functions.update.book import update_book
from source.controllers.functions.update.user import update_user

update.register_blueprint(update_book)
update.register_blueprint(update_user)