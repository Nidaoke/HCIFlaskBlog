# webpages / blueprint
# store views route

from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    posts = Post.query.all() # Gets all posts
    return render_template("home.html", user=current_user, posts=posts)
    # flask knows to search for templates in folders called "templates"
    # We also pass posts into the template so they can be accessed

@views.route("/create-post", methods=['GET', 'POST']) # Route for creating post
@login_required # Must be logged in
def create_post():
    if request.method== "POST": # If Post button is clicked
        text = request.form.get('text') # Get text from form
        if not text: # Text cannot be empty
            flash('Post cannot be empty', category='error')
        else: 
            post = Post(text=text, author=current_user.id) # Create post
            db.session.add(post) # Add post to database
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home')) # Go back to home
    return render_template('createpost.html', user=current_user) # Go to create post page, pass user