from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,SubmitField,PasswordField,IntegerField,BooleanField
from wtforms.validators import Required

class InstitutionForm(FlaskForm):
    name = StringField('Institution Name')
    lot_numbers = SelectField('Lot Quantity',validators=[Required()], choices=['8','10','12','16','20','24'])
    active = BooleanField('Active')
    submit = SubmitField('Commit Institution')