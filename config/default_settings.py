import os


uri = os.getenv('SQLALCHEMY_DATABASE_URI',
                'postgresql://postgres:1234@db/miso_db')


class Config(object):
    TESTING = False
    DEVICE_HOST = "http://devices:3040"
    SQLALCHEMY_DATABASE_URI = uri
    JWT_SECRET_KEY = 'secret-word'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
