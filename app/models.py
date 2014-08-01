from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    fbid = db.Column(db.String(64), unique = True)
    firstname = db.Column(db.String(32), unique = True)
    lastname = db.Column(db.String(32), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    markers = db.relationship('Marker', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Marker(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), index = True, unique = True)
    address = db.Column(db.String(80), index = True, unique = True)
    lat = db.Column(db.Float(precision=6))
    lng = db.Column(db.Float(precision=6))
    place = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Marker %r>' % (self.name)
