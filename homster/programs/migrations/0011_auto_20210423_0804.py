# Generated by Django 3.1.7 on 2021-04-23 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0010_auto_20210423_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progstarttime',
            name='next_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 8, 4, 10, 235907), verbose_name='Następny start'),
        ),
    ]
