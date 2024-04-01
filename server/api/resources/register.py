from datetime import datetime, timedelta

from flask_restful import Resource, reqparse

from .. import redis_client
from ..models.user import UserModel, db
from ..utils import is_valid_email, send_verification_code, check_password


# 发送验证码资源类
class SendCodeResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='需要提供邮箱')
        # 解析参数
        args = parser.parse_args()
        email = args['email']
        # 检查邮箱是否为空
        if not email:
            return {'message': '邮箱不能为空'}, 400
        # 检查邮箱格式是否正确
        if not is_valid_email(email):
            return {'message': '邮箱格式不正确'}, 400
        # 检查邮箱是否已经存在
        register_user = UserModel.query.filter_by(username=email).first()
        if register_user:
            return {'message': '该邮箱已经存在'}, 409
        # 发送验证码
        code = send_verification_code(email)
        # 使用redis缓存验证码
        redis_client.set(email, code, ex=600)
        return {'message': '邮件发送成功'}, 200


# 用户注册资源类
class RegisterResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='需要提供邮箱')
        parser.add_argument('code', type=str, required=True, help='需要提供验证码')
        parser.add_argument('password', type=str, required=True, help='需要提供密码')
        parser.add_argument('confirmPassword', type=str, required=True, help='需要再次提供密码')
        # 解析参数
        args = parser.parse_args()
        email = args['email']
        code = args['code']
        password = args['password']
        confirmPassword = args['confirmPassword']
        # 缓存验证码
        cache_code = redis_client.get(email)

        # 检查用户名和密码是否为空
        if not email:
            return {'message': '请输入邮箱'}, 400
        if not is_valid_email(email):
            return {'message': '邮箱格式不正确'}, 400
        if not code:
            return {'message': '请输入验证码'}, 400
        if not password:
            return {'message': '请输入密码'}, 400
        if not check_password(password):
            return {'message': '密码需由8位以上、大小写字母、特殊字符组成'}, 400
        if not confirmPassword:
            return {'message': '请再次输入密码'}, 400
        if int(code) != int(cache_code):
            return {'message': '验证码错误'}, 401
        if password != confirmPassword:
            return {'message': '两次密码不一致'}, 401

        # 注册用户
        register_user = UserModel.query.filter_by(username=email).first()
        if register_user:
            return {'message': '邮箱已经存在'}, 409

        createdAt = datetime.utcnow() + timedelta(hours=8)
        newUser = UserModel(username=email, password=password, created_time=createdAt)
        newUser.set_password()
        try:
            db.session.add(newUser)
            db.session.commit()
            return {'message': '用户注册成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('注册用户失败:', str(e))
            return {'message': '注册用户失败', 'error': str(e)}, 500
