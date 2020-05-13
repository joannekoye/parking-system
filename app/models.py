from app import db
from datetime import datetime
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(), default='user')
    sessions = db.relationship('Session', backref='session', lazy='dynamic')

class Institution(db.Model):
    __tablename__='institutions'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String())
    name = db.Column(db.String())

    @classmethod
    def get_all(cls):
        return Institution.query.all()


class Lot(db.Model):
    __tablename__='lots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id_in = db.Column(db.Integer)
    session_id_in = db.Column(db.Integer, db.ForeignKey('sessions.id'))

class Session(db.Model):
    __tablename__='sessions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lot_id = db.Column(db.Integer, db.ForeignKey('lots.id'))
    number_plate = db.Column(db.String(), nullable=False)
    time_in = db.Column(db.DateTime(),default=datetime.utcnow)
    time_out = db.Column(db.DateTime())

    