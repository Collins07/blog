from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, EqualTo, Length,Email, ValidationError
from app import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign-Up')

    def validate_field(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationErr('Use a different username')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")

    submit = SubmitField('Login')    