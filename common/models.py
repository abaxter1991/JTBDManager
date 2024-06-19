import uuid

from django.db import models


class CommonModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')

    class Meta:
        abstract = True


class CommonSlugModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, verbose_name='UUID')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True
