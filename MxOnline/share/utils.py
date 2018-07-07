# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/5 23:03'


from random import Random

from django.core.mail import send_mail

from MxOnline import settings
from users.models import EmailVerifyRecord


def gen_email_code(randomlength=8):
    """
    生成一个随机的字符串---长度默认8
    :return:
    """
    str = ''
    chars = "AaBbCcDdEeFfGgHhIiJjLlMmOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for i in xrange(randomlength):
        str += chars[random.randint(0, length)]

    return str


def send_email(email, email_type="register"):
    """
    用来向用户发送邮件的接口
    :return:
    """
    # 先将信息存入数据库，再发送邮件
    email_objects = EmailVerifyRecord()
    email_objects.email = email
    email_objects.code_type = email_type
    code = gen_email_code(randomlength=16)
    email_objects.code = code
    email_objects.save()

    # 发送邮件，用django自带的函数，需要在setting文件中配置好邮件的相关信息，比如说发送者服务器等等

    if email_type == "register":
        email_title = u"慕学在线网注册激活链接"
        email_body = u"请点击此链接完成账号激活:http:127.0.0.1:8000/active/{code}".format(code=code)
        # 其实是django通过配置--setting信息登录邮箱发送邮件
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:  # 邮件发送成功
            return True
        else:
            return False

    elif email_type == "forget":  # 表示是找回密码
        email_title = u"慕学在线网密码找回"
        email_body = u"请点击此链接修改密码:http:127.0.0.1:8000/reset_pwd/{code}".format(code=code)
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])

        if send_status:  # 邮件发送成功
            return True
        else:
            return False
