from django.db.models import Manager

from accounts.models import Account


class ProjectManager(Manager):
    def create_project(self, title, app_url, repository_url, team, **extra_fields):
        slug = title.replace(' ', '')

        project = self.model(
            title=title,
            app_url=app_url,
            repository_url=repository_url,
            slug=slug,
            **extra_fields,
        )

        project.save()

        user_id_list = []

        for username in team:
            user = Account.objects.get(username=username)
            user_id_list.append(user.id)
            project.team.add(user)

        return project
