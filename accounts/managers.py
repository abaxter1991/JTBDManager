from django.contrib.auth.models import BaseUserManager

from . import models as account_models


class UserAccountManager(BaseUserManager):
    def create_user(
            self,
            first_name,
            last_name,
            username,
            email_address,
            password,
            profile_settings=None,
            **extra_fields,
    ):
        if profile_settings is None:
            profile_settings = dict()

        if not email_address:
            raise ValueError('You must provide an email address')

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)

        email_address = self.normalize_email(email_address)

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email_address=email_address,
            **extra_fields,
        )

        user.set_password(password)
        user.save()

        profile_picture = None

        if profile_settings:
            profile_picture = profile_settings.get('profile_picture')

        profile = account_models.Profile.objects.create(user=user, profile_picture=profile_picture)
        profile.save()

        return user

    def create_superuser(
            self,
            first_name,
            last_name,
            username,
            email_address,
            password,
            profile_settings=None,
            **extra_fields,
    ):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must be assigned to is_admin=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(
            first_name,
            last_name,
            username,
            email_address,
            password,
            profile_settings,
            **extra_fields,
        )