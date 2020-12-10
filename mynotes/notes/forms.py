from django import forms
from .models import Note, sub_Note
import datetime

class createNoteForm(forms.ModelForm):
    class Meta:
        model = Note
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

class subNoteForm(forms.ModelForm):
    class Meta:
        model = sub_Note
        fields = '__all__'
        # fields = ['subject_text', 'added_date', 'note_field']
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


