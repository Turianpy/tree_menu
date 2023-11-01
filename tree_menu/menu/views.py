from typing import Any
from django.views.generic import TemplateView


class GPUs(TemplateView):
    template_name = 'gpus.html'


class BrandView(TemplateView):
    template_name = 'brand.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['brand'] = kwargs['brand']
        return context


class SeriesView(TemplateView):
    template_name = 'series.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['series'] = kwargs['series']
        return context


class ModelView(TemplateView):
    template_name = 'model.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model'] = kwargs['model']
        return context
