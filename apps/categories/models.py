from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название категори'
    )
    desc = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'