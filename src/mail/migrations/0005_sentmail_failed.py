# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_sentmail_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentmail',
            name='failed',
            field=models.BooleanField(default=False),
        ),
    ]
