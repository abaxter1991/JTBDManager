from django.core.management.base import BaseCommand

from jobs.models import Job


class Command(BaseCommand):
    help = 'Management command to create mock jobs for testing purposes.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        job_details = [
            {
                'title': 'Push Charges',
                'project': 'Rent Plus',
                'status': 'Backlog',
            },
        ]

        for job_detail in job_details:
            Job.objects.create_job(
                title=job_detail['title'],
                project=job_detail['project'],
                status=job_detail['status'],
            )
