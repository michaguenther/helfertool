# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import registration.models.event


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_event_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='email',
            field=models.EmailField(default=registration.models.event._default_mail, help_text='Used as Reply-to address for mails sent to helpers', max_length=254, verbose_name='E-Mail'),
        ),
    ]
