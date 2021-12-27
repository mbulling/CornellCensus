from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired, AnyOf
class form(FlaskForm):
    """
    creates the form for user input
    """
    colleges = ['engineering', 'arts and science', 'dyson', 'cals', 'humec']
    ratings =[1,2,3,4,5,6,7,8,9,10]

    cField = StringField('college', validators=[DataRequired(), AnyOf(colleges)])
    rField = IntegerField('rating', validators=[DataRequired(),AnyOf(ratings)])
    sField = SubmitField('submit')
