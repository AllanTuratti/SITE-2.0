# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171111_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='Matriz_Curricular',
            field=models.TextField(blank=True),
        ),
    ]
