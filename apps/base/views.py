from django.shortcuts import render

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