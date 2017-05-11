# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0049_auto_20170407_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(default='BPM開發', max_length=32, verbose_name='類別')),
                ('b', models.CharField(default='.', max_length=32, verbose_name='姓名')),
                ('c', models.CharField(max_length=512, verbose_name='內容')),
            ],
            options={
                'verbose_name_plural': '技術梗',
                'verbose_name': '技術梗',
            },
        ),
        migrations.AlterField(
            model_name='sqlstatement',
            name='prog',
            field=models.CharField(blank=True, default='.', max_length=512, null=True, verbose_name='T100運行程序'),
        ),
    ]
