const base = {
  login: "/login", //登录
  send_code: "/send_code", //发送验证码
  register: "/register", //注册
  update_password: "/update_password", //修改密码
  get_user_count: "/admin_home/get_user_count", //获取用户总数
  get_user_log_count: "/admin_home/get_user_log_count", //获取用户登录日志总数
  get_user_list: "/admin_home/get_user_list", //获取用户列表
  get_user_log_list: "/admin_home/get_user_log_list", //获取用户登录日志列表
  get_user: "/admin_user/get_user", //获取用户列表
  add_user: "/admin_user/add_user", //添加用户
  update_user: "/admin_user/update_user", //编辑用户
  delete_user: "/admin_user/delete_user", //删除用户
  set_password: "/admin_user/set_password", //重置密码
  get_log: "/admin_log/get_log", //获取日志列表
  delete_log: "/admin_log/delete_log", //获取日志列表
  get_time: "/get_time", //获取时间
  get_mark_card_info: "/get_mark_card_info", //获取打卡信息
  mark_card_am: "/mark_card_am", //上午打卡
  mark_card_pm: "/mark_card_pm", //下午打卡
  get_record_list:"/get_record",//获取签到记录列表
  delete_record:"/delete_record",//删除签到记录
  admin_get_record_list:"/admin_record/get_record",//获取签到记录列表
  admin_delete_record:"/admin_record/delete_record",//删除签到记录
};

export default base;
