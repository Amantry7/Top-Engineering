from django.urls import path

from apps.project.views import project, project_detail

urlpatterns = [
    path('', project, name='project'),
    path('<int:id>/', project_detail, name='project_detail'),
]
