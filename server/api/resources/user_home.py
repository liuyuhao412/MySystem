from flask_restful import Resource, reqparse
from ..models.user import LoginLogModel


class GetLoginTimeResource(Resource):
    @staticmethod
    def post():
        # 创建请求解析器
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='需要提供用户名')
        # 解析参数
        args = parser.parse_args()
        username = args['username']
        log = LoginLogModel.query.filter_by(username=username).order_by(LoginLogModel.login_time.desc()).first()
        login_time = log.login_time
        time = "您上次登录的时间：" + login_time.strftime("%Y-%m-%d %H:%M:%S")
        return {'message': time}, 200
