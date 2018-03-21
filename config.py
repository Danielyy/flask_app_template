import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qiye.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
    #     ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'lmlc@easecreate.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'need_change_password')
    FLASKY_MAIL_SUBJECT_PREFIX = '[立马理财]'
    FLASKY_MAIL_SENDER = 'Admin <lmlc@easecreate.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN', 'yangyi@easecreate.com')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class MySQLProductionConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://root:yzskynet@127.0.0.1/my_db?charset=utf8'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': MySQLProductionConfig
}
