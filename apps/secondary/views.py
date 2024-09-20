from django.shortcuts import render, get_object_or_404

from apps.base.models import Setting, About, Choose
from apps.secondary.models import Pricing, Partner, Team, Reviews
from apps.project.models import Service
# Create your views here.
def pricing(request):
    setting = Setting.objects.latest('id')
    pricing = Pricing.objects.all()
    partner = Partner.objects.all()
    about = About.objects.latest('id')
    return render(request, 'pricing.html', locals())

def team(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    team = Team.objects.all()
    partner = Partner.objects.all()
    return render(request, 'team.html', locals())

def team_detail(request, id):
    team = get_object_or_404(Team, id=id)
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    partner = Partner.objects.all()
    return render(request, 'team-details.html', locals())

def service(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    partner = Partner.objects.all()
    service = Service.objects.all()
    choose = Choose.objects.all()
    reviews = Reviews.objects.all()
    team = Team.objects.all()[:3]
    pricing = Pricing.objects.all()
    partner = Partner.objects.all()
    return render(request, 'service.html', locals())