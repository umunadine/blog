from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import DevConfig

app = Flask(__name__, instance_relative_config = True)
app.config.from_object(DevConfig)


app.config['SECRET_KEY'] = 'a74aba664f8b43bc68daa3d694ecf909'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes