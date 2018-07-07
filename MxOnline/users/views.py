# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login  # django自带的用来认证用户的方法 与登录方法
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password # 用来往数据库中存储密码的

from share.utils import send_email
from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from users.models import User, EmailVerifyRecord


"""
登录接口，操作同一个资源用同一个接口，只是不同的方法
1	GET	请求指定的页面信息，并返回实体主体。
2	HEAD	类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
3	POST	向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
4	PUT	    从客户端向服务器传送的数据取代指定的文档的内容。
5	DELETE	请求服务器删除指定的页面。
6	CONNECT	HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
7	OPTIONS	允许客户端查看服务器的性能。
8	TRACE	回显服务器收到的请求，主要用于测试或诊断。
"""

class CustomBackend(ModelBackend):
    """
    自定义登录校验的方法
    """
    def authenticate(self, username=None, password=None, **kwargs):
        """
        重载父类的方法
        :param username:
        :param password:
        :param kwargs:
        :return:
        """
        try:
            # 支持或的查询，用户名邮箱都可以进行登录
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request): # 请其他页面跳转，直接返回页面
        """
        get方法时请求
        :param request:
        :return:
        """
        return render(request, 'login.html', {})

    def post(self, request):
        """
        post请求
        :param request:
        :return:
        """
        login_form = LoginForm(request.POST)  # 参数的校验全部交给form去判断

        if login_form.is_valid():  # 表单有效
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            # 自带的用户认证方法,在setting中进行配置会调用自定义的校验方法 底层会去user表中进行查找
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    return render(request, "login.html", {"msg": u"用户未激活"})

                login(request, user)  # login原理 cookie + secssion， 会对request进行参数填充，然后request返回
                # 前端根据request.user状态判断用户是否已经登录
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": u"用户名或者密码错误"})

        else:
            return render(request, "login.html", {"login_form" : login_form})  # 将表单返回

    def put(self, request):
        pass

    def delete(self, request):
        pass


class RegisterView(View):
    """
    注册功能接口
    """
    def get(self, request):
        """
        在请求的时候会自动生成图片验证码
        :param request:
        :return:
        """
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})  # 将生成的验证码返回

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get("email")  # 这里需要判断用户是否已经存在
            password = register_form.cleaned_data.get("password")
            if User.objects.filter(email=email).first():
                # 表示该用户名已经存在
                return render(request, "register.html", {"register_form": register_form, "msg": u"用户名已存在"})

            else:
                # 向用户发送激活邮件
                send_status = send_email(email, "register")
                if send_status:
                    user = User()
                    user.username = email
                    user.email = email
                    user.password = make_password(password)  # 加密密码存入数据库
                    user.is_active = False  # 用户注册时默认为未激活，需要通过邮箱连接进行激活
                    user.save()
                    return render(request, "login.html")

                else:  # 邮件发送失败
                    return render(request, "register.html", {"msg": u"邮件发送失败，请重试"})

        else:  # 如果表单校验没通过，将表单信息返回，页面进行信息显示
            return render(request, 'register.html', {"register_form": register_form})


class RegisterActiveView(View):
    """
    注册链接激活接口
    """
    def get(self, request, active_code):
        # 先从数据库查是否有这个激活码
        email_object = EmailVerifyRecord.objects.filter(code=active_code)

        if email_object:
            for object in email_object:
                user = User.objects.get(email=object.email)
                if user:
                    # 有这个用户
                    user.is_active = True
                    user.save()
                    return render(request, "login.html")

            return render(request, "active_fail.html", {"msg": u"激活码错误"})

        else:  # 没有这个激活码
            return render(request, "active_fail.html", {"msg": u"激活码错误"})


class ForgetPwdView(View):
    def get(self, request):
        forget_pwd_form = ForgetForm(request.GET)
        return render(request, 'forgetpwd.html', {"forget_pwd_form": forget_pwd_form})

    def post(self, request):
        forget_pwd_form = ForgetForm(request.POST)

        if forget_pwd_form.is_valid():
            email = forget_pwd_form.cleaned_data.get("email")
            user = User.objects.get(email=email)

            if user:  # 说明用户存在, 向用户的邮箱发邮件，修改用户的密码
                flag = send_email(email, email_type="forget")
                if flag:
                    # 邮件发送成功
                    return render(request, "email_success.html", {"msg": u"修改密码邮件发送成功，请前往邮箱查看"})
                else:
                    return render(request, "email_success.html", {"msg": u"邮件发送失败，请重试"})
            else:
                return render(request, "forgetpwd.html", {"forget_pwd_form": forget_pwd_form, "msg": u"邮件地址错误"})

        else:  # 表单错误
            return render(request, "forgetpwd.html", {"forget_pwd_form": forget_pwd_form})


class ResetPwdView(View):
    """
    点击修改密码邮件
    """
    def get(self, request, active_code):
        email_object = EmailVerifyRecord.objects.filter(code=active_code)

        if email_object:
            for object in email_object:
                user = User.objects.get(email=object.email)

                if user:
                    return render(request, "password_reset.html", {"email": object.email})

        else:  # 没有这个激活码
            return render(request, "password_reset.html", {"msg": u"链接已失效"})


class ModifyPwdView(View):

    def post(self, request):
        pwd_form = ModifyPwdForm(request.POST)

        if pwd_form.is_valid():
            password1 = pwd_form.cleaned_data.get("password1")
            password2 = pwd_form.cleaned_data.get("password2")
            email = pwd_form.cleaned_data.get("email")
            user = User.objects.get(email=email)

            if not user:
                return render(request, "password_reset.html", {"msg": u"密码修改失败"})

            if password1 != password2:
                return render(request, "password_reset.html", {"msg": u"两次密码输入不相同"})

            user.password = make_password(password1)
            user.save()
            return render(request, "login.html")

        else:
            return render(request, "password_reset.html", {"msg": u"密码格式错误"})
