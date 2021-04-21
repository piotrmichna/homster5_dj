# Generated by Django 3.1.7 on 2021-04-20 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210420_1243'),
        ('programs', '0002_auto_20210420_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progpincfg',
            name='pin_cfg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpiopins', to='items.gpiopincfg', verbose_name='Pin sterujący'),
        ),
    ]