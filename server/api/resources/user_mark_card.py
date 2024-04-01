from datetime import datetime

from flask_restful import Resource, reqparse

from .. import db
from ..models.user import UserModel, CardRecordModel, CalendarModel


class GetMarkCardInfoResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('date', type=str, required=True)

        # 解析参数
        args = parser.parse_args()
        username = args['username']
        date = args['date']
        # 处理数据
        try:
            # 解析日期
            # 日期
            today_date = datetime.strptime(date, '%Y年%m月%d日').date()
            # 周
            weekday = today_date.weekday()
            day_of_week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][weekday]
            # 年
            year = today_date.year
            # 月
            month = today_date.month
            # 日
            day = today_date.day
            calendar = CalendarModel.query.filter_by(date=today_date).first()
            if not calendar:
                calendar = CalendarModel(date=today_date, day_of_week=day_of_week, year=year, month=month, day=day)
                db.session.add(calendar)
                db.session.commit()
            # 查询用户
            user = UserModel.query.filter_by(username=username).first()
            # 查询用户今天的打卡记录
            record = CardRecordModel.query.filter_by(user_id=user.user_id, calendar_id=calendar.calendar_id).first()
            # 若打卡记录不存在，则创建新的记录
            if not record:
                record = CardRecordModel(user_id=user.user_id, username=user.username, calendar_id=calendar.calendar_id,
                                         date=calendar.date)
                db.session.add(record)
                db.session.commit()

            # 获取用户的打卡记录
            morningChecked = record.morning_checkin
            eveningChecked = record.evening_checkin
            morningTime = record.morning_checkin_time.strftime('%H时%M分%S秒') if record.morning_checkin_time else None
            eveningTime = record.evening_checkin_time.strftime('%H时%M分%S秒') if record.evening_checkin_time else None
            # 返回数据
            response_data = {'morning_checkin': morningChecked, 'morning_checkin_time': morningTime,
                             'evening_checkin': eveningChecked, 'evening_checkin_time': eveningTime}
            return {'message': '获取打卡信息成功', 'data': response_data}, 200
        except Exception as e:
            print(e)
            return {'message': '获取打卡信息失败', 'error': str(e)}, 500


class MarkCardAmResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('date', type=str, required=True)
        parser.add_argument('morningChecked', type=bool, required=False)
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        date = args['date']
        morningChecked = args['morningChecked']
        # 处理数据
        try:
            # 解析日期
            today_date = datetime.strptime(date, '%Y年%m月%d日').date()
            # 查询用户
            user = UserModel.query.filter_by(username=username).first()
            # 查询用户今天的打卡记录
            record = CardRecordModel.query.filter_by(user_id=user.user_id, date=today_date).first()
            # 获取当前时间
            time = datetime.now().strftime('%H时%M分%S秒')
            mark_card_time = datetime.strptime(time, '%H时%M分%S秒').time()
            # 获取用户的打卡记录
            record.morning_checkin = morningChecked
            record.morning_checkin_time = mark_card_time
            db.session.commit()
            # 返回数据
            response_data = {'morning_checkin': morningChecked,
                             'morning_checkin_time': mark_card_time.strftime('%H时%M分%S秒')}
            return {'message': '打卡成功', 'data': response_data}, 200
        except Exception as e:
            return {'message': '打卡失败', 'error': str(e)}, 500


class MarkCardPmResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('date', type=str, required=True)
        parser.add_argument('eveningChecked', type=bool, required=False)
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        date = args['date']
        eveningChecked = args['eveningChecked']
        # 处理数据
        try:
            # 解析日期
            today_date = datetime.strptime(date, '%Y年%m月%d日').date()
            # 查询用户
            user = UserModel.query.filter_by(username=username).first()
            # 查询用户今天的打卡记录
            record = CardRecordModel.query.filter_by(user_id=user.user_id, date=today_date).first()

            # 获取当前时间
            time = datetime.now().strftime('%H时%M分%S秒')
            mark_card_time = datetime.strptime(time, '%H时%M分%S秒').time()
            # 获取用户的打卡记录
            record.evening_checkin = eveningChecked
            record.evening_checkin_time = mark_card_time
            db.session.commit()
            # 返回数据
            response_data = {'evening_checkin': eveningChecked,
                             'evening_checkin_time': mark_card_time.strftime('%H时%M分%S秒')}
            return {'message': '打卡成功', 'data': response_data}, 200
        except Exception as e:
            return {'message': '打卡失败', 'error': str(e)}, 500
