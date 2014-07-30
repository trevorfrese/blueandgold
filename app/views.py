from flask import render_template
from app import app
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Trevor' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/map')
def map():
     # creating a map in the view
    return render_template('map.html')
    #return render_template("map.html")

