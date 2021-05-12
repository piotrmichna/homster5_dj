# Generated by Django 3.1.7 on 2021-05-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20210506_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdaily',
            name='rain_m',
            field=models.BooleanField(default=False, verbose_name='Opady deszczu'),
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='rain_day_m',
            field=models.TimeField(default='00:00:00', verbose_name='Opady deszczu'),
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='rain_m',
            field=models.TimeField(default='00:00:00', verbose_name='Opady deszczu'),
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='rain_night_m',
            field=models.TimeField(default='00:00:00', verbose_name='Opady deszczu'),
        ),
    ]