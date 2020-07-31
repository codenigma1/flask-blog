from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Database and secret key config.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c22e7255acbc6f0b7d48270d303456f3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # we are passing function name of routes
login_manager.login_message_category = 'info'



from flaskblog import routes
