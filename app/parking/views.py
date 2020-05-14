from flask import redirect, render_template,jsonify
from . import parking
from ..models import Institution,Lot
from ..schemas import institutions_schema,lot_schema

@parking.route('/')
def home():
    institutions = Institution.get_all()
    return render_template('parking/home.html',institutions=institutions)


@parking.route('/all_institutions',)
def all_institutions():
    data = Institution.query.all()
    result = institutions_schema.dump(data)
    return jsonify(result)


@parking.route('/institution_<int:id>')
def institution(id):
    details = Institution.query.get(id)
    title=f'Lots in {details.name}'
    return render_template('parking/institution.html',institution_id=id,title=title)
@parking.route('/lots_of/<int:institution_id>')
def lots_of(institution_id):
    data = Lot.get_from_institution(institution_id)
    result = lot_schema.dump(data)
    return jsonify(result)


    