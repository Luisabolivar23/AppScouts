from django.utils import timezone
from django.db import models

from apps.pagina.noticias.models import NoticiasModel


class UnidadesModel(models.Model):
    nombre = models.CharField(
        "Nombre",
        max_length=50
    )

    imagen = models.ImageField(
        "Imagen",
        upload_to="media/unidades"
    )

    url = models.URLField(
        "Url",
        max_length=500
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

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Pagina | Unidad"
        verbose_name_plural = "Pagina | Unidades"
        ordering = ["orden","nombre"]
        db_table = "app_pagina_inicio_unidades"


class InicioModel(models.Model):
    video = models.URLField(
        "Video del inicio",
        max_length=500
    )

    section_img = models.ImageField(
        "Img del about del inicio",
        upload_to="media/inicio"
    )

    titulo = models.CharField(
        "Título del about del inicio",
        max_length=100
    )

    descripcion = models.TextField(
        "Texto del about del inicio"
    )

    noticia = models.ManyToManyField(
        NoticiasModel
    )
    
    categorias = models.ManyToManyField(
        UnidadesModel
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
        verbose_name = "Pagina | Inicio"
        verbose_name_plural = "Pagina | Inicio"
        ordering = ["orden","titulo"]
        db_table = "app_pagina_inicio"
