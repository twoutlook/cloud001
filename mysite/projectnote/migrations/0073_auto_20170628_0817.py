# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-28 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0072_t100dept_t100depttest'),
    ]

    operations = [
        migrations.AddField(
            model_name='t100dept',
            name='D1',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發未开工'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D2',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發在制'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D3',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發完成待验收'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D4',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發完成已验收'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D5',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發取消'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D6',
            field=models.IntegerField(default=0, verbose_name='鼎捷開發状态不明'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D7',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='D8',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F1',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F2',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F3',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F4',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F5',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F6',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F7',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
        migrations.AddField(
            model_name='t100dept',
            name='F8',
            field=models.IntegerField(default=0, verbose_name='工时'),
        ),
    ]
