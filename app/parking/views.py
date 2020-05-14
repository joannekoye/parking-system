from flask import redirect, render_template,jsonify,request,url_for
from . import parking
from ..models import Institution,Lot,User,Insights
from ..schemas import institutions_schema,lot_schema
from flask_login import login_required,current_user
from app import db
from datetime import datetime
@parking.route('/')
@login_required
def home():
    institutions = Institution.get_all()
    return render_template('parking/home.html',institutions=institutions)


@parking.route('/all_institutions')
def all_institutions():
    data = Institution.query.all()
    result = institutions_schema.dump(data)
    return jsonify(result)


@parking.route('/institution_<int:institution_id>', methods=['GET','POST'])
@login_required
def institution(institution_id):
    details = Institution.query.get(institution_id)
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
@parking.route('/user_insights')
@login_required
def user_insights():
    user_id = current_user.id
    insights = Insights.get_for_user(user_id)

    return render_template('parking/user_insights.html',insights=insights)

@parking.route('/lots_of/<int:institution_id>')
def lots_of(institution_id):
    data = Lot.get_from_institution(institution_id)
    result = lot_schema.dump(data)
    return jsonify(result)

@parking.route('/release/<int:insight_id>')
@login_required
def release(insight_id):
    insight = Insights.query.get(insight_id)
    insight.time_out =datetime.utcnow()
    lot = Lot.query.get(insight.lot_id)
    lot.user_id_in=None
    db.session.add_all([insight,lot])
    db.session.commit()

    return redirect(url_for('parking.user_insights'))
