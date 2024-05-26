"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session, redirect,url_for)
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
    # session.clear()
    # print(f"user_id: {session['user_id']}")
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    movies=crud.get_all_movies()
    return render_template('all_movies.html',movies=movies)

@app.route('/movie/<movie_id>')
def single_movie(movie_id):
    if 'user_id' in session:
        movie,rating=crud.get_single_movie(movie_id,session['user_id'])
        return render_template('movie_details.html',movie=movie,rating=rating)
    else:
        flash('Please login to see the details')
        return render_template('homepage.html')

@app.route('/change_rating/<movie_id>', methods=['POST'])
def change_rating(movie_id):
    new_rating = request.form.get('options')
    crud.update_rating(movie_id,session['user_id'],new_rating)
    # return single_movie(movie_id)
    return redirect(url_for('single_movie', movie_id=movie_id))
    
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
    elif email and password:
        flash("User created. Please Login.")
    else:
        flash("Please enter email or password")
    return render_template("homepage.html")


@app.route('/login',methods=['POST'])
def login():
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
    return redirect('/movies')

@app.route('/logout')
def logout():
     session.clear()
     flash('Logged out!')
     return render_template("homepage.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run( debug=True)
