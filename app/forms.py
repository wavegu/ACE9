# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
from user.user import User
from flask_wtf import Form
from wtforms import StringField
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms.validators import EqualTo
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import DataRequired


class RegisterForm(Form):
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])