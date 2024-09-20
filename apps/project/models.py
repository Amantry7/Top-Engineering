from django.db import models

from apps.categories.models import Category
# Create your models here.

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    desc = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    icon = models.ImageField(
        upload_to='service_icon/',
        verbose_name='Иконка'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Услуга',
        verbose_name_plural='Услуги'

class Project(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    desc = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    service = models.ForeignKey(
        Service, related_name='project_service',
        on_delete=models.CASCADE,
        verbose_name='Услуга'
    )
    category = models.ForeignKey(
        Category, related_name='project_category',
        on_delete=models.CASCADE, 
        verbose_name='Категория', 
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='project_image',
        verbose_name='Главное фото'
    )
    icon = models.ImageField(
        upload_to='project_icon', 
        verbose_name='Иконки'
    )
    banner = models.ImageField(
        upload_to='banner_project/',
        verbose_name='Баннер',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Проэкт'
        verbose_name_plural='Проэкты'
        
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='project_image',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='project_image',
        verbose_name='Фото'
    )
    class Meta:
        verbose_name='Фото проэкта'
        verbose_name_plural='Фото проэкта'
        
class ProjectInfo(models.Model):
    project = models.ForeignKey(
        Project, related_name='project_info',
        on_delete=models.CASCADE
    )
    key = models.CharField(
        max_length=255,
        verbose_name='Ключ'
    )
    valuem = models.CharField(
        max_length=255,
        verbose_name='Значение'
    )
    class Meta:
        verbose_name='Инфо о проэкте'
        verbose_name_plural='Инфо о проэкте'