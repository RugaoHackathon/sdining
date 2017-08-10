# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_accesstoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauthqqprofile',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], default=1, verbose_name='性别'),
        ),
    ]