# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class City(models.Model):
    """
    机构所属的城市
    """
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    desc = models.CharField(max_length=200, verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    """
    课程机构信息
    """
    city = models.ForeignKey(City, verbose_name=u"机构所属城市")
    name = models.CharField(max_length=30, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构的描述")
    click_nums = models.IntegerField(default=0, verbose_name=u"机构的点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"机构的收藏数")
    image = models.ImageField(upload_to="/org/%Y/%m", verbose_name=u"机构图片地址", max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"机构的具体地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """
    讲师信息
    """
    org = models.ForeignKey(CourseOrg, verbose_name=u"讲师所属机构")
    name = models.CharField(max_length=20, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=30, verbose_name=u"职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

