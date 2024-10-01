from django.urls import path

from apps.project.views import project, project_detail, ajax_search

urlpatterns = [
    path('', project, name='project'),
    path('<int:id>/', project_detail, name='project_detail'),
    path('search/', ajax_search, name='search')
]

