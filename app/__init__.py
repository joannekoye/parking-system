from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
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
    bootstrap.init_app(app)

    # register your blueprints here
    # from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint
    from .parking import parking as parking_blueprint
    from .admin import admin as admin_blueprint
    

    # app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(parking_blueprint)
    app.register_blueprint(admin_blueprint,url_prefix='/admin')


    return app