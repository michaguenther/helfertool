# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0013_auto_20160704_1214'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('multiple_assignments', models.BooleanField(default=False, verbose_name='Same item may be assigned to different helpers')),
                ('admins', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Administrators of inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('barcode', models.CharField(max_length=100, verbose_name='Barcode')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='UsedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('timestamp_returned', models.DateTimeField(auto_now_add=True)),
                ('helper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Helper')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
        ),
    ]
