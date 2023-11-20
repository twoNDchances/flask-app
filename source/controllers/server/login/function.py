from flask import redirect, render_template, request, session, flash, url_for
from flask_login import login_user
from source.controllers.server.login.form import LoginForm
from source.controllers.processor.queries import _check_login, _query_object_user_by_username


def _process_login():
    form = LoginForm()
    if form.validate_on_submit():
        get_username = form.username.data
        get_password = form.password.data
        check_username = _query_object_user_by_username(username=get_username)
        if check_username is not None and _check_login(username=get_username, password=get_password):
            session['username'] = form.username.data
            login_user(check_username)
            do_next = request.args.get('next')
            if do_next is None:
                return redirect(url_for('list.list.library', page=1))
            else:
                # return redirect(url_for(do_next[1:]))
                return redirect(do_next)
        else:
            flash('Your account maybe incorrect or not exist!')
    return render_template(template_name_or_list='login.html', form=form)
