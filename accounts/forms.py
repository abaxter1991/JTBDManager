from django import forms

from .models import Account


class AccountCreateModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'username',
            'email_address',
        )
