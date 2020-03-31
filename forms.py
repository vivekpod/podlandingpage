from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField 
from wtforms.validators import DataRequired



class AddForm(FlaskForm):
    email=StringField('Email Address',validators=[DataRequired()])
    state=StringField('State',validators=[DataRequired()])
    city=StringField('City/Town',validators=[DataRequired()])
    phonenumber=StringField('Phone Number',validators=[DataRequired()])
    submit = SubmitField('SUBMIT')
