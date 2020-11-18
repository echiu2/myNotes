from django import forms
from .models import Note
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

