from .admin_home import GetUserCountResource, GetUserLogCountResource, GetUserListResource, GetUserLogResource
from .admin_log import GetLogResource, DeleteLogResource
from .admin_record import AdminGetRecordResource, AdminDeleteRecordResource
from .admin_user import GetUserResource, AddUserResource, UpdateUserResource, DeleteUserResource, SetPasswordResource
from .login import LoginResource, UpdatePasswordResource
from .register import SendCodeResource, RegisterResource
from .user_home import GetLoginTimeResource
from .user_mark_card import GetMarkCardInfoResource, MarkCardAmResource, MarkCardPmResource
from .user_record import GetRecordResource, DeleteRecordResource


def register_routes(api):
    # 登录
    api.add_resource(LoginResource, '/login')
    # 注册
    api.add_resource(SendCodeResource, '/send_code')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(UpdatePasswordResource, '/update_password')
    # admin_home
    api.add_resource(GetUserCountResource, '/admin_home/get_user_count')
    api.add_resource(GetUserLogCountResource, '/admin_home/get_user_log_count')
    api.add_resource(GetUserListResource, '/admin_home/get_user_list')
    api.add_resource(GetUserLogResource, '/admin_home/get_user_log_list')
    # admin_user
    api.add_resource(GetUserResource, '/admin_user/get_user')
    api.add_resource(AddUserResource, '/admin_user/add_user')
    api.add_resource(UpdateUserResource, '/admin_user/update_user')
    api.add_resource(DeleteUserResource, '/admin_user/delete_user')
    api.add_resource(SetPasswordResource, '/admin_user/set_password')
    # admin_log
    api.add_resource(GetLogResource, '/admin_log/get_log')
    api.add_resource(DeleteLogResource, '/admin_log/delete_log')
    # admin_record
    api.add_resource(AdminGetRecordResource, '/admin_record/get_record')
    api.add_resource(AdminDeleteRecordResource, '/admin_record/delete_record')
    # user_home
    api.add_resource(GetLoginTimeResource, '/get_time')
    # user_mark_card
    api.add_resource(GetMarkCardInfoResource, '/get_mark_card_info')
    api.add_resource(MarkCardAmResource, '/mark_card_am')
    api.add_resource(MarkCardPmResource, '/mark_card_pm')
    # user_record
    api.add_resource(GetRecordResource, '/get_record')
    api.add_resource(DeleteRecordResource, '/delete_record')
