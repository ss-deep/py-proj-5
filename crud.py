"""CRUD operations."""
from model import db,User,Movie,Rating,connect_to_db

# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_movie(title, overview, release_date, poster_path):
    movie=Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    db.session.add(movie)
    db.session.commit()
    return movie

def create_rating(user, movie, score):
    rating=Rating(user=user, movie=movie, score=score)
    db.session.add(rating)
    db.session.commit()
    return rating



# connect you to the database when you run crud.py
if __name__=="__main__":
    from server import app
    connect_to_db(app)
