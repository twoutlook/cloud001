# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_sop_diagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='sop',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活躍'),
        ),
    ]