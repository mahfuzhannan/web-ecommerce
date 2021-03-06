# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-22 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170322_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketproduct',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_products', related_query_name='basket_product', to='app.Basket'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 22, 18, 13, 699978, tzinfo=utc)),
        ),
    ]
