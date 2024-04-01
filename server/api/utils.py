import random
import re

from flask_mail import Message

from . import mail


def is_valid_email(email):
    # 正则表达式用于检查邮箱格式
    email_pattern = r'^\S+@\S+\.\S+$'
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False


def check_password(password):
    # 密码要求：8位以上，包含数字、大小写字母和特殊字符
    pattern = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=])[0-9a-zA-Z!@#$%^&*()-_+=]{8,}$')

    # 使用正则表达式检查密码格式
    if pattern.match(password):
        return True
    else:
        return False


def send_verification_code(email):
    code = ''.join(random.choice('0123456789') for i in range(6))
    message = Message(subject='问答系统', recipients=[email],
                      body=f'【问答系统】注册验证码 {code},10分钟有效,请勿告知他人。')
    mail.send(message)
    return code
