from django.urls import path

from apps.base.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]
