class Config:
    # 应用程序的密钥，用于会话安全等
    SECRET_KEY = 'mySecretKey'

    # 数据库的配置信息
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'my_system'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，没有设置会有警告
    SQLALCHEMY_ECHO = False  # 查询时显示原始SQL语句

    # 邮箱的配置信息
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'liuyuhaoweb@163.com'
    MAIL_PASSWORD = 'ELCUNEUDEMBQXKRV'
    MAIL_DEFAULT_SENDER = 'liuyuhaoweb@163.com'

    # 是否开启调试模式
    DEBUG = True
