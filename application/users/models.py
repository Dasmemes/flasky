import datetime
from application import db, flask_bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):

    # Primary key for each user record
    id = db.Column(db.Integer, primary_key=True)

    # Unique email for each user record
    email = db.Column(db.String(255), unique=True)

    # Unique username for each user record
    username = db.Column(db.String(40), unique=True)

    # Hashed password for the user
    _password = db.Column('password', db.String(60))

    # Date/time that the user account was created on
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = flask_bcrypt.generate_password_hash(password)

    def __repr__(self):
        return self.username

    def is_authenticated(self):
        """All our registered users are authenticated"""
        return True

    def is_active(self):
        """All our users are active"""
        return True

    def is_anonymous(self):
        """We don't allow non authenticated users"""
        return False

    def get_id(self):
        """Get the user ID as unicode string"""
        return str(self.id)
