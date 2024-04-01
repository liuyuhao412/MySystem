from datetime import datetime, timedelta

from flask_restful import Resource, reqparse

from .. import db
from ..models.user import UserModel


class GetUserResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=False)
        parser.add_argument('limit', type=int, required=False)
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('role', type=str, required=False)
        # 解析参数
        args = parser.parse_args()
        page = args['page']
        limit = args['limit']
        username = args['username']
        role = args['role']

        if not username:
            username = ''
        if not role:
            role = ''
        query = UserModel.query
        if username != '':
            query = query.filter(UserModel.username.like('%{username}%'.format(username=username)))
        if role != '':
            query = query.filter(UserModel.role.like('%{role}%'.format(role=role)))
        count = query.count()  # 符合条件的记录总数
        pagination = query.paginate(page=page, per_page=limit, error_out=False)
        users = pagination.items
        data = [user.to_json() for user in users]
        return {'count': count, 'data': data}, 200


class AddUserResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('role', type=str, required=False)
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        role = args['role']
        if not username:
            return {'message': '请输入用户名'}, 400
        if not role:
            return {'message': '请选择角色'}, 400
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return {'message': '用户名已经存在'}, 409

        new_password = "Xxx@123456."
        register_time = datetime.utcnow() + timedelta(hours=8)
        user = UserModel(username=username, password=new_password, role=role, created_time=register_time)
        user.set_password()
        try:
            db.session.add(user)
            db.session.commit()
            return {'message': '添加用户成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('添加用户失败:', str(e))
            return {'message': '添加用户失败', 'error': str(e)}, 500


class UpdateUserResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=False)
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('role', type=str, required=False)
        # 解析参数
        args = parser.parse_args()
        user_id = args['user_id']
        username = args['username']
        role = args['role']
        if not username:
            return {'message': '请输入用户名'}, 400
        user = UserModel.query.filter_by(user_id=user_id).first()
        login_logs = user.login_logs
        for log in login_logs:
            log.username = username
            log.role = role
        user.username = username
        user.role = role
        try:
            db.session.commit()
            return {'message': '修改用户成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('删除用户失败:', str(e))
            return {'message': '修改用户失败', 'error': str(e)}, 500


class DeleteUserResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=False)
        # 解析参数
        args = parser.parse_args()
        user_id = args['user_id']
        user = UserModel.query.filter_by(user_id=user_id).first()
        login_logs = user.login_logs
        try:
            # 删除用户的所有登录日志
            for log in login_logs:
                db.session.delete(log)

            # 删除用户
            db.session.delete(user)

            # 提交事务
            db.session.commit()
            return {'message': '删除用户成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('删除用户失败:', str(e))
            return {'message': '删除用户失败', 'error': str(e)}, 500


class SetPasswordResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=False)

        # 解析参数
        args = parser.parse_args()
        user_id = args['user_id']
        user = UserModel.query.filter_by(user_id=user_id).first()
        user.password = 'Xxx@123456.'
        user.set_password()
        try:
            db.session.commit()
            return {'message': '重置密码成功'}
        except Exception as e:
            db.session.rollback()
            print('重置密码失败:', str(e))
            return {'message': '重置密码失败', 'error': str(e)}, 500
