from django import forms
from portfolio.models import Client

class SwitchClientForm(forms.Form):
    
    client = forms.ModelChoiceField(queryset=Client.objects.all(),
                empty_label=None,
                widget=forms.Select(attrs={ 'class': 'span-10' }))