# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True
from app import db
from app import app
from app import mail
from app import bcrypt
from app import login_manager
from forms import LoginForm
from forms import RegisterForm
from user.user import User
from user.user import ROLE_USER
from flask import render_template
from flask import g
from flask import flash
from flask import session
from flask import url_for
from flask import request
from flask import redirect
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You registered and are now logged in. Welcome!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('User not exist...', 'danger')
            return render_template('login.html', form=form)
        if bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid  password.', 'danger')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
