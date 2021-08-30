import os
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '3965a27bdf5ba755566e64e65c690aef'
    #SQLALCHEMY_DATABASE_URI = "postgres://irqtlwyphuuoqn:1833a784173005e27184c8b1f7232b5d9f9a8c033355b9cf2460dd52381faa09@ec2-50-17-255-244.compute-1.amazonaws.com:5432/dbbdtgt7l6mgm3"
    DATABASE_URL = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = "postgresql://ceramics:DYC42S3BVZjyrylfcCD0@localhost/GK_Pottery"

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')


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