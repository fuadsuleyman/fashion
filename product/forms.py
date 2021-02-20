from django import forms
from django.forms import TextInput


class SearchForm(forms.Form):
    class Meta:
        widgets = {
            '': TextInput(attrs={'class': 'form-control', 'placeholder': 'Search', 'type':'text'}),
        }