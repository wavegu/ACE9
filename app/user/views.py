# encoding=utf8
import sys
import datetime
from app import db
from app import app
from app import mail
from app import bcrypt
from app import login_manager
from forms import LoginForm
from forms import RegisterForm
from user import User
from user import ROLE_USER
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
from email_confirm import send_email
from email_confirm import confirm_token
from email_confirm import generate_confirmation_token

reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    current_user_email = request.cookies.get('current_user_email')
    if not current_user_email:
        return redirect(url_for('login'))
    user = User.query.filter_by(email=current_user_email).first()
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
        print form.data
        user = User(
            email=form.email.data,
            password=form.password.data,
            email_confirmed=False,
            extension='{}'
        )
        db.session.add(user)
        db.session.commit()

        target = redirect(url_for('index', user_id=user.id))
        response = app.make_response(target)
        response.set_cookie('current_user_email', value=user.email)

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)
        flash('You registered and are now logged in. Welcome!', 'success')

        return response
    return render_template('user/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('User not exist...', 'danger')
            return render_template('user/login.html', form=form)
        if bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            target = redirect(url_for('index', user_id=user.id))
            response = app.make_response(target)
            response.set_cookie('current_user_email', value=user.email)
            return response
        else:
            flash('Invalid  password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/confirm/<token>')
@login_required
def confirm_email(token):
    email = ''
    try:
        email = confirm_token(token)
    except Exception as e:
        flash('The confirmation link is invalid or has expired.' + str(e), 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.email_confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.email_confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index'))
