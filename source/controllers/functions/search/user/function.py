from flask import render_template, redirect, url_for, session
from flask_login import current_user
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.queries import _query_object_users_with_keyword

def _process_search_user(keyword, filter, sort):
    selfs = []
    others = []
    users = _query_object_users_with_keyword(keyword=str(keyword).strip(), category=filter, sort=sort)
    for user in users:
        if user.username != session['username']:
            others.append(user)
        if user.username == session['username']:
            selfs.append(user)
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_user.searchuser', keyword=keyword, filter=filter, sort='increase'))
    return render_template(template_name_or_list='result_user.html', users=_query_object_users_with_keyword(category=filter, keyword=str(keyword).strip(), sort=sort), form_search=form_search, keyword=keyword, sort=sort, filter=filter, selfs=selfs, others=others)


# def _process_search_user_categories(keyword: str, type: str) -> list:
#     list_users = []
#     if type == 'username':
#         for user in _query_object_user_by_query():
#             if keyword in user.username:
#                 list_users.append(user)
#     if type == 'first_name':
#         for user in _query_object_user_by_query():
#             if keyword in user.first_name:
#                 list_users.append(user)
#     if type == 'last_name':
#         for user in _query_object_user_by_query():
#             if keyword in user.last_name:
#                 list_users.append(user)
#     if type == 'email':
#         for user in _query_object_user_by_query():
#             if keyword == user.email:
#                 list_users.append(user)
#     if type == 'phone':
#         for user in _query_object_user_by_query():
#             if keyword == user.phone:
#                 list_users.append(user)
#     if type == 'career':
#         for user in _query_object_user_by_query():
#             if keyword in user.career:
#                 list_users.append(user)
#     if type == 'address':
#         for user in _query_object_user_by_query():
#             if keyword in user.address:
#                 list_users.append(user)
#     return list_users

