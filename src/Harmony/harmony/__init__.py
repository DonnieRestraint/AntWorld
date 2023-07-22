import os
import logging
from logging.handlers import RotatingFileHandler
import redis
from flask import Flask
from flask import render_template
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from harmony.models import db
from harmony.views_admin import admin_blueprint
from harmony.views_user import user_blueprint


def create_app(config):
    # 创建实例
    app = Flask(__name__, instance_relative_config=True)
    # 配置
    app.config.from_object(config)
    # 初始化数据库连接
    db.init_app(app)
    # 初始化session处理
    Session(app)
    # CSRF保护
    CSRFProtect(app)
    # 初始化Redis连接
    app.redis_client = redis.StrictRedis(config.REDIS_HOST, config.REDIS_PORT, config.REDIS_DB)

    # Test
    @app.route('/')
    def hello():
        return render_template('index.html')
    #
    # # 404的错误处理
    # @app.errorhandler(404)
    # def handle404(e):
    #     return render_template('404.html')

    # 设置日志记录等级
    logging.basicConfig(level=logging.DEBUG)
    # 创建日志文件处理器
    print(config.BASE_DIR + "/logs/harmony.log")
    if "logs" not in os.listdir(config.BASE_DIR):
        os.makedirs(config.BASE_DIR + "/logs/")
    # 1024 * 1024 * 100
    file_log_handler = RotatingFileHandler(config.BASE_DIR + "/logs/harmony.log", maxBytes=1, backupCount=10, mode='a+')
    # 日志记录格式
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为日志处理器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 创建全局日志对象
    # logging.getLogger().addHandler(file_log_handler)
    # app.logger_harmony = logging
    app.logger.addHandler(file_log_handler)

    # 注册蓝图
    app.register_blueprint(user_blueprint)
    return app
