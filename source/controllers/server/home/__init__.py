from flask import redirect, render_template, url_for, Blueprint
from source.controllers.functions.search.form import SearchForm
from source.controllers.server.home.function import _process_home, _process_main_root

home_path = Blueprint(name='home', import_name=__name__)


@home_path.route('/')
def main_root():
    return _process_main_root()


@home_path.route('/home', methods=['POST', 'GET'])
def home():
    return _process_home()
