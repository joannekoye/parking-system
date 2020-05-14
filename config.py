 
import os


class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:alex@localhost/tests'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']




class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG')


class TestingConfig(Config):
    TESTING = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig
}