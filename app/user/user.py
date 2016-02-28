# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
from app import db
from app import bcrypt
 
ROLE_USER = 0
ROLE_ADMIN = 1

 
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, paid=False, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.admin = admin

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
