from django.shortcuts import render, get_object_or_404, redirect

from apps.base.models import Setting, Slider, About, Contact, WorkProcessStep
from apps.project.models import Project, Service
from apps.categories.models import Category
from apps.secondary.models import Team, Reviews, News, Partner
# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    slider = Slider.objects.all()
    about = About.objects.latest('id')
    service = Service.objects.all()[:3]
    panel_service = Service.objects.all()
    category = Category.objects.all()
    project = Project.objects.all()[:6]
    team = Team.objects.all()[:3]
    reviews = Reviews.objects.all()
    news = News.objects.all()
    part = Partner.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('tel')
        email = request.POST.get('email')
        subject = request.POST.get('inquiries')
        text = request.POST.get('textarea')
        if not Contact.objects.filter(email=email).exists():
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                subject=subject,
                text=text
            )
            redirect('index')
        else:
            error_message = "Контакт с таким email уже существует."
            
    return render(request, 'base/index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    panel_service = Service.objects.all()
    service = Service.objects.all()[:3]
    category = Category.objects.all()
    project = Project.objects.all()[:6]
    team = Team.objects.all()[:3]
    reviews = Reviews.objects.all()
    steps = WorkProcessStep.objects.all()
    news = News.objects.all()
    part = Partner.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('tel')
        email = request.POST.get('email')
        subject = request.POST.get('inquiries')
        text = request.POST.get('textarea')
        if not Contact.objects.filter(email=email).exists():
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                subject=subject,
                text=text
            )
            redirect('index')
        else:
            error_message = "Контакт с таким email уже существует."
    return render(request, 'base/about-us.html', locals())

def news(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    news = News.objects.all()
    part = Partner.objects.all()
    panel_service = Service.objects.all()
    return render(request, 'blog.html', locals())

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    setting = Setting.objects.latest('id')
    panel_service = Service.objects.all()
    about = About.objects.latest('id')
    return render(request, 'blog-details.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    part = Partner.objects.all()
    panel_service = Service.objects.all()
    steps = WorkProcessStep.objects.all()

    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('tel')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('textarea')

        # Проверяем, есть ли уже контакт с таким email
        if not Contact.objects.filter(email=email).exists():
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                subject=subject,
                text=text
            )
            # Перенаправление на ту же страницу для избежания повторной отправки формы
            return redirect('contact')  # Убедитесь, что 'contact' - это имя пути в urls.py
        else:
            error_message = "Контакт с таким email уже существует."

    return render(request, 'contact.html', {
        'setting': setting,
        'about': about,
        'part': part,
        'panel_service': panel_service,
        'steps': steps,
        'error_message': error_message,
    })