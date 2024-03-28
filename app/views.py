"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory, sessions
from app.models import Property
from app.forms import propertytitle
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

"""routes to implement 
1/ /properties/create : form to add new house
2. /properties  : list all propeties in the database
3. /properties/<propertyid>   : viewing individual property"""

@app.route('/property/create', methods =['POST', 'GET']) #route to create form
def create(): #view function to the create property form
    form = propertytitle()

    if request.method =='POST':
        if form.validate_on_submit():
            prop_title = form.prop_title.data
            prop_description = form.prop_description.data
            num_of_rooms = form.num_of_rooms.data
            num_of_bathrooms =form.num_of_bathrooms.data
            price = form.price.data
            proptype = form.proptype.data
            location = form.location.data
            property_photo = form.property_photo.data
            filename= secure_filename(property_photo.filename)
            newlisting= Property(prop_title, prop_description, num_of_rooms, num_of_bathrooms, price, proptype,location, filename)
            db.session.add(newlisting)
            db.session.commit()
            property_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('This property has been saved successfully','Success')
            return redirect(url_for('property'))
    return render_template('addprop.html', form=form)

def get_uploaded_image():
    uploads_dir = os.path.join(app.config['UPLOAD_FOLDER'])
    uploaded_images = [f for f in os.listdir(uploads_dir) if os.path.isfile(os.path.join(uploads_dir, f))]
    return uploaded_images

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/properties")
def property():
    prope= Property.query.all()
    return render_template('allproperties.html', prope=prope)

@app.route('/properties/<propertyid>')
def eachproperty(propertyid):
    """Render the websites view property pages."""
    prop = Property.query.filter_by(id=propertyid).first()
    return render_template('eachproperty.html', prop=prop) 
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
