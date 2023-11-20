from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import PasswordField, RadioField, StringField, SubmitField
from wtforms.validators import Optional, Regexp


class UpdateUserForm(FlaskForm):
    first_name = StringField(label='First name')
    last_name = StringField(label='Last name')
    username = StringField(label='Username'
                           ,
                           validators=[
                               Optional(),
                               Regexp(r'^[a-zA-Z0-9_]*$',
                                      message='Your username maybe incorrect, please try again!')
                           ]
                           )
    gender = RadioField(label='Gender',
                        choices=[('m', 'Male'), ('f', 'Female')], validators=[Optional()])
    address = StringField(label='Address')

    career = StringField(label='Career')

    email = StringField(label='Email'
                        ,
                        validators=[
                            Optional(),
                            Regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$',
                                   message='Your email maybe incorrect, please try again!')
                        ]
                        )
    phone = StringField(label='Phone'
                        ,
                        validators=[
                            Optional(),
                            Regexp(regex=r'^\d{10}$',
                                   message='Your phone maybe incorrect, please try again!')
                        ]
                        )
    password = PasswordField(label='Password',
                             validators=[
                                 Optional(),
                                 Regexp(regex=r'^[^\s]*$', message='Your password must not contain spaces.')
                             ])
    file = FileField(label='Choose a file',
                     validators=[
                         Optional(),
                         FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='Image only')
                     ])
    phone_rule = RadioField(label='Phone', choices=[('pub', 'Public'), ('pri', 'Private')], validators=[Optional()])
    email_rule = RadioField(label='Email', choices=[(True, 'Public'), (False, 'Private')], validators=[Optional()])
    submit_button = SubmitField('Update')
