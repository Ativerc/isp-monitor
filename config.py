# For selecting dev or prod. Dunno if this is the right way.

import os

CONFIG_FILE_NAME = ".isp-monitor_config.yaml"

class Base():
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Base):
    DEBUG = True
    DEVELOPMENT = True
    CONFIG_URI = os.path.join(os.getcwd(), CONFIG_FILE_NAME)

class TestingConfig(Base):
    DEBUG = False
    TESTING = True
    CONFIG_URI = os.path.join(os.getcwd(), CONFIG_FILE_NAME)

class ProductionConfig(Base):
    DEBUG = False
    TESTING = False
    CONFIG_URI = os.path.join(os.path.expanduser('~'), CONFIG_FILE_NAME)
