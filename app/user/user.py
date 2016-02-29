# encoding=utf8
import sys
import json
from app import db
from app import bcrypt

reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

ROLE_USER = 0
ROLE_ADMIN = 1

 
class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    nickname = db.Column(db.String, unique=False, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, nullable=False)
    email_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    # In case we need more info later, we store extensions in json string
    extension = db.Column(db.String, unique=False, nullable=True)

    def __init__(self, email, password, role=ROLE_USER, email_confirmed=False, confirmed_on=None, extension='{}'):
        self.email = email
        self.nickname = email[:email.find('@')]
        self.password = bcrypt.generate_password_hash(password)
        self.role = role
        self.email_confirmed = email_confirmed
        self.confirmed_on = confirmed_on
        self.extension = extension
        self.extend_dict = json.loads(str(self.extension))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
 
    def __repr__(self):
        return '<User %r>' % self.email
