# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0033_auto_20170320_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bpm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=16, verbose_name='部门')),
                ('sop_name', models.CharField(max_length=512, verbose_name='SOP名称')),
            ],
            options={
                'verbose_name_plural': 'BPM列表',
                'verbose_name': 'BPM列表',
            },
        ),
        migrations.AlterField(
            model_name='dailywork',
            name='remarks',
            field=models.CharField(max_length=512, verbose_name='TODO'),
        ),
    ]
