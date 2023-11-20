from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from os import path
from source.controllers.processor.crypto import generate_secret_key_1024


#   application creation
application = Flask(__name__)
application.config['SECRET_KEY'] = generate_secret_key_1024()
#   database creation
application.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'data.sql'))
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(application)
Migrate(application, database)

#   login creation
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'system.login.login'

# from main.controls.object.book import book
# from main.controls.object.user import user
# from main.controls.server import home_path

# application.register_blueprint(blueprint=book, url_prefix='/book')
# application.register_blueprint(blueprint=user, url_prefix='/user')
# application.register_blueprint(blueprint=home_path)


from source.controllers.server import system
from source.controllers.functions.create import create
from source.controllers.functions.create.user import register_path
from source.controllers.functions.delete import delete
from source.controllers.functions.list import list
from source.controllers.functions.show import show
# from source.controllers.functions.show.user import show_path
from source.controllers.functions.update import update
from source.controllers.functions.search import search
from source.controllers.functions.visit import visit


application.register_blueprint(blueprint=system)
application.register_blueprint(blueprint=create)
application.register_blueprint(blueprint=register_path)
application.register_blueprint(blueprint=delete)
application.register_blueprint(blueprint=list)
application.register_blueprint(blueprint=show)
# application.register_blueprint(blueprint=show_path)
application.register_blueprint(blueprint=update)
application.register_blueprint(blueprint=search)
application.register_blueprint(blueprint=visit)

