from flask_restful import Resource, reqparse

from .. import db
from ..models.user import CalendarModel, CardRecordModel, UserModel


class AdminGetRecordResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('page', type=int, required=False)
        parser.add_argument('limit', type=int, required=False)
        parser.add_argument('month', type=str, required=False)
        parser.add_argument('day', type=str, required=False)
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        page = args['page']
        limit = args['limit']
        month = args['month']
        day = args['day']
        # 用0代表空值
        if not month:
            month = 0
        if not day:
            day = 0
        if not username:
            username = ''

        users = UserModel.query
        users = users.filter(UserModel.username.like('%{username}%'.format(username=username))).all()
        users_ids = [user.user_id for user in users]

        calendars = CalendarModel.query
        if month != 0:
            calendars = calendars.filter_by(month=month)
        if day != 0:
            calendars = calendars.filter_by(day=day)
        calendars = calendars.all()

        # 获取符合条件的日历记录的 calendar_id 列表
        calendar_ids = [calendar.calendar_id for calendar in calendars]

        # 根据 calendar_id 查询对应的打卡记录 ,in_ 函数接受一个可迭代对象作为参数，返回一个条件表达式
        card_records = CardRecordModel.query.filter(CardRecordModel.calendar_id.in_(calendar_ids),
                                                    CardRecordModel.user_id.in_(users_ids))

        # 符合条件的记录总数
        count = card_records.count()
        pagination = card_records.paginate(page=page, per_page=limit, error_out=False)
        records = pagination.items
        data = [record.to_json() for record in records]
        return {'count': count, 'data': data}, 200


class AdminDeleteRecordResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('record_id', type=int, required=False)
        # 解析参数
        args = parser.parse_args()
        record_id = args['record_id']
        record = CardRecordModel.query.filter_by(record_id=record_id).first()
        try:
            db.session.delete(record)
            db.session.commit()
            return {'message': '删除记录成功'}, 200
        except Exception as e:
            db.session.rollback()
            print('删除用户失败:', str(e))
            return {'message': '删除记录失败', 'error': str(e)}, 500
