from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={


  'apiKey': "AIzaSyAQiDBb_rgeMQyRpjFQMgpUJKX1pPAqXys",
  'authDomain': "fire-base-authentication-lab.firebaseapp.com",
  'projectId': "fire-base-authentication-lab",
  'storageBucket': "fire-base-authentication-lab.appspot.com",
  'messagingSenderId': "986265167518",
  'appId': "1:986265167518:web:449e75122da49e2ab47d8f",
  'measurementId': "G-D1HYL46KN7",
  'databaseURL':'https://test-91859-default-rtdb.europe-west1.firebasedatabase.app/'
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():

    error = ''
    if request.method == 'POST':
        email= request.form['email']
        password= request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return render_template("add_tweet.html")

        except:
            error = 'Authentication failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':
        full_name:request.form['full_name']
        email= request.form['email']
        password= request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            return render_template("add_tweet.html")

        except:
            error = 'Authentication failed'
    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)