from app import app
from app import mail
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception as e:
        print 'error when confirming token', e
        return False
    return email


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)


if __name__ == '__main__':
    from flask import render_template
    email = '648545255@qq.com'
    # token = generate_confirmation_token(email)
    # confirm_url = '127.0.0.1:5000/confirm/'+token
    # html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = 'test subject'
    send_email(email, subject, '<h1>welcome to flask<h1>')