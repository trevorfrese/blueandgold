from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, DecimalField
from wtforms.validators import Required, Length
	
class EditForm(Form):
    listingname = TextAreaField('listingname', validators = [Length(min = 0, max = 140)])
    listingaddress = TextField('',validators = [Length(min = 0, max = 140)])
    lat = DecimalField(places = 6)
    lng = DecimalField(places = 6)
    place = TextAreaField('',validators = [Length(min = 0, max = 140)])