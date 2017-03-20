# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0041_remove_bpm_complete_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpm',
            name='complete_date',
            field=models.DateField(null=True, verbose_name='行情日期'),
        ),
        migrations.AddField(
            model_name='bpm',
            name='concern',
            field=models.CharField(default='.', max_length=512, verbose_name='BPM-T100集成相关问题'),
        ),
        migrations.AddField(
            model_name='bpm',
            name='qry_t100',
            field=models.CharField(default='.', max_length=512, verbose_name='查询T100数据'),
        ),
        migrations.AddField(
            model_name='bpm',
            name='to_print',
            field=models.CharField(default='.', max_length=512, verbose_name='需待T100客制'),
        ),
    ]
