# Generated by Django 5.1.1 on 2024-09-15 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_about_image_1_alter_about_image_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=244, verbose_name='Название')),
                ('state', models.IntegerField(verbose_name='Цифра')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_state', to='base.about', verbose_name='О нас')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистики',
            },
        ),
    ]
