# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/4 17:27'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    """
    注册表单
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 图片验证码字段，后面dict转成中文错误


class ForgetForm(forms.Form):
    """
    找回密码提交的表单
    """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 图片验证码字段，后面dict转成中文错误


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)
    email = forms.EmailField(required=True)