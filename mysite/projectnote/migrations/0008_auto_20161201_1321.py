# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectnote', '0007_auto_20161129_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('A356', 'A356'), ('A380', 'A380'), ('ADC12', 'ADC12'), ('Zamak3', 'Zamak3'), ('Zamak5', 'Zamak5'), ('Zn99.995', 'Zn99.995')], default='???', max_length=32, verbose_name='牌号')),
                ('pricedate', models.DateField(max_length=10, verbose_name='行情日期')),
                ('priceavg', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='平均价')),
                ('yearnum', models.IntegerField(default=2016, verbose_name='年')),
                ('monthnum', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=11, verbose_name='月')),
                ('quarternum', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=4, verbose_name='季')),
            ],
            options={
                'verbose_name': '上海有色網',
                'verbose_name_plural': '上海有色網',
            },
        ),
        migrations.AlterUniqueTogether(
            name='smm',
            unique_together=set([('designation', 'pricedate')]),
        ),
    ]
