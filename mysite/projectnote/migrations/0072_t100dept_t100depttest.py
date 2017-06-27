# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-27 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0071_auto_20170627_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='T100Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t100DeptId', models.CharField(default='0000', max_length=16, verbose_name='T100 DEPT_ID')),
                ('t100DeptName', models.CharField(default='.', max_length=16, verbose_name='T100 DEPT NAME')),
            ],
        ),
        migrations.CreateModel(
            name='T100DeptTEST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='.', max_length=32, verbose_name='NOTE')),
                ('t100Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectnote.T100Dept')),
            ],
        ),
    ]
