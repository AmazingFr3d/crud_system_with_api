from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from .models import User


class RegisterForm(FlaskForm):
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists.')

    name = StringField('name', validators=[DataRequired(), Length(2, 20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(8, 20)])
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('role', validators=[DataRequired()], choices=[('user', 'User'), ('admin', 'Admin')])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Log In')


class PassResetForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
