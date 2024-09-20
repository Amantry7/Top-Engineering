# Generated by Django 5.1.1 on 2024-09-20 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_projectimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Ключ')),
                ('valuem', models.CharField(max_length=255, verbose_name='Значение')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_info', to='project.project')),
            ],
            options={
                'verbose_name': 'Инфо о проэкте',
                'verbose_name_plural': 'Инфо о проэкте',
            },
        ),
    ]