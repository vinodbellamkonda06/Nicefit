from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name