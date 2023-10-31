from django.views.generic import TemplateView


class GPUs(TemplateView):
    template_name = 'gpus.html'
