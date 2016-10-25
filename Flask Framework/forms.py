from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField
app = Flask(__name__)

class ContactForm(Form):
    name = TextField("Name")
    surname = TextField("Surname")
    email = TextField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Send")

if __name__ == '__main__':
    app.run(debug = True)
