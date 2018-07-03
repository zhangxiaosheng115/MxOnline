# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser  # django 默认用户表，用来继承有些字段就不需要自己写了


class User(AbstractUser):  # 继承的django自带的表
    # TODO 用户量较大，需要优化成分表设计，增加字段user_id --分表字段
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    sex = models.CharField(choices=(('male', u"男"),('female', u"女")), default='male', max_length=10)
    address = models.CharField(max_length=50, verbose_name=u"地址", default='')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号码")
    # 用来存储用户头像的地址，是一个路径
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # 打印的时候显示
        return self.username


class EmailVerifyRecord(models.Model):  # TODO 将所有数据的操作放在类里边，方便管理,后续可以加一层缓存--redis
    """
    邮箱验证码存储，验证码存储用redis实现更方便，后续修改
    """
    code = models.CharField(max_length=10, verbose_name=u"验证码")
    email = models.EmailField(max_length=20, verbose_name=u"邮箱")
    code_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码")),
                                 max_length=20, verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送验证码时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # 重载unicode方法是为了在后台显示的时候更加清晰而不是 EmailVerifyRecord object
        return '{0}{1}'.format(self.email,self.code)


class Banner(models.Model):
    """
    首页的轮播图资源
    """
    title = models.CharField(max_length=50, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"图片地址", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"点击跳转的url")
    index = models.ImageField(default=100, verbose_name=u"每张图片的顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
