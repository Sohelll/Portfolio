# Generated by Django 2.1.2 on 2019-01-21 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
