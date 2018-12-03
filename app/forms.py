from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SyringeForm(Form):
    syringe = StringField('syringe', validators=[DataRequired()])
    plunger = StringField('plunger', validators=[DataRequired()])
    

class RcontrolForm(Form):
    experiment = StringField('experiment', validators=[DataRequired()])
    runs = StringField('runs', validators=[DataRequired()])