from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Post
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        entry = request.form.get('entry')

        if len(entry) < 1:
            flash('Entry is too short!', category='error')
        else:
            new_entry = Post(entry=entry, user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Entry has been added.', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    e = json.loads(request.data)
    print(e)
    entryId = e['entryId']
    entry = Post.query.get(entryId)
    if entry:
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
    
    return jsonify({})