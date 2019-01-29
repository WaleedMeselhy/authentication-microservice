from flask_env import MetaFlaskEnv


class BaseConfig(metaclass=MetaFlaskEnv):
    ENV_PREFIX = ''
    ENV_LOAD_ALL = False

    JWT_PRIVATE_KEY = None
    JWT_PUBLIC_KEY = None
    JWT_ALGORITHM = None


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class StagingConfig(BaseConfig):
    """Staging configuration"""
    DEBUG = False


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
