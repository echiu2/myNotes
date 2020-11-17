from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Note
import datetime

class createNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'date', 'note']

    title = forms.CharField(max_length=100)
    date = forms.DateTimeField(initial=datetime.datetime.now())
    note = forms.CharField(max_length= 1000, widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))

