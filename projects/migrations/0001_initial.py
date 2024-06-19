# Generated by Django 3.2.5 on 2024-06-19 11:24

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Project Name')),
                ('app_url', models.URLField(verbose_name='App URL')),
                ('repository_url', models.URLField(verbose_name='Repository URL')),
                ('team', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Team')),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
