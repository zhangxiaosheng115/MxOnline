# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-06 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180704_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='code',
            field=models.CharField(max_length=32, verbose_name='\u9a8c\u8bc1\u7801'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='code_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c\u6fc0\u6d3b'), ('forget', '\u627e\u56de\u5bc6\u7801')], max_length=20, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b'),
        ),
    ]
