from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    subject=StringField('Subject', validators=[DataRequired()])
    message=StringField('Message', validators=[DataRequired()])
