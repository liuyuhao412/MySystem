from flask_restful import Resource, reqparse

from .. import db
from ..models.user import LoginLogModel


class GetLogResource(Resource):
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
        query = LoginLogModel.query
        if username != '':
            query = query.filter(LoginLogModel.username.like('%{username}%'.format(username=username)))
        if role != '':
            query = query.filter(LoginLogModel.role.like('%{role}%'.format(role=role)))
        count = query.count()  # 符合条件的记录总数
        pagination = query.paginate(page=page, per_page=limit, error_out=False)
        logs = pagination.items
        data = [log.to_json() for log in logs]
        return {'count': count, 'data': data}, 200


class DeleteLogResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('log_id', type=int, required=False)
        # 解析参数
        args = parser.parse_args()
        log_id = args['log_id']
        log = LoginLogModel.query.filter_by(log_id=log_id).first()
        try:
            db.session.delete(log)
            # 提交事务
            db.session.commit()
            return {'message': '日志删除成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('删除用户失败:', str(e))
            return {'message': '日志删除失败', 'error': str(e)}, 500

# from datetime import datetime, timedelta
#
# from flask_restful import Resource, reqparse
#
# from .. import db
# from ..models.user import UserModel
#
#
# class GetUserResource(Resource):
#     @staticmethod
#     def post():
#         parser = reqparse.RequestParser()
#         parser.add_argument('page', type=int, required=False)
#         parser.add_argument('limit', type=int, required=False)
#         parser.add_argument('username', type=str, required=False)
#         parser.add_argument('role', type=str, required=False)
#         # 解析参数
#         args = parser.parse_args()
#         page = args['page']
#         limit = args['limit']
#         username = args['username']
#         role = args['role']
#
#         if not username:
#             username = ''
#         if not role:
#             role = ''
#         query = UserModel.query
#         if username != '':
#             query = query.filter(UserModel.username.like('%{username}%'.format(username=username)))
#         if role != '':
#             query = query.filter(UserModel.role.like('%{role}%'.format(role=role)))
#         count = query.count()  # 符合条件的记录总数
#         pagination = query.paginate(page=page, per_page=limit, error_out=False)
#         users = pagination.items
#         data = [user.to_json() for user in users]
#         return {'count': count, 'data': data}, 200
#
# class DeleteUserResource(Resource):
#     @staticmethod
#     def post():
#         parser = reqparse.RequestParser()
#         parser.add_argument('user_id', type=int, required=False)
#         # 解析参数
#         args = parser.parse_args()
#         user_id = args['user_id']
#         user = UserModel.query.filter_by(user_id=user_id).first()
#         login_logs = user.login_logs
#         try:
#             # 删除用户的所有登录日志
#             for log in login_logs:
#                 db.session.delete(log)
#
#             # 删除用户
#             db.session.delete(user)
#
#             # 提交事务
#             db.session.commit()
#             return {'message': '用户删除成功'}, 200
#         except Exception as e:
#             db.session.rollback()
#             print('删除用户失败:', str(e))
#             return {'message': '删除用户失败', 'error': str(e)}, 500
