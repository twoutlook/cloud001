# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0025_auto_20170302_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sopdata',
            options={'verbose_name': '参数及基本数据建置进度计划表', 'verbose_name_plural': '参数及基本数据建置进度计划表'},
        ),
        migrations.AddField(
            model_name='sop',
            name='by2',
            field=models.CharField(default='...', max_length=16, verbose_name='审核人员'),
        ),
        migrations.AlterField(
            model_name='sopdata',
            name='cat',
            field=models.CharField(choices=[('整体', '整体'), ('制造', '制造')], default='整体', max_length=16, verbose_name='分類'),
        ),
    ]
