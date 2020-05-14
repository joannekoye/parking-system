from app import db
from datetime import datetime
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(), default='user')
    insights = db.relationship('Insights', backref='session', lazy='dynamic')

class Institution(db.Model):
    __tablename__='institutions'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String())
    name = db.Column(db.String())
    active = db.Column(db.String(),default='true')
    quantity = db.Column(db.Integer,default=8)
    lot_details = db.relationship('Lot', backref='lot_dets',lazy='dynamic')

    def get_all():
        return Institution.query.all()


class Lot(db.Model):
    __tablename__='lots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id_in = db.Column(db.Integer)
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'))
    session_id_in = db.Column(db.Integer, db.ForeignKey('insights.id'))

    @classmethod
    def create_lots(cls,tag_name,quantity):
        if(tag_name and quantity):
            for lot in range(quantity):
                institution_id = Institution.query.filter_by(tag_name=tag_name).first()
                lot_name = f'P-{str(lot+1).zfill(2)}'
                lot_item = Lot(name=lot_name,institution_id=institution_id.id)
                db.session.add(lot_item)
                db.session.commit()
        
    def get_from_institution(id):
        return Lot.query.filter_by(institution_id=id).all()

    def __repr(self):
        return self

class Insights(db.Model):
    __tablename__='insights'
    id = db.Column(db.Integer, primary_key=True)
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lot_id = db.Column(db.Integer, db.ForeignKey('lots.id'))
    number_plate = db.Column(db.String(), nullable=False)
    time_in = db.Column(db.DateTime(),default=datetime.utcnow)
    time_out = db.Column(db.DateTime())

    