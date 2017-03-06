# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0027_t100'),
    ]

    operations = [
        migrations.CreateModel(
            name='T100item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_seq', models.IntegerField(default=0)),
                ('item_text', models.CharField(max_length=600)),
                ('t100', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectnote.T100')),
            ],
        ),
    ]
