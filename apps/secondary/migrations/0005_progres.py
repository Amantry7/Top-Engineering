# Generated by Django 5.1.1 on 2024-09-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('icon', models.ImageField(upload_to='progres_icon/', verbose_name='Иконки')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Прогрецы',
            },
        ),
    ]
