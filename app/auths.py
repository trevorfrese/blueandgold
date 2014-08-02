#Oauth stuff for Facebook login
from flask_oauth import OAuth
oauth = OAuth()
GOOGLE_CLIENT_ID = '838957747084-cg799md78hdt3tn51rq5tnl8fl9bsme7.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = ''

FACEBOOK_KEY = '577704639005531'
FACEBOOK_SECRET = '9d844c13a7c906b8042df4df0028dc31'

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

# Use Twitter as example remote application
twitter = oauth.remote_app('twitter',
    # unless absolute urls are used to make requests, this will be added
    # before all URLs. This is also true for request_token_url and others.
    base_url='https://api.twitter.com/1/',
    # where flask should look for new request tokens
    request_token_url='https://api.twitter.com/oauth/request_token',
    # where flask should exchange the token with the remote application
    access_token_url='https://api.twitter.com/oauth/access_token',
    # twitter knows two authorizatiom URLs. /authorize and /authenticate.
    # they mostly work the same, but for sign on /authenticate is
    # expected because this will give the user a slightly different
    # user interface on the twitter side.
    authorize_url='https://api.twitter.com/oauth/authenticate',
    # the consumer keys from the twitter application registry.
    consumer_key='JcjawyfmbFEQD13Iz9SGX3Y2l',
    consumer_secret='QBIJenXb5Iv5I1YDgykylzcpwF1PesYo9c3ZufMWakN35jlmGL'
)