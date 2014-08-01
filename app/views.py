from flask import render_template, flash, redirect, url_for, session, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm
from auths import facebook
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Home')

@app.route('/map')
def map():
     # creating a map in the view
    return render_template('map.html')
    #return render_template("map.html")

@app.route('/login')
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    else:    
        return render_template('login.html', 
        title = 'Sign In')

#put this on a button
@app.route('/fblogin')
def fblogin():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

#this method is post authorization, takes all the data, creates a user
#store in db only if user is not already in, 
@app.route('/fblogin/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    session['oauth_token'] = (resp['access_token'], '')

    me = facebook.get('/me')

    user = User.query.filter_by(fbid = me.data['id']).first()
    if user is None:
        user = User(name= me.data['name'], fbid = me.data['id'] ,firstname = me.data['first_name'],
        lastname = me.data['last_name'],email= me.data['email'],role = 0)

        db.session.add(user)
        db.session.commit()
    
    login_user(user)
    return render_template("loggedin.html", name = me.data['name'])

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))