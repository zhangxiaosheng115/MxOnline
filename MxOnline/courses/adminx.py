# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/3 18:49'

import xadmin
from courses import models

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'duration', 'students',
                    'fav_nums', 'image', 'click_nums', 'add_time']

    search_fields = ['name', 'desc', 'detail', 'degree', 'duration', 'students', 'fav_nums', 'image', 'click_nums']

    list_filter = ['name', 'desc', 'detail', 'degree', 'duration', 'students',
                   'fav_nums', 'image', 'click_nums', 'add_time']

xadmin.site.register(models.Course, CourseAdmin)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']

xadmin.site.register(models.Lesson, LessonAdmin)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download_address', 'add_time']
    search_fields = ['course', 'name', 'download_address']
    list_filter = ['course', 'name', 'download_address', 'add_time']

xadmin.site.register(models.CourseResource, CourseResourceAdmin)


class ViedoAdmin(object):
    list_display = ['lesson', 'name', 'time_length', 'add_time']
    search_fields = ['lesson', 'name', 'time_length']
    list_filter = ['lesson', 'name', 'time_length', 'add_time']

xadmin.site.register(models.Viedo, ViedoAdmin)