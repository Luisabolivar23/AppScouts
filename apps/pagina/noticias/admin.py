from django.contrib import admin

from apps.pagina.inicio.admin import GeneralAdmin
from apps.pagina.noticias.models import NewsModel



@admin.register(NewsModel)
class NoticiasAdmin(GeneralAdmin):
    pass
    