from flask import redirect, render_template, session, url_for
from source.controllers.processor.crypto import _decrypt_string
from source.controllers.processor.queries import _query_object_book_by_key, _query_object_user_by_username
from source.controllers.functions.search.form import SearchForm


def _process_view(key):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    user = _query_object_user_by_username(username=session['username'])
    true_key = _decrypt_string(encrypted_string=key, key=user.key)
    if true_key != False:
        book = _query_object_book_by_key(key=true_key)
        return render_template(template_name_or_list='show.html', book=book, form_search=form_search)
    else:
        return 'Not found'
