"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, send_from_directory
from python_webapp_flask import app


# @app.route('/')
# @app.route('/home')
# def home():
#     """Renders the home page."""
#     return render_template(
#         'index.html',
#         title='Home Page',
#         year=datetime.now().year,
#     )

# @app.route('/contact')
# def contact():
#     """Renders the contact page."""
#     return render_template(
#         'contact.html',
#         title='Contact',
#         #year=datetime.now().year,
#         year=datetime.now().year,
#         message='Your contact page.'
#     )

# @app.route('/about')
# def about():
#     """Renders the about page."""
#     return render_template(
#         'about.html',
#         title='About',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )

@app.route('/')
def hello():
    title = "ExxonMobil"
    return render_template('angular_site.html', title=title)

@app.route('/angular')
def angular_site():
    """Renders the about page."""
    return render_template(
        'angular_site.html',
        title='ExxonMobil',
        message='Your application description page.'
    )

@app.route('/assets/<path:path>')
def send_assets(path):
    # import pdb; pdb.set_trace()
    return send_from_directory('static/angular/assets/', path)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('angular_site.html'), 404