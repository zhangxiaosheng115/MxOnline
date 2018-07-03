# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    """
    课程数据,一行记录一门课
    """
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程的描述信息")
    detail = models.TextField(verbose_name=u"课程详情")  # 副文本的存储
    degree = models.CharField(max_length=5, choices=(('cj', u"初级"), ('zj', u"中级"), ('gj', u"高级")),
                              verbose_name=u"课程的等级")

    duration = models.ImageField(default=0, verbose_name=u"课程总时长")
    students = models.IntegerField(default=0, verbose_name=u"学习的人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/image/%Y/%m", verbose_name=u"课程的封面图")
    click_nums = models.IntegerField(default=0, verbose_name=u"被点击的次数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"课程添加的时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name  # 复数形式


class Lesson(models.Model):
    """
    课程的章节信息，一个课程对应多个章节
    """
    course = models.ForeignKey(Course, verbose_name=u"课程")  # 章节所对应的课程，用外键的形式
    name = models.CharField(max_length=30, verbose_name=u"章节的名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"章节的添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Viedo(models.Model):
    """
    一章中的视频
    """
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=30, verbose_name=u"视频名称")
    time_length = models.IntegerField(default=0, verbose_name=u"视频的时长")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"视频的添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    """
    课程的资源信息表
    """
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"资源名称")
    download_address = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"课程资源地址", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"资源上传时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name


