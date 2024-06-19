from django.contrib import admin

from .models import Job, Story, AcceptanceCriteria

admin.site.register(Job)
admin.site.register(Story)
admin.site.register(AcceptanceCriteria)
