from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Quote
from flask_login import login_required, current_user
from .. import db, photos
from .forms import UpdateProfile
from ..requests import *
#from .forms import BlogForm,CommentForm

@main.route('/')
def home():
    '''
    View root function that returns index template
    '''
    quotes = get_quote()
    
    return render_template('home.html', quotes=quotes)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

# @main.route('/quotes')
# def quotes():

#     '''
#     '''
#     quotes = get_quote()
#     title = 'LetsBlog | Quotes'
    
#     return render_template('home.html', title = title,quotes = quotes)    