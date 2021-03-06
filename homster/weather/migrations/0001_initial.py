# Generated by Django 3.1.7 on 2021-05-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_m', models.DateTimeField(verbose_name='Data i czas pomiaru')),
                ('temp_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_m', models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')),
                ('humi_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_m', models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')),
            ],
            options={
                'verbose_name': 'Pogoda kilkudniowa',
                'verbose_name_plural': 'Pogoda kilkudniowa',
                'ordering': ['time_m'],
            },
        ),
        migrations.CreateModel(
            name='WeatherLong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_m', models.DateField(verbose_name='Data pomiarów')),
                ('temp_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_m', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Ciśnienie atmosferyczne')),
                ('humi_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_m', models.DecimalField(decimal_places=1, max_digits=7, verbose_name='Nasłonecznienie')),
                ('time_day_start', models.TimeField(verbose_name='Czas rozpoczęcia dnia')),
                ('time_day_stop', models.TimeField(verbose_name='Czas zakończenia dnia')),
                ('time_day', models.TimeField(verbose_name='Długość dnia')),
                ('temp_day_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_day_m', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Ciśnienie atmosferyczne')),
                ('humi_day_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_day_m', models.DecimalField(decimal_places=1, max_digits=7, verbose_name='Nasłonecznienie')),
                ('temp_night_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_night_m', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Ciśnienie atmosferyczne')),
                ('humi_night_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_night_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Nasłonecznienie')),
            ],
            options={
                'verbose_name': 'Pogoda - średnia dzienna',
                'verbose_name_plural': 'Pogoda - średnie dzienne',
                'ordering': ['date_m'],
            },
        ),
        migrations.CreateModel(
            name='WeatherWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_m', models.DateField(verbose_name='Data pomiarów')),
                ('temp_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_m', models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')),
                ('humi_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_m', models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')),
                ('time_day_start', models.TimeField(verbose_name='Czas rozpoczęcia dnia')),
                ('time_day_stop', models.TimeField(verbose_name='Czas zakończenia dnia')),
                ('temp_day_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_day_m', models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')),
                ('humi_day_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_day_m', models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')),
                ('temp_night_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Temperatura')),
                ('pres_night_m', models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')),
                ('humi_night_m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wilgotność powietrza')),
                ('ligh_night_m', models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')),
            ],
            options={
                'verbose_name': 'Pogoda - średnia tygodniowa',
                'verbose_name_plural': 'Pogoda - średnie tygodniowe',
                'ordering': ['date_m'],
            },
        ),
    ]
