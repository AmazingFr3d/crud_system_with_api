from .. import db
from .. import bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    # salt = db.Column(db.String(128), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        # Generate a random salt
        # salt = bcrypt.gensalt()
        # Combine the password and salt, then hash
        hashed_password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')
        # Save the hashed password and salt
        # self.salt = salt.decode('utf-8')
        self._password = hashed_password

    def __repr__(self):
        return f"<User {self.name}>"

    def check_password_correction(self, attempted_password):
        # Combine the provided password with the stored salt, then hash
        hashed_attempted_password = bcrypt.generate_password_hash(self.salt + attempted_password).decode('utf-8')
        # Compare the hashed passwords
        return bcrypt.check_password_hash(self._password, hashed_attempted_password)
