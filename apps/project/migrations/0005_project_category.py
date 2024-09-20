# Generated by Django 5.1.1 on 2024-09-15 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_title'),
        ('project', '0004_project_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_category', to='categories.category', verbose_name='Категория'),
        ),
    ]
