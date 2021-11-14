'''
views.py
How different pages are viewed by different users
'''
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Post
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required # Must be logged in to view
def home():
    if request.method == 'POST':
        entry = request.form.get('entry')

        if len(entry) < 1: # If someone submitted an empty entry
            flash('Entry is too short!', category='error')
        else:
            new_entry = Post(entry=entry, user_id=current_user.id) # Adds the entry to the database
            db.session.add(new_entry)
            db.session.commit()
            flash('Entry has been added.', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    e = json.loads(request.data)
    entryId = e['entryId'] # Retrieves the entryId of the entry to be removed
    entry = Post.query.get(entryId)
    if entry: # If the entry exists
        if entry.user_id == current_user.id:
            db.session.delete(entry) # Delete the entry
            db.session.commit()
    
    return jsonify({})