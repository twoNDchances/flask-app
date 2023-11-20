from os import remove
from flask import redirect, session, url_for
from source import database
from source.controllers.processor.crypto import _decrypt_string
from source.controllers.processor.queries import _query_object_book_by_key, _query_object_image_by_book_id, _query_object_user_by_username


def _process_delete_for_card(key):
    user = _query_object_user_by_username(username=session['username'])
    true_key = _decrypt_string(encrypted_string=key, key=user.key)[:-1]
    book = _query_object_book_by_key(key=true_key)
    image = _query_object_image_by_book_id(book_id=book.id)
    remove(path=book.book)
    remove(path=image.path)
    database.session.delete(image)
    database.session.delete(book)
    database.session.commit()
    return redirect(url_for('list.list.library', page=1))


def _process_delete_for_list(key):
    user = _query_object_user_by_username(username=session['username'])
    true_key = _decrypt_string(encrypted_string=key, key=user.key)[:-1]
    book = _query_object_book_by_key(key=true_key)
    image = _query_object_image_by_book_id(book_id=book.id)
    remove(path=book.book)
    remove(path=image.path)
    database.session.delete(image)
    database.session.delete(book)
    database.session.commit()
    return redirect(url_for('list.list.list'))


def _process_delete_for_search(key, keyword, filter, sort, show):
    user = _query_object_user_by_username(username=session['username'])
    true_key = _decrypt_string(encrypted_string=key, key=user.key)[1:-1]
    book = _query_object_book_by_key(key=true_key)
    remove(path=book.book)
    image = _query_object_image_by_book_id(book_id=book.id)
    remove(path=image.path)
    database.session.delete(book)
    database.session.delete(image)
    database.session.commit()
    return redirect(url_for('search.search_book.search', keyword=keyword, filter=filter, sort=sort, show=show))

