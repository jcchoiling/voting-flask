import os
import logging

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    FLASK_APP = APP_ROOT + 'run.py'
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'voting.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_CONFIRMABLE = False
    CACHE_TYPE = 'simple'
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500
    SUPPORTED_LANGUAGES = {'bg': 'Bulgarian', 'en': 'English', 'fr': 'Francais'}
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///voting.db'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/voting.db'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


config = {
    "development": "voting.config.DevelopmentConfig",
    "testing": "voting.config.TestingConfig",
    "default": "voting.config.DevelopmentConfig"
}



def configure_app(app):
    config_name = os.getenv('VOTING_CONFIGURATION', 'development')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

