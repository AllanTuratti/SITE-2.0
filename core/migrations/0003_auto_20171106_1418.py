# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
