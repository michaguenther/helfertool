# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='subject',
            field=models.CharField(choices=[('newevent', 'New event'), ('permadduser', 'Permission to add new users'), ('permaddevent', 'Permission to add new events'), ('feature', 'Feature request'), ('bug', 'Bug report'), ('other', 'Other topic')], max_length=20, verbose_name='Subject'),
        ),
    ]
