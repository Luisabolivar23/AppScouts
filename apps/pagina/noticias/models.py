from django.utils import timezone
from django.db import models

from ckeditor.fields import RichTextField


class GeneralModel(models.Model):
    section_name = models.CharField(
        "Nombre o título",
        max_length=100
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
    )
    
    is_active = models.BooleanField(
        'Estado',
        default=True,
    )
    
    home_active = models.BooleanField(
        'Se muestra en el inicio',
        default=True
    )

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        abstract = True


class NewsModel(GeneralModel):
    img = models.ImageField(
        "Imagen",
        upload_to="news/img/",
        blank=True, null=True
    )

    content = RichTextField(
        "Contenido"
    )

    home_visible = models.BooleanField(
        "¿Es visible en el inicio?",
        default=True
    )

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        verbose_name = "Pagina | Noticia"
        verbose_name_plural = "Pagina | Noticias"
        ordering = ["order", "id"]
        db_table = "app_pagina_news_model"
