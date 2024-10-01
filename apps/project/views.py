from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse

from apps.base.models import Setting, About
from apps.categories.models import Category
from apps.project.models import Project, Service
from apps.secondary.models import Partner, News
# Create your views here.

def project(request):
    setting = Setting.objects.latest('id')
    category = Category.objects.all()
    project = Project.objects.all()
    partner = Partner.objects.all()
    panel_service = Service.objects.all()
    about = About.objects.latest('id')
    return render(request, 'project.html', locals())

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    panel_service = Service.objects.all()
    rec_project = Project.objects.all()[:3]
    return render(request, 'project-details.html', locals())

def ajax_search(request):
    query = request.GET.get('query', '').strip()  # Получаем и очищаем запрос
    print('Запрос:', query)
    
    project = Project.objects.none()  # Инициализируем пустые QuerySets
    news = News.objects.none()

    if query:
        query_words = query.split()  # Разбиваем запрос на слова
        project_query = Q()
        news_query = Q()

        # Формируем запросы для проектов и новостей по каждому слову в запросе
        for word in query_words:
            project_query |= Q(title__icontains=word)
            news_query |= Q(title__icontains=word)

        print('Project query:', project_query)
        print('News query:', news_query)

        # Выполняем запросы к базе данных
        project = Project.objects.filter(project_query).values('id', 'title')
        news = News.objects.filter(news_query).values('id', 'title')

        print('Project:', project)
        print('News:', news)

    # Возвращаем результат в формате JSON
    return JsonResponse({'project': list(project), 'news': list(news)})