import os

SECRET_KEY = os.environ.get('SECRET_KEY')
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')