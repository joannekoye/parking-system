from . import auth
from flask import render_template, redirect, url_for, flash
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt

@auth.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@project.com' and form.password.data=='password':
            flash('You have been logged in!, success')
            return redirect(url_for('main.index'))
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