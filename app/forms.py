from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
# from app.forms import PropertyForm


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    num_of_rooms = StringField('No. of Rooms', validators=[InputRequired()])
    num_of_bathrooms = StringField('No. of bathrooms', validators=[InputRequired()])
    price= StringField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House'),('Apartment')], validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    property_photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images only! (png,jpg)')])