# Generated by Django 3.1.7 on 2021-05-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0031_remove_progpincfg_duration_sec'),
    ]

    operations = [
        migrations.AddField(
            model_name='progpincfg',
            name='duration_time',
            field=models.TimeField(default='00:00:01', verbose_name='Czas pracy'),
        ),
    ]
