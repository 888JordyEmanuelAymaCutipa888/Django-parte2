# Generated by Django 4.0.5 on 2022-06-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinosTuristicos', '0002_alter_destinoturistico_nombreciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinoturistico',
            name='nombreCiudad',
            field=models.CharField(max_length=100),
        ),
    ]