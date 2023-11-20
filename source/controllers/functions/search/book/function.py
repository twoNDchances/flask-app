from datetime import datetime
from flask import redirect, render_template, url_for, session
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.crypto import _encrypt_string
from source.controllers.processor.queries import _query_object_user_by_id, _query_object_books_with_keyword, _query_object_user_by_username

def _process_search_book(keyword, filter, sort, show):
    self_found = []
    other_found = []
    self_encryption_key = _query_object_user_by_username(username=session['username']).key
    for book in _query_object_books_with_keyword(keyword=str(keyword).strip(), category=filter, sort=sort):
        if _query_object_user_by_id(id=book.user_id).username == session['username']:
            self_found.append(book)
        if _query_object_user_by_id(id=book.user_id).username != session['username']:
            other_found.append(book)
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter=filter, sort=sort, show=show))
    return render_template(template_name_or_list='result.html', results=_query_object_books_with_keyword(keyword=str(keyword).strip(), category=filter, sort=sort), form_search=form_search, user=_query_object_user_by_id, keyword=keyword, now=datetime, sort=sort, filter=filter, show=show, self_found=self_found, other_found=other_found, encrypt=_encrypt_string, encryption_key=self_encryption_key)


# def __process_search_book_categories(keyword: str, type: str):
#     list_books = []
#     if type == 'title':
#         for book_title in _query_object_book_by_query():
#             if keyword.lower() in book_title.title.lower():
#                 list_books.append(book_title)
#     if type == 'author':
#         for book_author in _query_object_book_by_query():
#             if keyword.lower() in book_author.author.lower():
#                 list_books.append(book_author)
#     if type == 'release_year':
#         if keyword.isdigit():
#             for book_release_year in _query_object_book_by_query():
#                 if int(keyword) == book_release_year.release_year:
#                     list_books.append(book_release_year)
#     return list_books

