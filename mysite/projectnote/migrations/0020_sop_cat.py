# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0019_auto_20170217_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='sop',
            name='cat',
            field=models.CharField(choices=[('ABM产品结构', 'ABM产品结构'), ('AIC多角贸易', 'AIC多角贸易'), ('AIM料件', 'AIM料件'), ('AIN库存', 'AIN库存'), ('AMR模具', 'AMR模具'), ('AOO集团架构', 'AOO集团架构'), ('APM采购', 'APM采购'), ('APS排程', 'APS排程'), ('AQC质量', 'AQC质量'), ('ASF生产', 'ASF生产'), ('AXM销售', 'AXM销售'), ('AZZ整体', 'AZZ整体')], default='???', max_length=32, verbose_name='CAT'),
        ),
    ]