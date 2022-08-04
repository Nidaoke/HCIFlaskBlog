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
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)

class Post(db.Model): # Post model
    id = db.Column(db.Integer, primary_key=True) # ID of the post
    text = db.Column(db.Text, nullable=False) # Text of the post, cannot be null
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # Date post was made
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="Cascade"), nullable=False) # User who made post, is foreign key
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID of the Comment
    text = db.Column(db.String(200), nullable=False) # Text of the Comment, cannot be null, 200 chars
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # Date comment was made
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="Cascade"), nullable=False) # User who made comment
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="Cascade"), nullable=False) # Post comment is on

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)