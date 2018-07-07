# -*- coding: utf-8 -*-
__author__ = 'zxs'
__date__ = '2018/7/3 18:07'

import xadmin
from users import models
from xadmin import views


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'code_type', 'send_time']  # 用来控制显示哪些字段
    search_fields = ['code', 'email', 'code_type']  # 可搜素的字段
    list_filter = ['code', 'email', 'code_type', 'send_time']  # 用来作为过滤的字段

xadmin.site.register(models.EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(models.Banner, BannerAdmin)


class BaseSetting(object):
    """
    开放xadmin后台的主题功能
    """
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    """
    修改主题以及底部标题
    """
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion"  # 使菜单栏可以折叠

xadmin.site.register(views.CommAdminView, GlobalSetting)