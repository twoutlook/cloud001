# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20170209_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feeback_text',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='question',
        ),
    ]
