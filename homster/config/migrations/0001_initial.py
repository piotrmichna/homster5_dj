# Generated by Django 3.1.7 on 2021-05-05 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CfgType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64, null=True, verbose_name='Opis typu polecenia')),
                ('name', models.CharField(max_length=16, verbose_name='Nazwa typu polecenia')),
            ],
            options={
                'verbose_name': 'Typ komendy',
                'verbose_name_plural': 'Konfiguracja - typy komend',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CfgCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64, null=True, verbose_name='Opis polecenia')),
                ('name', models.CharField(max_length=16, verbose_name='Komenda')),
                ('value', models.CharField(max_length=16, verbose_name='Wartość')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.cfgtype', verbose_name='Typ komendy')),
            ],
            options={
                'verbose_name': 'Konfiguracja',
                'verbose_name_plural': 'Konfiguracja - komendy',
                'ordering': ['type__description', 'name'],
            },
        ),
    ]
