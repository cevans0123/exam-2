# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-25 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_job_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_public',
        ),
    ]
