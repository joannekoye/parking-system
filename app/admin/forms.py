from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,SubmitField,PasswordField

class InstitutionForm(FlaskForm):
    name = StringField('Institution Name')
    submit = SubmitField('Add')