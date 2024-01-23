import os

class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///dbmgt.sqlite"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        hostname=os.getenv("DB_HOST"),
        databasename=os.getenv("DB_NAME"),)
    # SQLALCHEMY_DATABASE_URI = "mysql+pymsql://Tolumichael:wS.4j8q9CmXv.!m@http://Tolumichael.mysql.pythonanywhere-services.com/Tolumichael$excel_db"
    SECRET_KEY = '9c97f13c5fd005af6d6090af'
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = '/tmp/flask_session'
    MAIL_SERVER = 'smtp.gmail.com'  # Update with your email provider's SMTP server
    MAIL_PORT = 465
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    # MAIL_USERNAME = ''
    # MAIL_PASSWORD = ''
    # MAIL_DEFAULT_SENDER = ''
