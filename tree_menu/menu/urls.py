from django.urls import path

from .views import GPUs

urlpatterns = [
    path('gpus', GPUs.as_view(), name='gpus'),
]
