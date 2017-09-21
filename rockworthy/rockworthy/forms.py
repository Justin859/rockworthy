from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Query(forms.Form):
    
    name = forms.CharField(label='Your name', max_length=100, required=True)
    email = forms.EmailField(label='Your Email', max_length=255, required=True)
    query = forms.CharField(label='Your Query', max_length=1001, required=True)