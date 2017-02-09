# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20161111_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='shirt',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('S_GIRLY', 'S (girly)'), ('M_GIRLY', 'M (girly)'), ('L_GIRLY', 'L (girly)'), ('XL_GIRLY', 'XL (girly)')], default='UNKNOWN', max_length=20, verbose_name='T-shirt'),
        ),
    ]
