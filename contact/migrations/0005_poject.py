# Generated by Django 2.1.2 on 2019-01-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20190121_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('site', models.URLField()),
            ],
        ),
    ]
