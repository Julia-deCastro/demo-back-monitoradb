from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class AddItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    idade = StringField('Idade', validators=[Length(max=50)])
    modalidade = StringField('Modalidade', validators=[Length(max=50)])
