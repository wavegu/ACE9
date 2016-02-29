# encoding=utf8
import sys

from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from config import DB_DIR


reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
 
app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.user import views