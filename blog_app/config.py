import os


class Config():
    SQLALCHEMY_DATABASE_URI  = "sqlite:///blog_app.db"
    SECRET_KEY  = "5ntw35eq24eu7oysftbhbncfy6fxdb65bgshwcjtvvd4"
    MAIL_SERVER ='smtp.google.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASS = os.environ.get('EMAIL_PASS')