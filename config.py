from dotenv import load_dotenv
load_dotenv()

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.getenv('DATABASE_URL')
    # simplemde conf
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # db conf
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    UPLOADED_PHOTOS_DEST ='app/static/images/blog'
    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://joan:Nekoye02@localhost/parking_test"
    DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.getenv('HEROKU_POSTGRESQL_BROWN_URL')
    DEBUG=False
    


config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}