from django.db.models import Manager

from projects.models import Project


class JobManager(Manager):
    def create_job(self, title, project, status, **extra_fields):
        project_obj = Project.objects.get(title=project)
        slug = title.replace(' ', '')

        job = self.model(
            title=title,
            project=project_obj,
            status=status,
            slug=slug,
            **extra_fields,
        )

        job.save()

        return job
