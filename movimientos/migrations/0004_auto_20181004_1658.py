# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0003_auto_20180929_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='cierrecaja',
            name='recibo_desde',
            field=models.CharField(max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='recibo_hasta',
            field=models.CharField(max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='num_recibo',
            field=models.IntegerField(unique=True),
        ),
    ]
