from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from .. import db


# 用户表
class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), default='user')
    created_time = db.Column(db.DateTime, default=datetime.utcnow)

    def to_json(self):
        return {'user_id': self.user_id, 'username': self.username, 'role': self.role,
                'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S')}

    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class LoginLogModel(db.Model):
    __tablename__ = "login_logs"
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(255), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False)

    # 添加关联属性
    user = db.relationship('UserModel', backref=db.backref('login_logs', lazy=True))

    def to_json(self):
        return {'log_id': self.log_id, 'username': self.username, 'role': self.role, 'ip': self.ip,
                'login_time': self.login_time.strftime('%Y-%m-%d %H:%M:%S')}


class CalendarModel(db.Model):
    __tablename__ = 'calendar'
    calendar_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    day_of_week = db.Column(db.String(10), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)


# 打卡记录
class CardRecordModel(db.Model):
    __tablename__ = 'card_records'
    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.calendar_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    morning_checkin = db.Column(db.Boolean, default=False)
    morning_checkin_time = db.Column(db.Time)
    evening_checkin = db.Column(db.Boolean, default=False)
    evening_checkin_time = db.Column(db.Time)

    user = db.relationship('UserModel', backref=db.backref('card_records', lazy=True))
    calendar = db.relationship('CalendarModel', backref=db.backref('card_records', lazy=True))

    def to_json(self):
        if self.morning_checkin:
            morning_checkin = '是'
        else:
            morning_checkin = '否'
        if self.evening_checkin:
            evening_checkin = '是'
        else:
            evening_checkin = '否'
        date = self.date.strftime('%Y年%m月%d日')
        if self.morning_checkin_time:
            morning_checkin_time = self.morning_checkin_time.strftime('%H时%M分%S秒')
        else:
            morning_checkin_time = ''
        if self.evening_checkin_time:
            evening_checkin_time = self.evening_checkin_time.strftime('%H时%M分%S秒')
        else:
            evening_checkin_time = ''
        return {'record_id': self.record_id, 'username':self.username, 'date': date, 'morning_checkin': morning_checkin,
                'morning_checkin_time': morning_checkin_time, 'evening_checkin': evening_checkin,
                'evening_checkin_time': evening_checkin_time}
