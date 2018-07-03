# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/3 19:18'

import xadmin
from operation import models


class UserAskAdmin(object):
    list_display = ['user', 'name', 'mobile', 'course_name', 'add_time']
    search_fields = ['user', 'name', 'mobile', 'course_name']
    list_filter = ['user', 'name', 'mobile', 'course_name', 'add_time']

xadmin.site.register(models.UserAsk, UserAskAdmin)


class UserCommentsAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user', 'course', 'comment']
    list_filter = ['user', 'course', 'comment', 'add_time']

xadmin.site.register(models.UserComments, UserCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']

xadmin.site.register(models.UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['user_id', 'message', 'has_read', 'add_time']
    search_fields = ['user_id', 'message', 'has_read']
    list_filter = ['user_id', 'message', 'has_read', 'add_time']

xadmin.site.register(models.UserMessage, UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']

xadmin.site.register(models.UserCourse, UserCourseAdmin)