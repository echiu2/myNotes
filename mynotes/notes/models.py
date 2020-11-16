from django.db import models
from django.conf import settings

# Create your models here.
class Notes(models.Model):
    subject_text = models.CharField(max_length=100)
    added_date = models.DateTimeField('date added')
    note_field = models.TextField("My field label", null=False, blank=False, max_length=1000)


