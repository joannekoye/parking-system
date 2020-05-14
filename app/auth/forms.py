from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required(),Length(min=2,max=20)])
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username Taken. Please Choose another')   

    def validate_email(self, email):
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('Email already registered.') 


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember =BooleanField('Remember Me')
    submit = SubmitField('Login') 
