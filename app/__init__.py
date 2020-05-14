from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.session_protection='strong'
login_manager.login_manager_category = 'info'
db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
ma = Marshmallow()


# from app.models import User

# create an application factory


def create_app(config_name):
    """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set the configurations
    app.config.from_object(config_options[config_name])

    # initialiaze the database
    db.init_app(app)
    #initializing of flask extentions
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)

    # register your blueprints here
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    from .parking import parking as parking_blueprint
    from .admin import admin as admin_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(parking_blueprint,url_prefix='/parking')
    app.register_blueprint(admin_blueprint,url_prefix='/admin')


    return app