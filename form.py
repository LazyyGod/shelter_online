from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(),])
    email =
    password = PasswordField("Password",validators=[DataRequired(),])
    submit = SubmitField() #кнопка «отправить»