# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0044_item007'),
    ]

    operations = [
        migrations.AddField(
            model_name='item007',
            name='r03c7xx0',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-正常'),
        ),
        migrations.AddField(
            model_name='item007',
            name='r03c7xx1',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-磨損'),
        ),
        migrations.AddField(
            model_name='item007',
            name='r03c7xx2',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-無法修復'),
        ),
    ]
