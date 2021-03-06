# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0043_auto_20170320_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpm',
            name='note1',
            field=models.CharField(default='.', max_length=512, verbose_name='SOP'),
        ),
        migrations.AddField(
            model_name='bpm',
            name='note2',
            field=models.CharField(default='.', max_length=512, verbose_name='TIOO运行程序'),
        ),
        migrations.AddField(
            model_name='bpm',
            name='note3',
            field=models.CharField(default='.', max_length=512, verbose_name='T100表单名称'),
        ),
        migrations.AlterField(
            model_name='bpm',
            name='complete_date',
            field=models.DateField(blank=True, null=True, verbose_name='完成日期'),
        ),
        migrations.AlterField(
            model_name='bpm',
            name='form_name',
            field=models.CharField(default='.', max_length=512, verbose_name='BPM表单名称'),
        ),
    ]
