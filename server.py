"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from flask import Flask

app = Flask(__name__)
app.secret_key="dev"
app.jinja_env.undefined=StrictUndefined
app.app_context().push()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    movies=crud.get_all_movies()
    return render_template('all_movies.html',movies=movies)

@app.route('/movie/<movie_id>')
def single_movie(movie_id):
        movie=crud.get_single_movie(movie_id)
        return render_template('movie_details.html',movie=movie)

@app.route('/users')
def all_users():
    users=crud.get_all_users()
    return render_template('all_users.html',users=users)

@app.route('/user/<user_id>')
def single_user(user_id):
        user=crud.get_single_user(user_id)
        return render_template('user_details.html',user=user)

@app.route('/users',methods=["POST"])
def register_user():
    email=request.form.get('email')
    password=request.form.get('password')
    result=crud.get_user_by_email(email)
    if result:
        flash("User already exists.")
        print(f"result : {result}")
    else:

        flash("User created.")
    return render_template("homepage.html")

@app.route('/login',methods=['POST'])
def login():
    session['user_id']=0
    email=request.form.get('email')
    password=request.form.get('password')
    user=crud.get_user_by_email(email)
    if user and user.password==password:
        flash("Login Successful!")
        session['user_id']=user.user_id
        # print(session['user_id'])
    else:
        flash("Please enter correct email or password")
    return render_template("homepage.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run( debug=True)
