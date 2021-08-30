import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '3965a27bdf5ba755566e64e65c690aef'
    SQLALCHEMY_DATABASE_URI = "postgresql://ceramics:DYC42S3BVZjyrylfcCD0@localhost/GK_Pottery"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True