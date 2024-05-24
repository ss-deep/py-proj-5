"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

POSTGRES_URI=os.getenv("POSTGRES_URI")

def connect_to_db(flask_app, db_uri=POSTGRES_URI, echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


class User(db.Model):
   """A user."""

   __tablename__ = "users"

   user_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
   email = db.Column(db.String, unique=True)
   password = db.Column(db.String)
   # ratings = a list of Rating objects

   def __repr__(self):
      return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):

    __tablename__="movies"
    movie_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    title=db.Column(db.String)
    overview=db.Column(db.Text)
    release_date=db.Column(db.DateTime)
    poster_path=db.Column(db.String)
    

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} Title={self.poster_path}>'

class Rating(db.Model):

    __tablename__="ratings"
    rating_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    score=db.Column(db.Integer)
    movie_id=db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id=db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie=db.relationship("Movie", backref="ratings")
    user=db.relationship("User", backref="ratings")

    def __repr__(self):
        return f'<Ratings rating_id={self.rating_id} score={self.score}>'


if __name__ == "__main__":
    from server import app
    connect_to_db(app,echo=False)


#you will need this only if want to create db
    # with app.app_context():
    #     db.create_all()
