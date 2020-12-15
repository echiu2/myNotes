from django.db import models
from django.conf import settings
from datetime import datetime    
from django.db.models.signals import pre_save
from django.urls import reverse
from mynotes.utils import unique_slug_generator

# Create your models here.
class Note(models.Model):
    subject_text = models.CharField(max_length=100)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    note_field = models.TextField("My field label", null=False, blank=False, max_length=1000)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.subject_text

    # def get_absolute_url(self):
    #     return reverse("note_content", kwargs={"slug": self.slug})

class sub_Note(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    subject_text = models.CharField(max_length=100)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    note_field = models.TextField("My field label", null=False, blank=False, max_length=1000)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.subject_text

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Note)

pre_save.connect(slug_generator, sender=sub_Note)

