from flask_wtf import FlaskForm

from wtforms import StringField, TextField, SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired()])
    subject = StringField("Subject",validators=[DataRequired(),Length(min=2,message=("Too short"))])
    body = TextAreaField("Body",validators=[DataRequired()])
    submit = SubmitField("Submit")