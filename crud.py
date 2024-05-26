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

def get_single_movie(movie_id,user_id):
    movie=Movie.query.get(movie_id)
    rating=Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first()
    return movie,rating

def create_rating(user, movie, score):
    rating=Rating(user=user, movie=movie, score=score)
    db.session.add(rating)
    db.session.commit()
    return rating

def update_rating(movie_id,user_id,new_rating):
    rating=Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first()
    if not rating:
        user = User.query.get(user_id)
        movie = Movie.query.get(movie_id)
        return create_rating(user,movie,new_rating)
    else:
        rating.score=new_rating
        db.session.commit()
        return rating
    

def get_user_by_email(email):
    user=User.query.filter(User.email==email).first()
    return user if user else None
    # return User.query.filter(User.email == email).first()


# connect you to the database when you run crud.py
# if __name__=="__main__":
#     from server import app
#     connect_to_db(app)
