# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

from app import app
from app import db

db.create_all()
app.run(debug=True)