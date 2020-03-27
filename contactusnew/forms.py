from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField

from wtforms import validators, ValidationError


class ContactForm(Form):
    name = TextField("Name", [validators.InputRequired("Please enter name")])
    email = TextField("Email", [validators.InputRequired("Please enter email"), validators.Email("Please enter email")])
    subject = TextField("Subject", [validators.InputRequired("Please enter subject")])
    message = TextAreaField("Message", [validators.InputRequired("Please enter message")])
    submit = SubmitField("Send")
