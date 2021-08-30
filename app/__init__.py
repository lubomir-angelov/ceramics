from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config["SECRET_KEY"] = '3965a27bdf5ba755566e64e65c690aef'
app.config['APP_SETTINGS']="config.ProductionConfig"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ceramics:DYC42S3BVZjyrylfcCD0@localhost/GK_Pottery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app import models
from app import config
