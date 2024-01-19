from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
from flask_restful import Api
from flask_mail import Mail
from .config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
session = Session()
restful_api = Api()
mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.static_folder = "../static"
    app.template_folder = "../templates"

    # Configure Flask-Session to use server-side session storage
    mail.init_app(app)
    session.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    restful_api.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .auth import models
    from .main import models

    with app.app_context():
        db.create_all()

    return app


from .api.resources import MembersResource

restful_api.add_resource(MembersResource, '/api/ktr')
