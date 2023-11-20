from os import remove, rename
from flask import redirect, render_template, session, url_for
from source import database
from source.controllers.functions.update.user.form import UpdateUserForm
from source.controllers.functions.search.form import SearchForm
from source.controllers.processor.queries import _query_avatar_id_by_user_id, _query_avatar_path_by_user_id, _query_object_avatar_by_id, _query_object_user_by_email, _query_object_user_by_id, _query_object_user_by_phone, _query_object_user_by_username, _query_user_id_by_username
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash

def _process_update():
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='card'))
    form = UpdateUserForm()
    if form.validate_on_submit():
        get_firstname = form.first_name.data
        get_lastname = form.last_name.data
        get_gender = __process_set_gender(choices=form.gender.data)
        get_address = form.address.data
        get_career = form.career.data
        get_phone = form.phone.data
        get_email = form.email.data
        get_username = form.username.data
        get_password = form.password.data
        get_avatar = form.file.data
        get_phone_rule = __process_set_seeable(choices=form.phone_rule.data)
        get_email_rule = __process_set_seeable(choices=form.email_rule.data)
        if get_phone_rule != '':
            __process_update_user(categorize='phone_rule', data=bool(get_phone_rule))
        if get_email_rule != '':
            __process_update_user(categorize='email_rule', data=bool(get_email_rule))
        if get_username != '':
            query_username_exist = _query_object_user_by_username(username=get_username)
            if query_username_exist is not None:
                session['username_alert'] = 'Username exist!'
            else:
                get_old_avatar_path = _query_avatar_path_by_user_id(
                    user_id=_query_user_id_by_username(username=session['username']))
                get_new_avatar_path = get_old_avatar_path.replace(str(session['username']), get_username)
                __process_update_avatar(path_image=get_new_avatar_path)
                __process_update_user(categorize='username', data=get_username)
                rename(r'/var/www/flask-app/source/static/{current_username}'.format(current_username=session['username']),
                       rf'/var/www/flask-app/source/static/{get_username}')
                session['username'] = get_username
                session['username_alert'] = None
        if get_avatar is not None:
            file_name = secure_filename(get_avatar.filename)
            remove(path=_query_avatar_path_by_user_id(user_id=_query_user_id_by_username(username=session['username'])))
            get_path = r'/var/www/flask-app/source/static/{username}/avatar/{file_name}'.format(username=session['username'], file_name=file_name)
            get_avatar.save(get_path)
            __process_update_avatar(path_image=get_path)
        if get_firstname != '':
            __process_update_user(categorize='first_name', data=get_firstname)
        if get_lastname != '':
            __process_update_user(categorize='last_name', data=get_lastname)
        if get_gender != '':
            __process_update_user(categorize='gender', data=get_gender)
        if get_address != '':
            __process_update_user(categorize='address', data=get_address)
        if get_career != '':
            __process_update_user(categorize='career', data=get_career)
        if get_password != '':
            __process_update_user(categorize='password', data=get_password)
        if get_email != '':
            query_email_exist = _query_object_user_by_email(email=get_email)
            if query_email_exist is not None:
                session['email_alert'] = 'Email exist!'
            else:
                __process_update_user(categorize='email', data=get_email)
                session['email_alert'] = None
        if get_phone != '':
            query_phone_exist = _query_object_user_by_phone(phone=get_phone)
            if query_phone_exist is not None:
                session['phone_alert'] = 'Phone exist!'
            else:
                __process_update_user(categorize='phone', data=get_phone)
                session['phone_alert'] = None
        return redirect(url_for('show.showuser.profile', username=session['username']))
    return render_template(template_name_or_list='update.html', form=form, form_search=form_search)


def __process_update_user(categorize: str, data: str):
    user = _query_object_user_by_id(
        id=_query_user_id_by_username(
            username=session['username']
            )
            )
    if categorize == 'username':
        user.username = data
    elif categorize == 'first_name':
        user.first_name = data
    elif categorize == 'last_name':
        user.last_name = data
    elif categorize == 'gender':
        user.gender = data
    elif categorize == 'address':
        user.address = data
    elif categorize == 'career':
        user.career = data
    elif categorize == 'phone':
        user.phone = data
    elif categorize == 'email':
        user.email = data
    elif categorize == 'password':
        user.password = generate_password_hash(data)
    elif categorize == 'phone_rule':
        user.rule.phone_rule = data
    elif categorize == 'email_rule':
        user.rule.email_rule = data
    database.session.add(user)
    database.session.commit()


def __process_update_avatar(path_image: str):
    avatar = _query_object_avatar_by_id(id=_query_avatar_id_by_user_id(user_id=_query_user_id_by_username(username=session['username'])))
    avatar.image = path_image
    database.session.add(avatar)
    database.session.commit()


def __process_set_gender(choices: str):
    if choices == 'm':
        return 'Male'
    elif choices == 'f':
        return 'Female'
    else:
        return ''


def __process_set_seeable(choices: str):
    if choices == 'pub':
        return True
    elif choices == 'pri':
        return False
    else:
        return None