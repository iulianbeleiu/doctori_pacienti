# Generated by Django 2.2.12 on 2020-06-01 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0006_auto_20200527_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adresa',
            options={'verbose_name': 'Adresa', 'verbose_name_plural': 'Adrese'},
        ),
        migrations.AlterModelOptions(
            name='datemedicale',
            options={'verbose_name': 'Date Medicale', 'verbose_name_plural': 'Date Medicale'},
        ),
        migrations.AlterModelOptions(
            name='pacient',
            options={'verbose_name': 'Pacient', 'verbose_name_plural': 'Pacienti'},
        ),
        migrations.AlterModelOptions(
            name='recomandari',
            options={'verbose_name': 'Recomandari', 'verbose_name_plural': 'Recomandari'},
        ),
    ]
