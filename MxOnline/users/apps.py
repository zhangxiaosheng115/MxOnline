# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

"""
用来配置app显示名称
"""

class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户"