from django.utils import timezone
from django.db import models

# Create your models here.


class NoticiasModel(models.Model):
    img = models.ImageField(
        "Imagen de presentación de la noticia",
        upload_to="media/noticias"
    )

    titulo = models.CharField(
        "titulo",
        max_length=200
    )

    descripcion = models.TextField(
        "Descripción de la noticia"
    )
    
    creado = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        blank=True, null=True
    )

    actualizado = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        blank=True, null=True
    )

    orden = models.PositiveIntegerField(
        'Orden',
        default=0,
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return f"{self.titulo}"
    
    class Meta:
        verbose_name = "Pagina | Noticia"
        verbose_name_plural = "Pagina | Noticias"
        ordering = ["orden", "id"]
        db_table = "app_pagina_noticia"