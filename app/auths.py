#Oauth stuff for Facebook login
from flask_oauth import OAuth
oauth = OAuth()
GOOGLE_CLIENT_ID = '838957747084-cg799md78hdt3tn51rq5tnl8fl9bsme7.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = ''

FACEBOOK_KEY = '728516440523822'
FACEBOOK_SECRET = '755e333aa52e140fec75b70d01dc032f'
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_KEY,
    consumer_secret=FACEBOOK_SECRET,
    request_token_params={'scope': 'email'}
)
'''
google = oauth.remote_app('google',
	base_url='https://www.google.com/accounts/',
	authorize_url='https://accounts.google.com/o/oauth2/auth',
	request_token_url=None,
	request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email','response_type': 'code'},
	access_token_url='https://accounts.google.com/o/oauth2/token',
	access_token_method='POST',
	access_token_params={'grant_type': 'authorization_code'},
	consumer_key=GOOGLE_CLIENT_ID,
	consumer_secret=GOOGLE_CLIENT_SECRET)
'''