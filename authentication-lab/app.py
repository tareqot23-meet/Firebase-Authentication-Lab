from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



config={
    
  "apiKey": "AIzaSyBGljqzVxqgTRfap9LLgYcZwlmxWWgPzTk",
  "authDomain": "test-91859.firebaseapp.com",
  "databaseURL": "https://test-91859-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "test-91859",
  "storageBucket": "test-91859.appspot.com",
  "messagingSenderId": "110938425702",
  "appId": "1:110938425702:web:1b947c5c1f229d9173e0a7",
  "measurementId": "G-YMJ8Q21MK7"
  

}



firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
app=Flask(__name__)




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
           error = "Authentication failed"
        return render_template("signin.html")
    else:
        if request.method == 'GET':
            return render_template("signin.html")


    


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':



        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        fullname = request.form['fullname']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"fullname":fullname,"bio":bio,"password":password,"username":username,"email":email}
            db.child("users").child(login_session['user']['localId'] ).set(user)




            return redirect(url_for('add_tweet'))

        except:
           error = "Authentication failed"
           return error

 
    else:
         if request.method == 'GET':
            return render_template("signup.html")

    




@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():

    if request.method == 'POST':

        text=request.form['text']
        title=request.form['title']

        
        try:
            tweet={"text":text,"title":title}
            db.child("tweets").push(tweet)
            
            return redirect(url_for('all_tweets'))

        except:
           error = "Authentication failed"
           return error

 
    else:

        if request.method == 'GET':
            return render_template("add_tweet.html")




@app.route('/all_tweets')
def all_tweets():
    tweets=db.child("tweets").get().val().values()
    return render_template("tweets.html",tweets=tweets)


if __name__ == '__main__':
    app.run(debug=True)





    