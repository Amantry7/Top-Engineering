from django.urls import path

from apps.base.views import index, about, news, news_detail, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('contact/', contact, name='contact')
]
