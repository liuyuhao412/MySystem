import redis
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from .config import Config

# 连接redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()


def create_app():
    # 创建 Flask 应用程序实例
    app = Flask(__name__)
    # 从配置文件加载配置
    app.config.from_object(Config)

    # 初始化数据库
    db.init_app(app)

    # 初始化令牌
    jwt.init_app(app)

    # 初始化邮箱
    mail.init_app(app)

    # 初始化 Restful API
    api = Api(app)

    # 注册 API 资源
    from .resources.route import register_routes
    register_routes(api)

    return app
