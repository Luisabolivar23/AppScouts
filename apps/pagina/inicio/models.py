from django.utils import timezone
from django.db import models

from ckeditor.fields import RichTextField

from apps.pagina.noticias.models import NewsModel
from apps.pagina.unidades.models import UnitsModel


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

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        abstract = True


class HomeModel(GeneralModel):
    video_link = models.URLField(
        "Youtube video link",
        max_length=500
    )

    unit = models.ForeignKey(
        UnitsModel,
        on_delete=models.CASCADE,
        related_name="home_units"
    )

    img_content = models.ImageField(
        "Imagen del banner del inicio",
        upload_to="media/inicio/banner/"
    )

    content = RichTextField(
        "Contenido del banner del inicio"
    )

    news = models.ForeignKey(
        NewsModel,
        on_delete=models.CASCADE,
        related_name="home_news"
    )

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        verbose_name = "Pagina | Inicio"
        verbose_name_plural = "Pagina | Inicio"
        ordering = ["order", "id"]
        db_table = "apps_pagina_home_model"
