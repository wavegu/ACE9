# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
from setuptools import setup, find_packages

setup(
    name="ACE9",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'flask',
        "flask-wtf",
        'flask-mail',
        'flask-login',
        'flask-openid',
        'flask-bcrypt',
        "flask-sqlalchemy",
        'migrate',
        'sqlalchemy-migrate',
    ],
)