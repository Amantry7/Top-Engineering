from django.shortcuts import render, get_object_or_404

from apps.base.models import Setting, Slider, About
from apps.project.models import Project, Service
from apps.categories.models import Category
from apps.secondary.models import Team, Reviews, News, Partner
# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    slider = Slider.objects.all()
    about = About.objects.latest('id')
    service = Service.objects.all()[:3]
    category = Category.objects.all()
    project = Project.objects.all()[:6]
    team = Team.objects.all()[:3]
    reviews = Reviews.objects.all()
    news = News.objects.all()
    part = Partner.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    service = Service.objects.all()[:3]
    category = Category.objects.all()
    project = Project.objects.all()[:6]
    team = Team.objects.all()[:3]
    reviews = Reviews.objects.all()
    news = News.objects.all()
    part = Partner.objects.all()
    return render(request, 'base/about-us.html', locals())

def news(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    news = News.objects.all()
    part = Partner.objects.all()
    return render(request, 'blog.html', locals())

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    return render(request, 'blog-details.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    part = Partner.objects.all()
    return render(request, 'contact.html', locals())