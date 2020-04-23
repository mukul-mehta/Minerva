"""
DB Model for Users table
and relevant junction tables
"""
import datetime

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import and_, select

from app.main import db, login_manager
from app.main.models.movies import Movie
from app.main.models.posts import Post
from app.main.models.comments import Comment


class User(db.Model, UserMixin):
    """
    Description of User model.
    Columns
    -----------
    :id: int [pk]
    :username: varchar(128) [not NULL]
    :password: varchar(128) [not NULL]
    :first_name: varchar(255) [not NULL]
    :last_name: varchar(255)
    :dob: date
    :email: varchar(255) [not NULL]
    :fb_handle: varchar(255)
    :twitter_handle: varchar(255)
    :bio: text
    :occupation: varchar(255)
    :profile_picture: int
    :last_login: timestamp
    :creation_time: timestamp
    :is_verified: boolean

    # Relationships
    :watch_list: Relationship -> Movies (one to Many)
    :bucket_list: Relationship -> Movies (one to Many)
    """

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(255), default="")
    last_name = db.Column(db.String(255), default="")
    dob = db.Column(db.DateTime)
    email = db.Column(db.String(255), nullable=False)
    fb_handle = db.Column(db.String(255))
    g_handle = db.Column(db.String(255))
    twitter_handle = db.Column(db.String(255))
    profile_picture = db.Column(db.Integer)
    bio = db.Column(db.Text)
    last_login = db.Column(db.DateTime)
    creation_time = db.Column(db.DateTime)
    is_verified = db.Column(db.Boolean, default=False)

    # Relationships
    watch_list = db.relationship('Movie', backref="user")
    bucket_list = db.relationship('Movie', backref="User")
    posts = db.relationship('Post', backref="user")
    comments = db.relationship('Comment', backref="user")

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.is_verified = False
        self.profile_picture = 1

        db.session.add(self)
        db.session.commit()

    @staticmethod
    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()

    def update_col(self, key, value):
        setattr(self, key, value)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def resetPassword(self, newPassword):
        # Pass in a hashed password
        self.password = generate_password_hash(newPassword)
        db.session.commit()

    def isVerified(self):
        return self.is_verified

    def setVerified(self):
        self.is_verified = True
        db.session.commit()

    def add_to_watch_list(self, imdb_ID):
        movie = Movie.query.filter_by(imdb_ID=imdb_ID).first()
        self.watch_list.append(movie)
        db.session.commit()

    def add_to_bucket_list(self, imdb_ID):
        movie = Movie.query.filter_by(imdb_ID=imdb_ID).first()
        self.bucket_list.append(movie)
        db.session.commit()
