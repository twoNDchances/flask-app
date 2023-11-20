from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import Optional, Length, NumberRange


class UpdateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[Optional(), Length(min=5, max=100)])
    author = StringField(label='Author', validators=[Optional(), Length(min=5, max=100)])
    release_year = IntegerField(label='Release Year',
                                validators=[
                                    Optional(),
                                    NumberRange(min=1900, max=datetime.now().year)
                                ])
    submit_button = SubmitField(label='Confirm')
