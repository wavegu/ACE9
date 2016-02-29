# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

from app import app
from app import db
from config import SERVER_IP
from config import SERVER_PORT
from user.user import User
from user.user import ROLE_USER


def update_db():
    db.create_all()


if __name__ == '__main__':
    update_db()
    app.run(debug=True, host=SERVER_IP, port=SERVER_PORT)