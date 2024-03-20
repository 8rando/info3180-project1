import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory, sessions
from app.models import Property
from app.forms import PropertyForm
from werkzeug.utils import secure_filename



"""routes to implement 
1/ /properties/create : form to add new house
2. /properties  : list all propeties in the database
3. /properties/<propertyid>   : viewing individual property"""


@app.route('/properties/create', methods=['POST','GET'])
def create_properties():
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            num_of_rooms = form.num_of_rooms.data
            num_of_bathrooms = form.num_of_bathrooms.data
            price = form.price.data
            property_type= form.property_type.data
            location = form.location.data
            property_photo = form.property_photo.data
            filename = secure_filename(property_photo.filename)
            newListing = Property(title,description,num_of_rooms,num_of_bathrooms,price, property_type, location, filename)
            db.session.add(newListing)
            db.session.commit()
            property_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('This property has been saved successfully','Success')
            return redirect(url_for('property'))
    return render_template('propertyadd.html',form =form) #make propertyadd.html m8 

@app.route('/properties')
def property():
    propertys = Property.query.all()
    return render_template('allproperties.html', propertys = propertys)

@app.route('/properties/<int:property_id>')
def property_detail(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('property_detail.html', property=property)

       

def get_uploaded_image():
    uploads_dir = os.path.join(app.config['UPLOAD_FOLDER'])
    uploaded_images = [f for f in os.listdir(uploads_dir) if os.path.isfile(os.path.join(uploads_dir, f))]
    return uploaded_images


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




@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route('/files')
def files():
    images = get_uploaded_image()
    return render_template('files.html', images = images)



