from flask_restful import Resource
from sqlalchemy import func

from .. import db
from ..models.user import UserModel, LoginLogModel


class GetUserCountResource(Resource):
    @staticmethod
    def get():
        query = UserModel.query.filter_by()
        count = query.count()
        return {'count': count}, 200


class GetUserLogCountResource(Resource):
    @staticmethod
    def get():
        query = LoginLogModel.query.filter_by()
        count = query.count()
        return {'count': count}, 200


class GetUserListResource(Resource):
    @staticmethod
    def get():
        all_months = list(range(1, 13))
        user_count_by_month = (db.session.query(func.extract('month', UserModel.created_time).label('month'),
                                                func.count().label('user_count')).filter().group_by(
            func.extract('month', UserModel.created_time)).all())

        user_counts_dict = {month: count for month, count in user_count_by_month}
        user_list = [(month - 1, user_counts_dict.get(month, 0)) for month in all_months]
        return {'user_list': user_list}, 200


class GetUserLogResource(Resource):
    @staticmethod
    def get():
        all_months = list(range(1, 13))
        Log_count_by_month = (db.session.query(func.extract('month', LoginLogModel.login_time).label('month'),
                                               func.count().label('user_count')).filter().group_by(
            func.extract('month', LoginLogModel.login_time)).all())

        Log_counts_dict = {month: count for month, count in Log_count_by_month}
        log_list = [(month - 1, Log_counts_dict.get(month, 0)) for month in all_months]
        return {'log_list': log_list}, 200
