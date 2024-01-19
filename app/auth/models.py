from flask import current_app
from .. import db
from .. import bcrypt, login_manager
from flask_login import UserMixin
import datetime
import secrets


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    reset_token = db.Column(db.String(32), nullable=True)
    reset_token_expiration = db.Column(db.DateTime, nullable=True)

    def generate_reset_token(self):
        self.reset_token = secrets.token_urlsafe(16)
        self.reset_token_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    def __repr__(self):
        return f"<User {self.name}>"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
