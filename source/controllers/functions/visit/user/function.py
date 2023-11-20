from datetime import datetime
from flask import redirect, render_template, url_for
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.crypto import _encrypt_string
from source.controllers.processor.queries import _query_object_user_by_username, _query_all_book_by_username, _query_object_user_by_id

def _process_visit_user(username, show):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        get_keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=get_keyword, filter='title', sort='increase', show='card'))
    user = _query_object_user_by_username(username=username)
    books = _query_all_book_by_username(username=username)
    number_of_books, status = __process_book_status(username=username)
    return render_template(template_name_or_list='visit_user.html', form_search=form_search, user=user, show=show, now=datetime, books=books, number=number_of_books, status=status, encrypt=_encrypt_string)

def __process_book_status(username):
    books = _query_all_book_by_username(username=username)
    if books.__len__() > 1:
        return books.__len__(), 'books'
    else:
        return books.__len__(), 'book'
