from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional,
)


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[
        Length(min=6), Email(message='Enter a valid email.'), DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Confirm Your Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')])
    website = StringField('Website',validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField('Email', validators=[
        DataRequired(), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[
        Email(message='Not a valid email address.'), DataRequired()])
    body = TextAreaField('Message', validators=[
        DataRequired(), Length(min=4, message='Your message is too short.')])
    recaptcha = RecaptchaField(default='')
    submit = SubmitField('Submit')
