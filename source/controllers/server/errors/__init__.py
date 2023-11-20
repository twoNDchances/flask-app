from flask_login import login_required
from flask import Blueprint, render_template, abort, redirect, url_for
from os import listdir
from source.controllers.functions.search.form import SearchForm

errors = Blueprint(name='errors', import_name=__name__)



@errors.app_errorhandler(404)
@login_required
def not_found_error(e):
    form_search = SearchForm()
    if form_search.validate_on_submit():
        get_keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=get_keyword, filter='title', sort='increase', show='card'))
    return render_template(template_name_or_list='errors/404.html', form_search=form_search), 404

