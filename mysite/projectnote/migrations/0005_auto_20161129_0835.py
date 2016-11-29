# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0004_auto_20161129_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='where',
            field=models.CharField(default='.', max_length=512, verbose_name='Where'),
        ),
        migrations.AddField(
            model_name='note',
            name='whereurl',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='URL'),
        ),
    ]
