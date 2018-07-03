# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import User
from courses.models import Course


class UserAsk(models.Model):
    """
    用户申请学习信息
    """
    user = models.ForeignKey(User, verbose_name=u"用户")
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    mobile = models.CharField(max_length=11, verbose_name=u"用户手机号")
    course_name = models.CharField(max_length=50, verbose_name=u"申请课的名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"申请时间")

    class Meta:
        verbose_name = u"用户申请表"
        verbose_name_plural = verbose_name


class UserComments(models.Model):
    """
    用户对课程的评论
    """
    user = models.ForeignKey(User, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comment = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")


    class Meta:
        verbose_name = u"用户评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户的收藏，可以收藏课程、机构、讲师
    """
    user = models.ForeignKey(User, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"收藏的id")
    fav_type = models.IntegerField(choices=((1, u"课程"), (2, u"机构"), (3, u"机构")),
                                   default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户的消息
    """
    user_id = models.IntegerField(default=0, verbose_name=u"接受用户")  # 当id == 0 时表示发给所有用户
    message = models.CharField(max_length=300, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读") # False 表示未读
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """
    用户的课程
    """
    user = models.ForeignKey(User, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name






