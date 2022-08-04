from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post', backref='user', passive_deletes=True) # Stores posts made by this user, which can be backreferenced through post.user

class Post(db.Model): # Post model
    id = db.Column(db.Integer, primary_key=True) # ID of the post
    text = db.Column(db.Text, nullable=False) # Text of the post, cannot be null
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # Date post was made
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="Cascade"), nullable=False) # User who made post, is foreign key