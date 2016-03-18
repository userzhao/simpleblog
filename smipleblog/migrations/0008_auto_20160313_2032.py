# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smipleblog', '0007_auto_20160312_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 13, 12, 32, 34, 284666, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 13, 12, 32, 34, 283906, tzinfo=utc)),
        ),
    ]
