from django.db import models

from accounts.models import Account
from common.models import CommonSlugModel
from .managers import ProjectManager


class Project(CommonSlugModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Project Name')
    app_url = models.URLField(verbose_name='App URL')
    repository_url = models.URLField(verbose_name='Repository URL')
    team = models.ManyToManyField(Account, verbose_name='Team')

    objects = ProjectManager()

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.title
