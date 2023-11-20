from source.datatable import User, Avatar, Book, Image
from werkzeug.security import check_password_hash


def _query_user_id_by_username(username: str) -> int:
    """
    :param username:
    :return: an integer of user by username
    """
    return _query_object_user_by_username(username=username).id


def _query_object_user_by_id(id: int) -> User:
    """
    :param id: an id of an object user
    :return: an object user
    """
    user_id = User.query.get(id)
    return user_id


def _query_object_user_by_username(username: str) -> User:
    """
    :param username:
    :return: an object user with username
    """
    user = User.query.filter_by(username=username)
    return user.first()


def _query_object_user_by_email(email: str) -> User:
    """
    :param email:
    :return: an object user with email
    """
    user = User.query.filter_by(email=email)
    return user.first()


def _query_object_user_by_phone(phone: str) -> User:
    """
    :param phone:
    :return: an object user with phone
    """
    user = User.query.filter_by(phone=phone)
    return user.first()


def _check_login(username: str, password: str) -> bool:
    """
    :param username: username by user input
    :param password: password by user input
    :return: True if password input by user match with password hashed in database
    """
    query_hashed_password = _query_object_user_by_username(username=username).password
    return check_password_hash(password=password, pwhash=query_hashed_password)


def _query_object_avatar_by_id(id: int) -> Avatar:
    """
    :param id: an id of an object avatar
    :return: an object avatar
    """
    avatar_id = Avatar.query.get(id)
    return avatar_id


def _query_avatar_id_by_user_id(user_id: int) -> int:
    """
    :param user_id: an id of an object user
    :return: an id of an object avatar
    """
    avatar_id = Avatar.query.filter_by(user_id=user_id)
    return avatar_id.first().id


def _query_avatar_path_by_user_id(user_id: int) -> str:
    """
    :param user_id: an id of an object user
    :return: a string path where avatar is stored
    """
    avatar_path = Avatar.query.filter_by(user_id=user_id)
    return avatar_path.first().image


def _query_object_book_by_query() -> list:
    return Book.query.all()


def _query_object_book_by_key(key) -> Book:
    """
    :param key: a key of object book
    return: a object book
    """
    book = Book.query.filter_by(key=key)
    return book.first()


def _query_object_image_by_book_id(book_id) -> Image:
    """
    :param book_id: an id of book
    return: a object image of book
    """
    image = Image.query.filter_by(book_id=book_id)
    return image.first()


def _query_all_book_by_username(username):
   '''
   :param username: username of user
   return: all of books of the specific user
   '''
   return _query_object_user_by_username(username=username).book.all()


def _query_object_user_by_query() -> list:
    return User.query.all()


def _query_object_users_with_keyword(keyword: str, category: str, sort: str) -> list:
    if sort in ['increase', 'asc']:
        if category == 'username':
            return User.query.filter(User.username.like('%' + keyword + '%')).order_by(User.username.asc()).all()
        if category in ['first_name', 'firstname', 'first name']:
            return User.query.filter(User.first_name.like('%' + keyword + '%')).order_by(User.first_name.asc()).all()
        if category in ['last_name', 'lastname', 'last name']:
            return User.query.filter(User.last_name.like('%' + keyword + '%')).order_by(User.last_name.asc()).all()
        if category == 'phone':
            if User.query.filter_by(phone=keyword).first() is not None:
                if User.query.filter_by(phone=keyword).first().rule.phone_rule:
                    return User.query.filter_by(phone=keyword).all()
                else:
                    return []
            else:
                return []
        if category == 'email':
            if User.query.filter_by(email=keyword).first() is not None:
                if User.query.filter_by(email=keyword).first().rule.phone_rule:
                    return User.query.filter_by(email=keyword).all()
                else:
                    return []
            else:
                return []
        if category == 'address':
            return User.query.filter(User.address.like('%' + keyword + '%')).order_by(User.address.asc()).all()
        if category == 'career':
            return User.query.filter(User.career.like('%' + keyword + '%')).order_by(User.career.asc()).all()
    elif sort in ['decrease', 'desc']:
        if category == 'username':
            return User.query.filter(User.username.like('%' + keyword + '%')).order_by(User.username.desc()).all()
        if category in ['first_name', 'firstname', 'first name']:
            return User.query.filter(User.first_name.like('%' + keyword + '%')).order_by(User.first_name.desc()).all()
        if category in ['last_name', 'lastname', 'last name']:
            return User.query.filter(User.last_name.like('%' + keyword + '%')).order_by(User.last_name.desc()).all()
        if category == 'phone':
            return User.query.filter_by(phone=keyword).all()
        if category == 'email':
            return User.query.filter_by(email=keyword).all()
        if category == 'address':
            return User.query.filter(User.address.like('%' + keyword + '%')).order_by(User.address.desc()).all()
        if category == 'career':
            return User.query.filter(User.career.like('%' + keyword + '%')).order_by(User.career.desc()).all()


def _query_object_books_with_keyword(keyword: str, category: str, sort: str) -> list:
    if sort in ['increase', 'asc']:
        if category == 'title':
            return Book.query.filter(Book.title.like('%' + keyword + '%')).order_by(Book.title.asc()).all()
        if category == 'author':
            return Book.query.filter(Book.author.like('%' + keyword + '%')).order_by(Book.author.asc()).all()
        if category in ['release_year', 'releaseyear', 'release year']:
            return Book.query.filter(Book.release_year.like('%' + keyword + '%')).order_by(Book.release_year.asc()).all()
    elif sort in ['decrease', 'desc']:
        if category == 'title':
            return Book.query.filter(Book.title.like('%' + keyword + '%')).order_by(Book.title.desc()).all()
        if category == 'author':
            return Book.query.filter(Book.author.like('%' + keyword + '%')).order_by(Book.author.desc()).all()
        if category in ['release_year', 'releaseyear', 'release year']:
            return Book.query.filter(Book.release_year.like('%' + keyword + '%')).order_by(Book.release_year.desc()).all()