# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='imagen',
            field=models.ImageField(upload_to="logos"),
        ),
    ]
