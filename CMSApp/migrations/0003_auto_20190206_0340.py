# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-05 20:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CMSApp', '0002_report_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='postal_code',
            field=models.CharField(default=-1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 5, 20, 40, 24, 44249, tzinfo=utc)),
        ),
    ]
