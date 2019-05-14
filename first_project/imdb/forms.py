
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    message = forms.CharField()

