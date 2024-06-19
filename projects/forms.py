from django import forms

from .models import Project


class ProjectCreateModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'app_url',
            'repository_url',
            'slug',
            'team',
        )
        widgets = {
            'team': forms.CheckboxSelectMultiple(
                attrs={'class': 'overflow-hidden h-32 text-red-500'}
            )
        }
