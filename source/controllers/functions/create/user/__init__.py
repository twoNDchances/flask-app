from flask import Blueprint

from source.controllers.functions.create.user.function import _process_register

register_path = Blueprint(name='register', import_name=__name__)

@register_path.route('/register', methods=['GET', 'POST'])
def register():
    return _process_register()