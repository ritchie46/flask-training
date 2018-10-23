from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired


class ClassifierForm(FlaskForm):
    sepal_length = DecimalField('Sepal length', validators=[DataRequired()])
    sepal_width = DecimalField('Sepal width', validators=[DataRequired()])
    petal_length = DecimalField('Petal length', validators=[DataRequired()])
    petal_width = DecimalField('Petal width', validators=[DataRequired()])
    button_value = 'Classify'
