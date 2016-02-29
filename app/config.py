# encoding=utf8
import os
from os.path import join
from os.path import abspath
from util import create_dir_if_not_exist
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


# server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000


# CSRF
CSRF_ENABLED = True
SECRET_KEY = 'CSSUNB'
SECURITY_PASSWORD_SALT = 'CSSUNB23333'

# database

DB_DIR = join(abspath(os.path.dirname(__file__)), 'db')
create_dir_if_not_exist(DB_DIR)

APP_DB = 'ACE.db'
TEST_DB = 'test'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = join(DB_DIR, 'db_repo')
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (join(DB_DIR, APP_DB))


# mail settings

MAIL_SERVER = 'smtp.126.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False

MAIL_USERNAME = ''
MAIL_PASSWORD = ''

MAIL_DEFAULT_SENDER = ''


# openid
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myoopenid.com'}
]