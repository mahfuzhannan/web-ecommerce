# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 21:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170321_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 21, 38, 57, 488684, tzinfo=utc)),
        ),
    ]
