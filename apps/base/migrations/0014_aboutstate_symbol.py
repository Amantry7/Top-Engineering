# Generated by Django 5.1.1 on 2024-09-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_aboutstate_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutstate',
            name='symbol',
            field=models.CharField(default=1, max_length=2, verbose_name='Символ'),
            preserve_default=False,
        ),
    ]
