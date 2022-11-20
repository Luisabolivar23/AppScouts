from django.contrib import admin

from apps.pagina.noticias.models import NoticiasModel

@admin.register(NoticiasModel)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    readonly_fields = ("creado", "actualizado", "orden")
    ordering = ("orden", "id")
    search_fields = ("id", "titulo")
    