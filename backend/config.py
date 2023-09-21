import os
basedir = os.path.abspath(os.path.dirname(__file__))
from datetime import timedelta

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    REDIS_URL = "redis://localhost:6379"
    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 9
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0

class LocalDevementConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///datbase.sqlite3'
    JWT_SECRET_KEY = 'super-secret' 
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    WTF_CSRF_ENABLED = False
    SECURITY_FRESHNESS = timedelta(minutes=30)
    SECURITY_FRESHNESS_GRACE_PERIOD = timedelta(minutes=5)
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    REDIS_URL = "redis://localhost:6379"
    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 9
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0