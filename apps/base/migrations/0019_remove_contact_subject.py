# Generated by Django 5.1.1 on 2024-10-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_workprocessstep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]