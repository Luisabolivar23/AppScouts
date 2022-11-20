from django.contrib import admin

from apps.pagina.inicio.models import InicioModel, UnidadesModel


@admin.register(InicioModel)
class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    readonly_fields = ("creado", "actualizado", "orden")
    ordering = ("orden", "titulo")
    search_fields = ("id", "titulo")


@admin.register(UnidadesModel)
class UnidadesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    list_display_links = ("id", "nombre")
    readonly_fields = ("creado", "actualizado", "orden")
    ordering = ("orden", "nombre")
    search_fields = ("id", "nombre")
