import random

from django.core.management.base import BaseCommand

from accounts.models import Account
from projects.models import Project


def get_random_team_name():
    team_list = []
    num_members = random.choice([3, 4, 5, 6, 7])
    accounts = [x.username for x in Account.objects.all()]

    while len(team_list) < num_members:
        team_list.append(random.choice(accounts))

    return team_list


class Command(BaseCommand):
    help = 'Management command to create mock Projects for testing purposes.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        project_details = [
            {
                'title': 'Rent Dynamics',
                'app_url': 'https://app.rentdynamics.com',
                'repository_url': 'https://github.com',
                'team': get_random_team_name(),
            },
            {
                'title': 'Rent Plus',
                'app_url': 'https://my.rentplus.com',
                'repository_url': 'https://github.com',
                'team': get_random_team_name(),
            },
            {
                'title': 'RD Admin',
                'app_url': 'https://admin.rentdynamics.com',
                'repository_url': 'https://github.com',
                'team': get_random_team_name(),
            },
            {
                'title': 'Hello Contact Center',
                'app_url': 'https://cc.rentdynamics.com',
                'repository_url': 'https://github.com',
                'team': get_random_team_name(),
            },
        ]

        for project_detail in project_details:
            Project.objects.create_project(
                title=project_detail['title'],
                app_url=project_detail['app_url'],
                repository_url=project_detail['repository_url'],
                team=project_detail['team'],
            )
