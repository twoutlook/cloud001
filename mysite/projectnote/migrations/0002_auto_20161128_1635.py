# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='.', max_length=256, verbose_name='記要')),
                ('followup', models.CharField(default='.', max_length=256, verbose_name='後續追蹤')),
            ],
        ),
        migrations.DeleteModel(
            name='Flowchartprocess',
        ),
    ]
