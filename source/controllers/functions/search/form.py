from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp


class SearchForm(FlaskForm):
    keyword = StringField(label='Search', validators=[DataRequired(), Regexp(regex='[a-zA-Z0-9 ]', message='Only characters and digits!')], render_kw={'class': 'btn btn-outline-success my-2 my-sm-0', 'placeholder': 'Search'})
    submit_button = SubmitField(label='Search')
