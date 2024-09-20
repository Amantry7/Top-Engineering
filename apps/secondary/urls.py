from django.urls import path

from apps.secondary.views import pricing, team, team_detail, service

urlpatterns = [
    path('pricing/', pricing, name='pricing'),
    path('team/', team, name='team'),
    path('team/<int:id>/', team_detail, name='team_detail'),
    path('service/', service, name='service'),
]
