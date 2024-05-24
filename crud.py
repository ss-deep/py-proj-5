"""CRUD operations."""
from model import db,User,Movie,Rating,connect_to_db
 


# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def get_single_user(user_id):
    return User.query.get(user_id)

def create_movie(overview, poster_path, release_date, title ):
    movie=Movie(overview=overview, poster_path=poster_path, release_date=release_date, title=title )
    db.session.add(movie)
    db.session.commit()
    return movie

def get_all_movies():
    return Movie.query.all()

def get_single_movie(movie_id):
    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    rating=Rating(user=user, movie=movie, score=score)
    db.session.add(rating)
    db.session.commit()
    return rating


# connect you to the database when you run crud.py
# if __name__=="__main__":
#     from server import app
#     connect_to_db(app)
