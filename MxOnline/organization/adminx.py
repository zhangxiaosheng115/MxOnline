# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/3 19:06'


import xadmin
from organization import models


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

xadmin.site.register(models.City, CityAdmin)


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address']
    list_filter = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']

xadmin.site.register(models.CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_nums', 'fav_nums', 'add_time']

    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']

    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position',
                   'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(models.Teacher, TeacherAdmin)