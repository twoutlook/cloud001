# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feeback_text',
            field=models.CharField(choices=[('可以', '可以'), ('不行', '不行'), ('不知道', '不知道')], default='不知道', max_length=200, verbose_name='回覆'),
        ),
    ]
