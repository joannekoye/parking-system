from . import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    role = db.Column(db.String(50), default='user', nullable= False)
    image_file = db.Column(db.String(20), unique= True, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)


    def __repr__(self):
        return f'User("{self.username}","{self.email}")'