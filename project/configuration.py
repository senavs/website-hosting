import os
from abc import ABC

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASE_URL = os.environ.get('DATABASE_URL', os.path.join(BASE_DIR, 'database', 'sqlite', 'hopedar-dev.sqlite'))


class ConfigBase(ABC):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'simplest secrete key')


class DevelopmentConfig(ConfigBase):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(ConfigBase):
    ENV = 'production'
    DEBUG = False


CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
