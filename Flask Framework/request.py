from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():pass

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('profile',username='mark'))

if __name__ == '__main__':
    app.run(debug = True)
