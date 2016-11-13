# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20161111_1324'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventorySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_inventory', models.ManyToManyField(to='inventory.Inventory', verbose_name='Available inventory')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
    ]
