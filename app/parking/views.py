from flask import redirect, render_template,jsonify,request
from . import parking
from ..models import Institution,Lot,User,Insights
from ..schemas import institutions_schema,lot_schema
from app import db

@parking.route('/')
def home():
    institutions = Institution.get_all()
    return render_template('parking/home.html',institutions=institutions)


@parking.route('/all_institutions',)
def all_institutions():
    data = Institution.query.all()
    result = institutions_schema.dump(data)
    return jsonify(result)


@parking.route('/institution_<int:institution_id>', methods=['GET','POST'])
def institution(institution_id):
    details = Institution.query.get(institution_id)
    current_user = User.query.get(2)
    title=f'Lots in {details.name}'

    lot_name = request.form.get('lot_name')
    number_plate = request.form.get('number_plate')
    if number_plate and lot_name:
        lot = Lot.query.filter_by(institution_id=institution_id,name=lot_name).first()
        lot.user_id_in = current_user.id
        insight = Insights(institution_id=institution_id,user_id=current_user.id, lot_id=lot.id,number_plate=number_plate)

        db.session.add_all([lot, insight])
        db.session.commit()
        print (lot.id)

    return render_template('parking/institution.html',institution_id=institution_id,title=title)


@parking.route('/lots_of/<int:institution_id>')
def lots_of(institution_id):
    data = Lot.get_from_institution(institution_id)
    result = lot_schema.dump(data)
    return jsonify(result)


    