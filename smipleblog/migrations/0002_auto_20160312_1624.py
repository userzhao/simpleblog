# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smipleblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 12, 8, 24, 7, 837590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 12, 8, 24, 7, 829943, tzinfo=utc)),
        ),
    ]
