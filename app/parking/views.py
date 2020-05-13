from flask import redirect, render_template
from . import parking
from ..models import Institution

@parking.route('/')
def home():
    institutions = Institution.get_all()
    return render_template('parking/home.html',institutions=institutions)

@parking.route('/<int:id>')
def institution(id):
    return render_template('parking/institution.html')


@parking.route('/test/', methods=['GET','POST'])
def test():
    clicked=None
    if request.method == "POST":
        clicked=request.form['data']
    return render_template('test.html')