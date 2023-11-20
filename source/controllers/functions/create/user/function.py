from os import mkdir
from shutil import copyfile
from flask import redirect, render_template, url_for
from source import database
from source.controllers.functions.create.user.form import RegistrationForm
from source.controllers.processor.crypto import _generate_bytes_for_url_crypto
from source.controllers.processor.queries import _query_object_user_by_email, _query_object_user_by_phone, _query_object_user_by_username, _query_user_id_by_username
from source.datatable import Avatar, User, Rule


def _process_register():
    username_alert, email_alert, phone_alert = None, None, None
    form = RegistrationForm()
    if form.validate_on_submit():
        get_firstname = form.first_name.data
        get_lastname = form.last_name.data
        get_phone = form.phone.data
        get_email = form.email.data
        get_gender = __process_set_gender(choices=str(form.gender.data))
        get_address = form.address.data
        get_career = form.career.data
        get_username = form.username.data
        get_password = form.password_confirm.data
        query_username_exist = _query_object_user_by_username(username=get_username)
        query_email_exist = _query_object_user_by_email(email=get_email)
        query_phone_exist = _query_object_user_by_phone(phone=get_phone)
        if query_username_exist is None and query_email_exist is None and query_phone_exist is None:
            add_user = User(
                first_name=get_firstname,
                last_name=get_lastname,
                username=get_username,
                email=get_email,
                phone=get_phone,
                password=get_password,
                address=get_address,
                career=get_career,
                gender=get_gender,
                key=_generate_bytes_for_url_crypto()
            )
            database.session.add(add_user)
            database.session.commit()
            database.session.add(Rule(user_id=_query_user_id_by_username(username=get_username), phone_rule=False, email_rule=False))
            database.session.commit()
            mkdir(path=fr'/var/www/flask-app/source/static/{get_username}')
            mkdir(path=fr'/var/www/flask-app/source/static/{get_username}/avatar')
            mkdir(path=fr'/var/www/flask-app/source/static/{get_username}/books')
            mkdir(path=fr'/var/www/flask-app/source/static/{get_username}/images')
            avatar = __process_set_default_avatar(get_username)
            initial_avatar = Avatar(str(avatar), _query_user_id_by_username(username=get_username))
            database.session.add(initial_avatar)
            database.session.commit()
            return redirect('/login')
        if query_username_exist is not None:
            username_alert = 'Username exist!'
        if get_username == 'Server' or get_username == 'server':
            username_alert = 'Your username is not accepted!'
        if query_email_exist is not None:
            email_alert = 'Email exist!'
        if query_phone_exist is not None:
            phone_alert = 'Phone exist!'
        return render_template(template_name_or_list='register.html',
                               form=form,
                               username_alert=username_alert,
                               email_alert=email_alert,
                               phone_alert=phone_alert
                               )
    return render_template(template_name_or_list='register.html', form=form)


def __process_set_gender(choices: str):
    if choices == 'm':
        return 'Male'
    elif choices == 'f':
        return 'Female'
    else:
        return ''
    

def __process_set_default_avatar(new_username: str):
    source = r'/var/www/flask-app/source/static/Server/resources/user/new_user.png'
    destination = fr'/var/www/flask-app/source/static/{new_username}/avatar/new_user.png'
    return copyfile(src=source, dst=destination)
