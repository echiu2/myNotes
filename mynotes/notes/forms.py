from django import forms
from .models import Note, sub_Note
from django.contrib.auth.models import User
import datetime

class createNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('slug',)
        fields = '__all__'
        labels = {
            'subject_text': ('Title'),
            'added_date': ('Date'),
            'note_field': ('Note')
        }
        widgets = {
            'note_field': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(createNoteForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = User.objects.filter(pk = user.id)
        self.fields['owner'].disabled = True

class subNoteForm(forms.ModelForm):
    class Meta:
        model = sub_Note
        exclude = ('slug',)
        fields = '__all__'
        labels = {
            'subject_text': ('Title'),
            'added_date': ('Date'),
            'note_field': ('Note')
        }
        widgets = {
            'note_field': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }

    def __init__(self, *args, **kwargs):
            super(subNoteForm, self).__init__(*args, **kwargs)
            self.fields['note'].disabled = True


