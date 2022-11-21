from django.urls import path

from apps.pagina.inicio.views import HomeTemplateView

app_name = "inicio"

urlpatterns = [
    path(
        "",
        HomeTemplateView.as_view(),
        name = "inicio"
    )
]