# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-03 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20180703_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='user',
            new_name='user_id',
        ),
    ]