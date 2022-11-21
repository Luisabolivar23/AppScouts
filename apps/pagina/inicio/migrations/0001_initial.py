# Generated by Django 4.1.3 on 2022-11-21 01:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticias', '0001_initial'),
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100, verbose_name='Nombre o título')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('video_link', models.URLField(max_length=500, verbose_name='Youtube video link')),
                ('img_content', models.ImageField(upload_to='media/inicio/banner/', verbose_name='Imagen del banner del inicio')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido del banner del inicio')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_news', to='noticias.newsmodel')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_units', to='unidades.unitsmodel')),
            ],
            options={
                'verbose_name': 'Pagina | Inicio',
                'verbose_name_plural': 'Pagina | Inicio',
                'db_table': 'apps_pagina_home_model',
                'ordering': ['order', 'id'],
            },
        ),
    ]