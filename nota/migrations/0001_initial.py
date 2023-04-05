# Generated by Django 4.2 on 2023-04-04 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, verbose_name='Nombres')),
                ('dui', models.CharField(max_length=9, unique=True, verbose_name='Nombres')),
                ('date_joined', models.DateField(default=datetime.datetime(2023, 4, 3, 18, 11, 4, 727714), verbose_name='Fecha de registro')),
                ('age', models.IntegerField(default=0, verbose_name='Edad')),
                ('salary', models.FloatField(default=0.0, verbose_name='Salario')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d', verbose_name='Imagen_Perfil')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d', verbose_name='Hoja de vida')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
            },
        ),
    ]
