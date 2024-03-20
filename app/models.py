import unicodedata
from . import db


class Property(db.Model):
    
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    num_of_rooms = db.Column(db.String(10))
    num_of_bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    location= db.Column(db.String(80))
    property_photo= db.Column(db.String(255))

    def __init__(self, title, description, num_of_rooms, num_of_bathrooms, price, property_type, location,property_photo):
       self.title= title
       self.description=description
       self.num_of_rooms= num_of_rooms
       self.num_of_bathrooms = num_of_bathrooms
       self.price = price
       self.property_type= property_type
       self.location= location
       self.property_photo= property_photo

    def get_id(self):
        try:
            return unicodedata(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.propertytitle)