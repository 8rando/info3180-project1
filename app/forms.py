from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class propertytitle(FlaskForm):
    prop_title = StringField('Property Title', validators=[InputRequired()])
    prop_description = TextAreaField('prop_description', validators=[InputRequired()])
    num_of_rooms = StringField('No. of num_of_rooms', validators=[InputRequired()])
    num_of_bathrooms = StringField('No. of num_of_bathrooms', validators=[InputRequired()])
    price= StringField('Price', validators=[InputRequired()])
    proptype = SelectField('Property Type', choices=[('House'),('Apartment')], validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    property_photo = FileField('property_photo', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images only! (png,jpg)')])
