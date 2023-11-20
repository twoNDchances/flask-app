from source import database, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_user):
    return User.query.get(id_user)


class User(database.Model, UserMixin):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(16))
    last_name = database.Column(database.String(64))
    username = database.Column(database.String(32), unique=True, index=True)
    gender = database.Column(database.String(8))
    career = database.Column(database.String(32))
    address = database.Column(database.String(128))
    email = database.Column(database.String(64), unique=True, index=True)
    phone = database.Column(database.String(16), unique=True, index=True)
    password = database.Column(database.String(512))
    key = database.Column(database.String(2048))
    book = database.relationship('Book', backref='user', lazy='dynamic')
    avatar = database.relationship('Avatar', backref='avatar', uselist=False)
    rule = database.relationship('Rule', backref='rules', uselist=False)

    def __init__(self, first_name, last_name, username, gender, address, career, email, phone, password, key):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.address = address
        self.career = career
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password=password)
        self.key = key


class Book(database.Model):
    __tablename__ = 'books'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(128))
    author = database.Column(database.String(128))
    release_year = database.Column(database.Integer)
    created_at = database.Column(database.DateTime)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    book = database.Column(database.String(512))
    image = database.relationship('Image', backref='image', uselist=False)
    key = database.Column(database.String(128))

    def __init__(self, title, author, release_year, created_at, book, user_id, key):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.created_at = created_at
        self.book = book
        self.user_id = user_id
        self.key = key


class Rule(database.Model):
    __tablename__ = 'rules'
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    phone_rule = database.Column(database.Boolean, default=False)
    email_rule = database.Column(database.Boolean, default=False)
    def __init__(self, user_id, phone_rule, email_rule):
        self.user_id = user_id
        self.phone_rule = phone_rule
        self.email_rule = email_rule


class Avatar(database.Model):
    __tablename__ = 'avatar'
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.String(512))
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))

    def __init__(self, image, user_id):
        self.image = image
        self.user_id = user_id


class Image(database.Model):
    __tablename__ = 'images'
    id = database.Column(database.Integer, primary_key=True)
    path = database.Column(database.String(512))
    book_id = database.Column(database.Integer, database.ForeignKey('books.id'))

    def __init__(self, path, book_id):
        self.path = path
        self.book_id = book_id
        