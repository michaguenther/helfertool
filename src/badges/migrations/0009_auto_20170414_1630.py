# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0008_badgesettings_only_coordinators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='custom_design',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='badges.BadgeDesign', verbose_name='Design'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='custom_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='badges.BadgeRole', verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='badgedefaults',
            name='design',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='badges.BadgeDesign', verbose_name='Default design'),
        ),
        migrations.AlterField(
            model_name='badgedefaults',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='badges.BadgeRole', verbose_name='Default role'),
        ),
    ]
