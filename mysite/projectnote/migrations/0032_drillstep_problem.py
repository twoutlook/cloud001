# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0031_drillstep_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='drillstep',
            name='problem',
            field=models.CharField(default='...', max_length=512, verbose_name='異常'),
        ),
    ]