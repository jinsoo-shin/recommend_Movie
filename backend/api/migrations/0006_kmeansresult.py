# Generated by Django 2.2.4 on 2019-08-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_usermovierating'),
    ]

    operations = [
        migrations.CreateModel(
            name='KmeansResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clusterlist', models.TextField()),
            ],
        ),
    ]
