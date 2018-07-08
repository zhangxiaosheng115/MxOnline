# -*- coding: utf-8 -*-
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin  # xadmin
from django.views.generic import TemplateView  # django用来处理直接返回静态页面的类,没有后天逻辑时可以使用
from django.views.static import  serve

from MxOnline.settings import MEDIA_ROOT
from users import views as user
from organization import views as org

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),  # 直接访问域名返回的页面

    # url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^login/$', user.LoginView.as_view(), name='login'),  # 返回的是一个函数对象

    url(r'^register/$', user.RegisterView.as_view(), name='register'),  # 注册接口

    url(r'^captcha/', include('captcha.urls')),  # 图片验证码功能，使用的库

    # 通过这样写可以直接拿到激活码,正则表达式
    url(r'^active/(?P<active_code>.*)/$', user.RegisterActiveView.as_view(), name="active"),

    # 找回密码url
    url(r'forget_pwd/$', user.ForgetPwdView.as_view(), name='forget_pwd'),

    # 密码找回链接
    url(r'^reset_pwd/(?P<active_code>.*)/$', user.ResetPwdView.as_view(), name="reset_pwd"),
    url(r'modify_pwd/$', user.ModifyPwdView.as_view(), name='modify_pwd'),

    url(r'org_list/$', org.OrgListView.as_view(), name="org_list"),

    # media 请求路径
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
]
