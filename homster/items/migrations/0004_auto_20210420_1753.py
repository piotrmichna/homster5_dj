# Generated by Django 3.1.7 on 2021-04-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210420_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gpiopincfg',
            options={'ordering': ['pin_board']},
        ),
        migrations.AlterUniqueTogether(
            name='gpiopincfg',
            unique_together={('buss_pin', 'pin_board')},
        ),
    ]
