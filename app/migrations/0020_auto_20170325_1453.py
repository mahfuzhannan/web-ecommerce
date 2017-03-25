# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20170325_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 25, 14, 53, 1, 681196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 25, 14, 53, 1, 685189, tzinfo=utc)),
        ),
    ]