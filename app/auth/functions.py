from flask_mail import Message, Mail
from flask import current_app, url_for
from .. import mail


def send_password_reset_email(to_email, reset_token):
    subject = 'Password Reset Request'
    body = f"Click the following link to reset your password: {url_for('auth.reset_password', token=reset_token, _external=True)}"

    message = Message(subject, recipients=[to_email], body=body)

    try:
        mail.send(message)
    except Exception as e:
        # Handle email sending errors
        print(f"Error sending email: {str(e)}")


