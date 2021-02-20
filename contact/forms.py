from django import forms
from .models import Contact
from django.forms import ModelForm, Textarea, TextInput

class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_num', 'email', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id':'name', 'placeholder': 'Enter your name', 'type': 'text'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last-name', 'placeholder': 'Enter your last name', 'type': 'text'}),
            'phone_num': TextInput(attrs={'class': 'form-control', 'id': 'review', 'placeholder': 'Enter your number', 'type': 'number'}),
            'email': TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email', 'type': 'email'}),
            'message': Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'placeholder': 'Write your message', 'type': 'text'}),
        }