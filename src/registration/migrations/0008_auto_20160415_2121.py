# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_event_ask_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Registration publicly visible'),
        ),
    ]
