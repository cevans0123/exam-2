# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-25 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
