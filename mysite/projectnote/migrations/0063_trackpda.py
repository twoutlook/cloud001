# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0062_auto_20170623_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackPDA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField(default=0, verbose_name='序号')),
                ('b', models.DateField(blank=True, max_length=32, null=True, verbose_name='提报时间')),
                ('c', models.CharField(default='.', max_length=32, verbose_name='提报人员')),
                ('d', models.CharField(default='.', max_length=32, verbose_name='鼎捷责任人')),
                ('e', models.CharField(default='.', max_length=32, verbose_name='问题分类')),
                ('f', models.CharField(default='.', max_length=512, verbose_name='问题描述')),
                ('g', models.CharField(default='.', max_length=512, verbose_name='问题分析')),
                ('h', models.CharField(default='.', max_length=512, verbose_name='解决方案')),
                ('i', models.DateField(blank=True, max_length=32, null=True, verbose_name='计划完成时间')),
                ('j', models.DateField(blank=True, max_length=32, null=True, verbose_name='实际完成时间')),
                ('k', models.CharField(default='.', max_length=512, verbose_name='进度状态')),
                ('l', models.CharField(default='.', max_length=512, verbose_name='用户确认')),
                ('m', models.CharField(default='.', max_length=32, verbose_name='备注')),
            ],
            options={
                'verbose_name': '全制程--智能物流问题追踪表',
                'verbose_name_plural': '全制程--智能物流问题追踪表',
            },
        ),
    ]