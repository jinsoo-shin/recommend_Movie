# Generated by Django 2.2.4 on 2019-09-25 12:05

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieContent',
            fields=[
                ('id', models.IntegerField(default=api.models.number, primary_key=True, serialize=False, unique=True)),
                ('ImdbLink', models.CharField(max_length=500)),
                ('posterUrl', models.CharField(max_length=500)),
                ('Summary', models.CharField(max_length=500)),
                ('Director', models.CharField(max_length=500)),
                ('Writers', models.CharField(max_length=500)),
            ],
        ),
    ]
