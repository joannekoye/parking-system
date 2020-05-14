from . import auth
from flask import render_template, redirect, url_for, flash, request
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, current_user, logout_user, login_required

@auth.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('parking.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('parking.home'))
            flash('You have been logged in!, success')
        else:
            flash('Login Unsuccessful. Please Check username and password', 'danger')
    return render_template('auth/login.html', title='login', form=form)


@auth.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('parking.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email= form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('auth/account.html', title='Account', image_file=image_file)