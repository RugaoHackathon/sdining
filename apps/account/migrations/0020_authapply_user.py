# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 20:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_authapply_date_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='authapply',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请者'),
            preserve_default=False,
        ),
    ]