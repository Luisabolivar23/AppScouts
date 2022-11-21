# Generated by Django 4.1.3 on 2022-11-21 01:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnitsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100, verbose_name='Nombre o título')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('logo_img', models.ImageField(upload_to='media/inicio/unidades/', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Pagina | Unidad',
                'verbose_name_plural': 'Pagina | Unidades',
                'db_table': 'apps_pagina_units_model',
                'ordering': ['order', 'id'],
            },
        ),
    ]
