# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0066_trackreport01'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackReport00',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='.', max_length=16, verbose_name='DEPT')),
                ('a', models.IntegerField(default=0, verbose_name='项次')),
                ('b', models.CharField(default='.', max_length=32, verbose_name='需求类型')),
                ('c', models.CharField(default='.', max_length=32, verbose_name='作业程序')),
                ('d', models.CharField(default='.', max_length=32, verbose_name='业务需求')),
                ('e', models.CharField(default='.', max_length=32, verbose_name='讨论结果')),
                ('f', models.DateField(blank=True, max_length=32, null=True, verbose_name='讨论日期')),
                ('g', models.DateField(blank=True, max_length=32, null=True, verbose_name='确认日期')),
                ('h', models.CharField(default='.', max_length=512, verbose_name='客制否')),
                ('i', models.CharField(default='.', max_length=512, verbose_name='BPM')),
                ('j', models.IntegerField(default=0, verbose_name='工时')),
                ('k', models.CharField(default='.', max_length=512, verbose_name='备注')),
                ('l', models.CharField(default='.', max_length=512, verbose_name='客制状态')),
                ('m', models.CharField(default='.', max_length=32, verbose_name='客制完成否')),
            ],
            options={
                'verbose_name': '全制程--报表-业务-and others',
                'verbose_name_plural': '全制程--报表-业务-and others',
            },
        ),
    ]
