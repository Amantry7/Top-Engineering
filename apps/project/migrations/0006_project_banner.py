# Generated by Django 5.1.1 on 2024-09-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner_project/', verbose_name='Баннер'),
        ),
    ]
