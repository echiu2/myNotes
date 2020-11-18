from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=60)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email