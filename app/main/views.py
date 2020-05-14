from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user


# your views go here i.e for home,about
@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('parking.home'))
    return render_template('index.html')


@main.route("/about")
def about():
    pass