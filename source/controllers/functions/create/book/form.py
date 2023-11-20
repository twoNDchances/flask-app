from datetime import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange

class UploadForm(FlaskForm):
    # file = MultipleFileField(label='Choose files',
    #                          validators=[
    #                              DataRequired(),
    #                          ])
    title = StringField(label='Title of your book', validators=[DataRequired(), Length(min=5, max=100)])
    author = StringField(label='Author', validators=[DataRequired(), Length(min=5, max=100)])
    release_year = IntegerField(label='Release Year',
                                validators=[
                                    InputRequired(),
                                    NumberRange(min=1900, max=datetime.now().year)
                                ])
    file = FileField(label='Choose a file',
                     validators=[
                         DataRequired(),
                         FileAllowed(['pdf'], message='PDF only!')
                     ])
    submit_button = SubmitField('Create')
