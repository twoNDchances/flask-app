from flask import redirect, render_template, url_for
from source.controllers.functions.search.form import SearchForm

def _process_main_root():
    return redirect(url_for('system.home.home'))

def _process_home():
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    return render_template(template_name_or_list='home.html', form_search=form_search)