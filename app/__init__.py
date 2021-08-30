from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config["SECRET_KEY"] = '3965a27bdf5ba755566e64e65c690aef'
app.config['APP_SETTINGS']="config.ProductionConfig"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ceramics:DYC42S3BVZjyrylfcCD0@localhost/GK_Pottery'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://irqtlwyphuuoqn:1833a784173005e27184c8b1f7232b5d9f9a8c033355b9cf2460dd52381faa09@ec2-50-17-255-244.compute-1.amazonaws.com:5432/dbbdtgt7l6mgm3"
app.config['DATABASE_URL'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app import models
from app import config
