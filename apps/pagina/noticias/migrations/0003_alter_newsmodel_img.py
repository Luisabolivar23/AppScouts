# Generated by Django 4.1.3 on 2022-11-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_alter_newsmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news/img/', verbose_name='Imagen'),
        ),
    ]