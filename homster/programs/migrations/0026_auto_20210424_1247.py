# Generated by Django 3.1.7 on 2021-04-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0025_auto_20210423_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='progpincfg',
            name='set_off',
            field=models.BooleanField(default=False, null=True, verbose_name='Wyłącz'),
        ),
        migrations.AddField(
            model_name='progpincfg',
            name='set_on',
            field=models.BooleanField(default=False, null=True, verbose_name='Włącz'),
        ),
    ]
