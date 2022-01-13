from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField
from wtforms.validators import DataRequired, AnyOf
class form(FlaskForm):
    """
    creates the form for user input
    """
    colleges = ['College of Engineering', 'College of Arts and Sciences', 'Dyson School of Business', 'College of Agriculture and Life Sciences', 'College of Human Ecology']
    majorsCOE = ['Computer Science', 'Electrical and Computer Engineering', 'Mechanical Engineering']
    years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    ratings =[1,2,3,4,5,6,7,8,9,10]

    cField = SelectField('Select Your College', choices=colleges)
    mField = SelectField('Select Your Major', choices=majorsCOE)
    yField = SelectField('Select Your Year', choices=years)
    rField = IntegerField('Rating', validators=[DataRequired(),AnyOf(ratings)])
    sField = SubmitField('Submit')
