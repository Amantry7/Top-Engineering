from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name='Фотография сотрудника'
    )
    desc = models.TextField(
        verbose_name='Описние',
        blank=True, null=True
    )
    rols = models.CharField(
        max_length=244,
        verbose_name='Должность'
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram',
        blank=True, null=True
    )
    linkedin = models.URLField(
        verbose_name='Ссылка на linkedin',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook',
        blank=True, null=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Комманда'
        verbose_name_plural='Комманды'
        
class TeamInfo(models.Model):
    team = models.ForeignKey(
        Team, related_name='team_info',
        on_delete=models.CASCADE
    )
    key = models.CharField(
        max_length=255
    )
    valuem = models.CharField(
        max_length=255
    )
    def __str__(self):
        return self.key
    
class TeamInfoDop(models.Model):
    team = models.ForeignKey(
        Team, related_name='team_info_dop',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    desc = models.TextField(
        verbose_name='Текст отзыва'
    )
    image = models.ImageField(
        upload_to='reviews/',
        verbose_name='Фото'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Отзыв клиента'
        verbose_name='Отзывы клиетов'
        
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Фотография'
    )
    auther = models.CharField(
        max_length=244,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата',
        auto_created=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        
class Partner(models.Model):
    image = models.ImageField(
        upload_to='partner/',
        verbose_name='Фото'
    )
    class Meta:
        verbose_name='Парнтер'
        verbose_name_plural='Парнтеры'
        
        
        
class Progres(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    icon = models.ImageField(
        upload_to='progres_icon/',
        verbose_name='Иконки'
    )
    desc = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Прогрец'
        verbose_name_plural='Прогрецы'
        
class Pricing(models.Model):
    icon = models.ImageField(
        upload_to='pricing_icon', 
        verbose_name='Иконка'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    price = models.PositiveIntegerField(
        verbose_name='цена'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Цены'
        verbose_name_plural='Цены'
        
class PricingService(models.Model):
    pricing = models.ForeignKey(
        Pricing, related_name='pricing_service',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Что входит в покет'
        verbose_name_plural='Что входит в покет'