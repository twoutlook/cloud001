# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0003_auto_20161129_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='followup',
            field=models.CharField(default='.', max_length=512, verbose_name='後續追蹤'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.CharField(default='.', max_length=512, verbose_name='主題記要'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='標記'),
        ),
    ]
