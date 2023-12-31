from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
session = Session()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.static_folder = "../static"
    app.template_folder = "../templates"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbmgt.sqlite"
    app.config["SECRET_KEY"] = '9c97f13c5fd005af6d6090af'

    # Configure Flask-Session to use server-side session storage
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
    session.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    db.init_app(app)

    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .auth import models
    from .main import models

    with app.app_context():
        db.create_all()

    return app
