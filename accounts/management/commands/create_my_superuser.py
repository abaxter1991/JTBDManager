from django.core.management.base import BaseCommand

from accounts.models import Account


class Command(BaseCommand):
    help = 'Management command to create 1 superuser.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        profile_picture_path = 'images/profile_pictures/profile_picture_0.png'

        first_name = 'Austin'
        last_name = 'Baxter'
        username = 'abaxter'
        email_address = 'austin@example.com'
        password = '1234'
        is_active = True
        is_staff = True
        is_admin = True
        is_superuser = True

        profile_settings = {
            'profile_picture': profile_picture_path,
        }

        Account.objects.create_superuser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email_address=email_address,
            password=password,
            is_active=is_active,
            is_staff=is_staff,
            is_admin=is_admin,
            is_superuser=is_superuser,
            profile_settings=profile_settings,
        )
