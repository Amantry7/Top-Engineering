# Generated by Django 5.1.1 on 2024-09-19 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_alter_progres_options_pricingservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('valuem', models.CharField(max_length=255)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_info', to='secondary.team')),
            ],
        ),
    ]