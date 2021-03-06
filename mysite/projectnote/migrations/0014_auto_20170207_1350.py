# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0013_auto_20170207_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='trans',
            name='cat',
            field=models.IntegerField(choices=[(1, '期初'), (2, '购进'), (3, '领用')], default=2, max_length=7, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='trans',
            name='yrmonth',
            field=models.CharField(choices=[('2017-01', '2017-01'), ('2017-02', '2017-02'), ('2017-03', '2017-03'), ('2017-04', '2017-04'), ('2017-05', '2017-05'), ('2017-06', '2017-06'), ('2017-07', '2017-07'), ('2017-08', '2017-08'), ('2017-09', '2017-09'), ('2017-10', '2017-10'), ('2017-11', '2017-11'), ('2017-12', '2017-12')], default='2017-01', max_length=7, verbose_name='年月'),
        ),
    ]
