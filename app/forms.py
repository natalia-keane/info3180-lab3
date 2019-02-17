from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name=StringField('name',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired()])
    subject=StringField('subject', validators=[DataRequired()])
    message=StringField('message', validators=[DataRequired()])
