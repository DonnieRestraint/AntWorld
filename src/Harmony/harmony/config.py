import redis
import os


class Config(object):
    DEBUG = False
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host:port/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # REDIS配置
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 7
    # session
    SECRET_KEY = "ScholarFlower"
    # flask_session配置
    SESSION_TYPE = "redis"
    SESSION_USER_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 21  # 过期时间
    # 项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/harmony'


class ProductConfig(Config):
    pass


config_dict = {
    'dev': DevelopConfig,
    'pro': ProductConfig
}
