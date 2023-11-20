from datetime import datetime
from flask import render_template, redirect, url_for
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.crypto import _decrypt_string
from source.controllers.processor.queries import _query_object_user_by_username, _query_object_book_by_key, _query_object_user_by_id


def _process_visit_book(username, key):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        get_keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=get_keyword, filter='title', sort='increase', show='card'))
    true_key = _decrypt_string(encrypted_string=key, key=_query_object_user_by_username(username=username).key)
    if true_key != False:
        book = _query_object_book_by_key(key=true_key)
        return render_template(template_name_or_list='visit_book.html', form_search=form_search, book=book, now=datetime, user=_query_object_user_by_id)
    else:
        return 'Not found'
