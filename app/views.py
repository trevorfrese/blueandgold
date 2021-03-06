from flask import render_template, flash, redirect, url_for, session, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from auths import facebook, twitter
from models import User, ROLE_USER, ROLE_ADMIN
from forms import EditForm

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

@app.route('/map', methods = ['GET', 'POST'])
@login_required
def map():
     # creating a map in the view
    form = EditForm()
    '''render_template('map.html',form = form)
    if form.validate_on_submit():
        #g.user.about_me = form.about_me.data
        #db.session.add(g.user)
        #db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('map'))
    else:
        #form.nickname.data = g.user.nickname
        #form.about_me.data = g.user.about_me
        flash('nothing happened')
    '''
    return render_template('map.html',form = form)

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

    user = User.query.filter_by(auth_id = me.data['id']).first()
    if user is None:
        user = User(name= me.data['name'], auth_id = me.data['id'], 
            email= me.data['email'], role = 0)
        db.session.add(user)
        db.session.commit()

    
    login_user(user)
    return render_template("loggedin.html", name = me.data['name'])

@app.route('/tweetlogin')
def tweetlogin():
    return twitter.authorize(callback=url_for('tweet_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@twitter.authorized_handler
def tweet_authorized(resp):

    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    user = User.query.filter_by(auth_id=resp['id']).first()
     # user never signed on
    if user is None:
        user = User(name= resp['name'], auth_id = resp['id'], 
            email= resp['email'], role = 0)
        db.session.add(user)
        db_session.commit()
  
    
    #session['user_id'] = user.id
    flash('You were signed in')
    return redirect(next_url)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@twitter.tokengetter
def get_twitter_token():
    user = g.user
    if user is not None:
        return user.oauth_token, user.oauth_secret

