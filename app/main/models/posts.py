"""
DB Model for Posts and
relevant junction tables
"""
import datetime

from sqlalchemy.sql import and_, select

from app.main import db, login_manager
from app.main.models.comments import Comment


class Post(db.Model):
    """
    Description of User model.
    Columns
    -----------
    :id: int [pk]
    :title: Text [not NULL]
    :author_id: int [Foreign Key]
    :creation_time: DateTime [not NULL]
    :last_edit_time: DateTime [not NULL]
    :post_body: Text

    # Relationships
    :comments: Relationship -> Comments (one to many)
    """

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creation_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_edit_time = db.Column(db.DateTime, default=datetime.datetime.now())
    post_body = db.Column(db.Text)

    # Relationships
    comments = db.relationship('Comment', backref="post")

    def __init__(self):
        pass
        #TODO: Create __init__ method

    def update_col(self, key, value):
        setattr(self, key, value)
        db.session.commit()
