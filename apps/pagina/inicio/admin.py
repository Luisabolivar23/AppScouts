from django.contrib import admin

from apps.pagina.inicio.models import HomeModel


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name', 'is_active')
    list_display_links = ('id', 'section_name')
    readonly_fields = ("created", "updated")
    ordering = ("order", "section_name", "id")
    search_fields = ("id", "section_name")


@admin.register(HomeModel)
class HomeAdmin(GeneralAdmin):
    pass
