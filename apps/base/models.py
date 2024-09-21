from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название сайта'
    )
    desc = models.TextField(
        verbose_name='Описание компании'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    schedul = models.CharField(
        max_length=255,
        verbose_name='График работы'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook',
        blank=True, null=True
    )
    linkendin = models.URLField(
        verbose_name='Ссылка на linkendin',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram',
        blank=True, null=True
    )
    whatsapp = models.CharField(
        max_length=255,
        verbose_name='Номер whatsapp',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Настройка сайта'
        verbose_name_plural='Настройки сайта'
        
class Slider(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    button_text = models.CharField(
        max_length=20,
        verbose_name='Текст кнопки'
    )
    url = models.URLField(
        verbose_name='Ссылка',
        help_text='Куда перейдет при нажати на кнопку',
        blank=True, null=True
    )
    video = models.URLField(
        verbose_name='Видео',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Слайдер'
        verbose_name_plural='Слайдеры'
        
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    banner = models.ImageField(
        upload_to='about-banner/',
        verbose_name='Баннер' 
    )
    video = models.URLField(
        verbose_name='Видео',
        blank=True, null=True
    )
    image_1 = models.ImageField(
        upload_to='about/image',
        verbose_name="Фото 1",
        blank=True, null=True
    )
    image_2 = models.ImageField(
        upload_to='about/image',
        verbose_name="Фото 2",
        blank=True, null=True
    )
    image_3 = models.ImageField(
        upload_to='about/image',
        verbose_name="Фото 3",
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'
        
class AboutService(models.Model):
    about = models.ForeignKey(
        About, related_name='about_service',
        on_delete=models.CASCADE, 
        verbose_name='О нас'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    class Meta:
        verbose_name='Услуги'
        verbose_name_plural='Услуги'
        
class AboutState(models.Model):
    about = models.ForeignKey(
        About, related_name='about_state',
        on_delete=models.CASCADE,
        verbose_name='О нас'
    )
    title = models.CharField(
        max_length=244,
        verbose_name='Название'
    )
    state = models.CharField(
        max_length=255,
        verbose_name='Цифра'
    )
    symbol = models.CharField(
        max_length=2,
        verbose_name='Символ'
    )
    icon = models.ImageField(
        upload_to='icon-state/',
        verbose_name='Иконки'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Статистика'
        verbose_name_plural='Статистики'
        
class AboutSkill(models.Model):
    about = models.ForeignKey(
        About, related_name='about_skill',
        on_delete=models.CASCADE,
        verbose_name='О нас'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    number = models.CharField(
        max_length=255,
        verbose_name='Значение'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Навык'
        verbose_name_plural='Навыки'
        
class Choose(models.Model):
    icon = models.ImageField(
        upload_to='choose_icon',
        verbose_name='Иконка'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Почему выберают нас'
        verbose_name_plural='Почему выберают нас'
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    subject = models.CharField(
        max_length=255,
        verbose_name='Запрос'
    )
    text = models.TextField(
        verbose_name='Сообщение'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Запросы о обратоной связи'
        verbose_name_plural='Запросы о обратоной связи'