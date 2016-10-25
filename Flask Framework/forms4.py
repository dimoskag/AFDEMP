from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField
app = Flask(__name__)

@app.route('/new',methods=['GET','POST'])
def new():
    if (request.method == 'POST'):
        pass
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug = True)
