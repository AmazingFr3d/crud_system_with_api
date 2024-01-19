class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///dbmgt.sqlite"
    SECRET_KEY = '9c97f13c5fd005af6d6090af'
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = '/tmp/flask_session'
    MAIL_SERVER = 'smtp.gmail.com'  # Update with your email provider's SMTP server
    MAIL_PORT = 465
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'techredy@gmail.com'
    MAIL_PASSWORD = 'Fr3d4ali4i'
    MAIL_DEFAULT_SENDER = 'techredy@gmail.com'
