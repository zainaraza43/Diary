'''
views.py
How different pages are viewed by different users
'''
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Post, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required  # Must be logged in to view
def home():
    if request.method == 'POST':
        entry = request.form.get('entry')

        if len(entry) < 1:  # If someone submitted an empty entry
            flash('Tweet is too short!', category='error')
        else:
            # Adds the entry to the database
            new_entry = Post(entry=entry, user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Tweet has been Posted.', category='success')

    # Retrieve all users from the database
    users = User.query.all()

    return render_template("home.html", user=current_user, users=users)


@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    e = json.loads(request.data)
    entryId = e['entryId']  # Retrieves the entryId of the entry to be removed
    entry = Post.query.get(entryId)
    if entry:  # If the entry exists
        if entry.user_id == current_user.id:
            db.session.delete(entry)  # Delete the entry
            db.session.commit()
        else:
            flash('Cannot delete other users\' Tweets!', category='error')

    return jsonify({})
