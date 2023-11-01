from django.urls import path

from .views import GPUs, BrandView, SeriesView, ModelView

urlpatterns = [
    path('gpus', GPUs.as_view(), name='gpus'),
    path('gpus/<slug:brand>', BrandView.as_view(), name='brands'),
    path(
        'gpus/<slug:brand>/<slug:series>', SeriesView.as_view(), name='series'
    ),
    path(
        'gpus/<slug:brand>/<slug:series>/<slug:model>',
        ModelView.as_view(), name='model'
    ),
]
