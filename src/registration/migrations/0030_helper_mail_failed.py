# Generated by Django 2.2.1 on 2019-06-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_auto_20190202_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='mail_failed',
            field=models.CharField(blank=True, default=None, max_length=512, null=True),
        ),
    ]
