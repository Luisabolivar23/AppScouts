# Generated by Django 4.1.3 on 2022-11-21 04:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0002_alter_unitsmodel_logo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitsmodel',
            name='content',
            field=ckeditor.fields.RichTextField(default='Content', verbose_name='Contenido'),
            preserve_default=False,
        ),
    ]
