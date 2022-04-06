import os


uri = os.getenv('SQLALCHEMY_DATABASE_URI',
                'postgresql://postgres:123456@localhost/miso')


class Config(object):
    TESTING = False
    DEVICE_HOST = "http://devices:3040"
    SQLALCHEMY_DATABASE_URI = uri
    JWT_SECRET_KEY = 'secret-word'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
