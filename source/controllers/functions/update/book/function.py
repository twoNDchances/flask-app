from datetime import datetime
from flask import redirect, render_template, session, url_for
from source import database
from source.controllers.functions.update.book.form import UpdateBookForm
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.crypto import _decrypt_string
from source.controllers.processor.queries import _query_object_book_by_key, _query_object_user_by_username
from source.datatable import Book


def _process_update_book(key, keyword, filter, sort, show):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        get_keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=get_keyword, filter='title', sort='increase', show='card'))
    form = UpdateBookForm()
    get_title, get_author, get_release_year = form.title.data, form.author.data, form.release_year.data
    user = _query_object_user_by_username(username=session['username'])
    true_key = _decrypt_string(encrypted_string=key, key=user.key)
    if true_key != False:
        book = _query_object_book_by_key(key=true_key)
        if form.validate_on_submit():
            if get_title != '':
                __process_update_book_categorize(categorize='title', new_data=get_title, object_book=book)
            if get_author != '':
                __process_update_book_categorize(categorize='author', new_data=get_author, object_book=book)
            if get_release_year != None:
                __process_update_book_categorize(categorize='release_year', new_data=int(get_release_year), object_book=book)
            if (keyword and filter and sort and show) is not None:
                return redirect(url_for('search.search_book.search', keyword=keyword, filter=filter, sort=sort, show=show))
            else:
                return redirect(url_for('list.list.library', page=1))
        return render_template(template_name_or_list='update_book.html', form=form, book=book, form_search=form_search)
    else:
        return 'Not found!'


def __process_update_book_categorize(categorize: str, new_data, object_book: Book):
    if categorize == 'title':
        object_book.title = new_data
    elif categorize == 'author':
        object_book.author = new_data
    elif categorize == 'release_year':
        object_book.release_year = new_data
    object_book.created_at = datetime.now()
    database.session.add(object_book)
    database.session.commit()
