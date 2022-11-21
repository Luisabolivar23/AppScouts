from django.contrib import admin

from apps.pagina.inicio.admin import GeneralAdmin
from apps.pagina.unidades.models import UnitsModel


@admin.register(UnitsModel)
class UnitsAdmin(GeneralAdmin):
    pass
