# Generated by Django 3.1.7 on 2021-04-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0024_progstarttime_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progstarttime',
            name='next_time',
            field=models.DateTimeField(null=True, verbose_name='Następny start'),
        ),
    ]
