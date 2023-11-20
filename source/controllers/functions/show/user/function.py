from flask import redirect, render_template, session, url_for
from source.controllers.processor.queries import _query_avatar_path_by_user_id, _query_object_user_by_username, _query_user_id_by_username, _query_all_book_by_username
from source.controllers.functions.search.form import SearchForm


def _process_profile(username):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    got_information = _query_object_user_by_username(username=session['username'])
    get_avatar = _query_avatar_path_by_user_id(user_id=_query_user_id_by_username(username=got_information.username))
    state = None
    if _query_all_book_by_username(username=got_information.username).__len__() > 1:
        state = 'books'
    else:
        state = 'book'
    return render_template(template_name_or_list='profile.html', get_avatar_path=get_avatar[26:],
                           first_name=got_information.first_name, last_name=got_information.last_name,
                           username=got_information.username, email=got_information.email, phone=got_information.phone,
                           gender=got_information.gender, address=got_information.address, career=got_information.career, available=_query_all_book_by_username(username=got_information.username).__len__(), state=state, form_search=form_search, rule=got_information.rule)
