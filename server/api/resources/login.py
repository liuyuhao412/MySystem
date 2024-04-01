from datetime import datetime, timedelta

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from ..models.user import UserModel, LoginLogModel, db


# 用户登录资源类
class LoginResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='需要提供用户名')
        parser.add_argument('password', type=str, required=True, help='需要提供密码')
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        # 检查用户名和密码是否为空
        if not username:
            return {'message': '用户名不能为空'}, 400
        if not password:
            return {'message': '密码不能为空'}, 400
        # 查找用户
        user = UserModel.query.filter_by(username=username).first()
        # 用户或密码错误
        if not user or not user.check_password(password):
            return {'message': '用户名或密码错误'}, 401
        # 用户存在且密码匹配，则生成访问令牌
        token = create_access_token(identity=user.user_id)
        role = user.role
        # 编写登录日志
        ip = request.headers.get('X-Forwarded-For')
        if not ip:
            ip = request.remote_addr
        login_time = datetime.utcnow() + timedelta(hours=8)
        LoginLog = LoginLogModel(user_id=user.user_id, username=user.username, role=role, login_time=login_time, ip=ip)
        db.session.add(LoginLog)
        db.session.commit()
        return {'message': '登录成功', 'token': token, 'role': role, 'username': username}, 200


class UpdatePasswordResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='需要提供用户名')
        parser.add_argument('newPassword', type=str, required=True, help='需要提供密码')
        parser.add_argument('confirmPassword', type=str, required=True, help='需要提供密码')
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        newPassword = args['newPassword']
        confirmPassword = args['confirmPassword']
        if not newPassword:
            return {'message': '请输入密码'}, 400
        if not confirmPassword:
            return {'message': '请再次输入密码'}, 400
        if newPassword != confirmPassword:
            return {'message': '两次密码不一致'}, 401
        user = UserModel.query.filter_by(username=username).first()
        user.password = newPassword
        user.set_password()
        try:
            # 提交事务
            db.session.commit()
            return {'message': '修改密码成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('修改密码失败:', str(e))
            return {'message': '修改密码失败', 'error': str(e)}, 500
