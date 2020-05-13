from . import auth
from flask import render_template, redirect, url_for, flash
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
from flask_login import login_user, current_user

@auth.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.index'))
            flash('You have been logged in!, success')
        else:
            flash('Login Unsuccessful. Please Check username and password', 'danger')
    return render_template('auth/login.html', title='login', form=form)


@auth.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)