from datetime import datetime
from flask import redirect, render_template, session, url_for
from source.controllers.processor.crypto import _encrypt_string
from source.controllers.processor.queries import _query_object_user_by_username
from source.controllers.functions.search.form import SearchForm


def _process_library(page):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    
    user = _query_object_user_by_username(username=session['username'])
    is_empty = __process_is_empty(username=session['username'])
    return render_template(template_name_or_list='library.html', now=datetime, is_empty=is_empty, encrypt=_encrypt_string, encryption_key=user.key, form_search=form_search, books=user.book.paginate(page=page, per_page=3))


def _process_list():
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    user = _query_object_user_by_username(username=session['username'])
    is_empty = __process_is_empty(username=session['username'])
    return render_template(template_name_or_list='list.html', is_empty=is_empty, encrypt=_encrypt_string, encryption_key=user.key, form_search=form_search, books=user.book.all())


def __process_is_empty(username: str) -> bool:
    user = _query_object_user_by_username(username=username)
    books = user.book.all()
    if books.__len__() == 0:
        return True
    else:
        return False
