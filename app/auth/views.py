from . import auth
from flask import render_template, redirect, url_for
# from ..models import
from .forms import RegistrationForm, LoginForm
# from .. import db

@auth.route("/login")
def login():
    form = LoginForm()
    return render_template('auth/login.html', title='login', form=form)


@auth.route("/register")
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', title='Register', form=form)