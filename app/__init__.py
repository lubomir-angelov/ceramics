from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
app.config['APP_SETTINGS']="config.ProductionConfig"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app import models
from app import config
