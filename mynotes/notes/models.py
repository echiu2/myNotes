from django.db import models
from django.conf import settings
from datetime import datetime    

# Create your models here.
class Note(models.Model):
    subject_text = models.CharField(max_length=100)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    note_field = models.TextField("My field label", null=False, blank=False, max_length=1000)

    def __str__(self):
        return self.subject_text

class sub_Note(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    subject_text = models.CharField(max_length=100)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    note_field = models.TextField("My field label", null=False, blank=False, max_length=1000)

    def __str__(self):
        return self.subject_text


