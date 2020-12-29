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

    def __init__(self, *args, **kwargs):
        #get user keyword data 
        user = kwargs.pop('user', None)
        super(createNoteForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = User.objects.filter(pk = user.id)
        self.fields['owner'].disabled = True

    # def save(self, commit=True):
    #     instance = super(createNoteForm, self).save(commit=False)
    #     instance.subject_text = self.cleaned_data['subject_text'] # etc
    #     if commit:
    #         instance.save()
    #     return instance

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


