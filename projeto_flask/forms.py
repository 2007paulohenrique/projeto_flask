from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CPFForm(FlaskForm):
    documento = StringField('CPF', validators=[DataRequired()])
    submit = SubmitField('validar')

class CNPJForm(FlaskForm):
    documento = StringField('CNPJ', validators=[DataRequired()])
    submit = SubmitField('validar')
