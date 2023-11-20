from flask_wtf import FlaskForm
from wtforms import PasswordField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField(label='First Name',
                             validators=[
                                 DataRequired()
                             ])
    last_name = StringField(label='Last Name',
                            validators=[
                                DataRequired()
                            ])
    username = StringField(label='Username',
                           validators=[
                               DataRequired(),
                               Regexp(r'^[a-zA-Z0-9_]*$', message='Your username maybe incorrect, please try again!')
                           ])
    gender = RadioField(label='Gender',
                        choices=[('m', 'Male'), ('f', 'Female')],
                        validators=[
                            DataRequired(message='You should be either male or female')
                        ])
    address = StringField(label='Address', validators=[DataRequired()])
    career = StringField(label='Career', validators=[DataRequired()])
    email = StringField(label='Email',
                        validators=[
                            DataRequired(),
                            Regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$',
                                   message='Your email maybe incorrect, please try again!')
                        ])
    phone = StringField(label='Phone Number',
                        validators=[
                            DataRequired(),
                            Regexp(regex=r'^\d{10}$', message='Your phone maybe incorrect, please try again!')
                        ])
    password = PasswordField(label='Password',
                             validators=[
                                 DataRequired()
                             ])
    password_confirm = PasswordField(label='Password Confirm',
                                     validators=[
                                         DataRequired(),
                                         EqualTo(
                                             fieldname='password',
                                             message='Your confirm password is not match with password!'
                                         )
                                     ])
    submit_button = SubmitField(label='Register')
