# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 21:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0005_auto_20170812_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authapply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商家名称')),
                ('position', models.IntegerField(choices=[(1, '楚园食堂'), (2, '汉园食堂')], verbose_name='位置')),
                ('floor', models.IntegerField(choices=[(1, '一楼'), (2, '二楼')], verbose_name='楼层')),
                ('type', models.IntegerField(choices=[(1, '餐品'), (2, '饮品')], verbose_name='商家类型')),
                ('date_apply', models.DateTimeField(auto_now_add=True, verbose_name='申请时间')),
                ('is_passed', models.BooleanField(default=False, verbose_name='是否通过')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请者')),
            ],
            options={
                'verbose_name': '商家认证申请',
                'verbose_name_plural': '商家认证申请',
            },
        ),
    ]
