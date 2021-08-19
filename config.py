import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    DEBUG = True
    DATABASE = os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    DATABASE = 'sqlite://'

class ProductionConfig(Config):
    os.path.join(basedir, 'data.sqlite')
    SECRET_KEY = os.environ.get('SECRET_KEY')


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
