from flask import Flask, request, render_template, redirect, send_from_directory, flash, session
from forms import ContactForm
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/new',methods=['GET','POST'])
def new():
    if (request.method == 'POST'):
        if (not request.form['name'] or not request.form['surname'] \
                or not request.form['email'] or not request.form['password']):
           flash ('Please fill all the fields.','error')
        else:
            session['name'] = request.form['name']
            return login()
    return render_template('new.html')

@app.route ('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
