from flask import render_template, url_for, request
from app import app

members = [
        {
            'name': 'Dyani Dillard',
            'headshot': 'static/img/dyani_photo.jpg',
            'title': 'Co-President'
        },
        {
            'name': 'Joey Rose',
            'headshot': 'static/img/joey_photo.jpg',
            'title': 'Co-President'
        },
        {
            'name': 'Scott Morris',
            'headshot': 'static/img/scott_photo.jpeg',
            'title': 'Head of Events'
        },
        {
            'name': 'Tammie Oh',
            'headshot': 'static/img/tammy_photo.JPG',
            'title': 'Marketing & Finance'
        },
        {
            'name': 'Ruth Schlosser',
            'headshot': 'static/img/ruth_photo.jpg',
            'title': 'Head of Projects'
        },
        {
            'name': 'Ali Mian',
            'headshot': 'static/img/ali_photo.jpg',
            'title': 'Local Engagement'
        },
        {
            'name': 'Jasmine Reyes',
            'headshot': 'static/img/jasmine_photo.jpg',
            'title': 'Community Outreach'
        }
    ]

# Main site pages

@app.route('/')
def homepage():
    return render_template('pages/index.html')

@app.route('/about')
def aboutpage():
    return render_template('pages/about.html', members=members)

@app.route('/events')
def eventspage():
    return render_template('pages/events.html')

@app.route('/contact')
def contactpage():
    return render_template('pages/contact.html')

@app.route('/resources')
def resourcespage():
    return render_template('pages/resources.html')

# Static resources

@app.route('/robots.txt')
def robotstxtpage():
    return url_for('static', filename='robots.txt')

@app.route('/favicon.ico')
def faviconpage():
    return url_for('static', filename='favicon.png')

# Error handling

@app.errorhandler(404)
def pagenotfounderror(error):
    return(render_template('error/404.html')) # Return a nice and pretty custom 404 error page