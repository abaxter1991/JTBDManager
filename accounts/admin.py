from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account, Profile


class AccountAdminConfig(UserAdmin):
    model = Account

    list_display = [
        'first_name',
        'last_name',
        'username',
        'email_address',
        'is_active',
        'is_staff',
        'is_admin',
        'is_superuser',
    ]

    ordering = [
        'first_name',
        'last_name',
    ]

    search_fields = [
        'username',
        'email_address',
        'first_name',
        'last_name',
    ]

    list_filter = [
        'first_name',
        'last_name',
        'username',
        'email_address',
        'is_active',
        'is_staff',
        'is_admin',
        'is_superuser',
    ]

    fieldsets = (
        ('User Settings', {
            'fields': [
                'first_name',
                'last_name',
                'username',
                'email_address',
                'password',
            ],
        }),
        ('Permissions', {
            'fields': [
                'is_active',
                'is_staff',
                'is_admin',
                'is_superuser',
            ],
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ['wide'],
                'fields': [
                    'first_name',
                    'last_name',
                    'username',
                    'email_address',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_admin',
                    'is_superuser',
                ],
            },
        ),
    )


admin.site.register(Account, AccountAdminConfig)
admin.site.register(Profile)
