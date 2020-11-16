from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notes
import datetime

class createNote(forms.Form):
    class Meta:
        model = Notes
        fields = ['title', 'date', 'note']

    title = forms.CharField(max_length=100)
    date = forms.DateTimeField(initial=datetime.datetime.now())
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))
