from . import auth
from flask import render_template, redirect, url_for
# from ..models import
from .forms import RegistrationForm, LoginForm
# from .. import db

@auth.route("/login")
def login():
    return "<h1>You are now logged in</h1>"