from django.shortcuts import render, get_object_or_404

from apps.base.models import Setting, About
from apps.categories.models import Category
from apps.project.models import Project
from apps.secondary.models import Partner
# Create your views here.

def project(request):
    setting = Setting.objects.latest('id')
    category = Category.objects.all()
    project = Project.objects.all()
    partner = Partner.objects.all()
    about = About.objects.latest('id')
    return render(request, 'project.html', locals())

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    rec_project = Project.objects.all()[:3]
    return render(request, 'project-details.html', locals())