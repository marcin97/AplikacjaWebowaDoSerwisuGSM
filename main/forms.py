from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import ugettext_lazy as _


class PhoneForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial='PL'),
        }