from django.shortcuts import render
from django.views.generic import TemplateView

from apps.pagina.inicio.models import HomeModel
from apps.pagina.noticias.models import NewsModel
from apps.pagina.unidades.models import UnitsModel


class HomeTemplateView(TemplateView):
    template_name = "pagina/inicio/inicio.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeTemplateView, self).get_context_data(**kwargs)
        ctx["inicio"] = HomeModel.objects.all()
        ctx["unidades"] = UnitsModel.objects.all()
        ctx["noticias"] = NewsModel.objects.all()
        return ctx
