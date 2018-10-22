import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}