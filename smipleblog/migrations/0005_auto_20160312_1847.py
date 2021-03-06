# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smipleblog', '0004_auto_20160312_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 12, 10, 47, 37, 552699, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 47, 37, 551855, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=None, verbose_name=datetime.datetime(2016, 3, 12, 10, 47, 37, 551893, tzinfo=utc)),
        ),
    ]
