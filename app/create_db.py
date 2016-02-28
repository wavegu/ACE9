# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
from migrate.versioning import api
from migrate.exceptions import DatabaseAlreadyControlledError
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path


def create_db():
    try:
        db.create_all()
        if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
            api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    except DatabaseAlreadyControlledError:
        print 'sqldb alread exists'

db.create_all()