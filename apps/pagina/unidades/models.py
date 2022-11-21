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

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        abstract = True


class UnitsModel(GeneralModel):
    logo_img = models.ImageField(
        "Logo",
        upload_to="inicio/unidades/",
        blank=True, null=True
    )

    content = RichTextField(
        "Contenido"
    )

    def __str__(self) -> str:
        return f"{self.section_name}"

    class Meta:
        verbose_name = "Pagina | Unidad"
        verbose_name_plural = "Pagina | Unidades"
        ordering = ["order", "id"]
        db_table = "apps_pagina_units_model"
