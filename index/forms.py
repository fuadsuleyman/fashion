from django import forms
from .models import Subscriber
from django.forms import TextInput


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email',]
        widgets = {
            'email': TextInput(attrs={'class': 'form-control', 'id': 'mce-EMAIL', 'placeholder': 'Enter your email', 'type':'email'}),
        }